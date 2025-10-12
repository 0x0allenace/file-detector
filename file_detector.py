from termcolor import cprint
import os
import sys

file_signatures = {
    'EXE': {
        'magic_bytes': b'\x4d\x5a',
        'offset': 0,
        'number_bytes': 2
    },
    'ELF': {
        'magic_bytes': b'\x7f\x45\x4c\x46',
        'offset': 0,
        'number_bytes': 4,
        'class_offset': 4,
        'endianness_offset': 5,
        'start_offset': 24
    },
    'ZIP': {
        'magic_bytes': b'\x50\x4B\x03\x04',
        'offset': 0,
        'number_bytes': 4
    },
    'PDF': {
        'magic_bytes': b'\x25\x50\x44\x46\x2D',
        'offset': 0,
        'number_bytes': 5
    },
}
# prompt user to enter the file name to be analyzed

file_name = input('Enter file name: ').strip()

# basic path checks (prevents crashes)
if not os.path.exists(file_name):
    cprint(f'Error: File "{file_name}" not found', 'red')
    sys.exit(1)
if os.path.isdir(file_name):
    cprint(f'Error: "{file_name}" is a directory, not a file!', 'red')
    sys.exit(1)
found = False
# open file safely
try:
    with open(file_name, 'rb') as f:
        for file_type, attributes in file_signatures.items():
            # ensure we seek to an integer offset even if it's stored as a string
            f.seek(int(attributes['offset']))
            magic_bytes = f.read(attributes['number_bytes'])
            if magic_bytes == attributes['magic_bytes']:
                cprint(f'Found file type: {file_type}', 'green')

                if file_type == 'ELF':
                    # read class (32 vs 64-bit)
                    f.seek(attributes['class_offset'])
                    elf_class = f.read(1)
                    # read endianness
                    f.seek(attributes['endianness_offset'])
                    endianness_byte = f.read(1)
                    endianness = 'little' if endianness_byte == b'\x01' else 'big'
                    print(f'Endianness: {endianness.capitalize()}')

                    # read start address (entry point) at start_offset
                    f.seek(attributes['start_offset'])
                    if elf_class == b'\x01':  # ELF32
                        print('Class: ELF32')
                        start_bytes = f.read(4)
                    else:  # ELF64
                        print('Class: ELF64')
                        start_bytes = f.read(8)

                    # convert to int using the detected endianness
                    start_address_as_int = int.from_bytes(start_bytes, byteorder=endianness)
                    print(f'Start Address: {hex(start_address_as_int)}')

                found = True
                break  # stop after detecting the file type

finally:
    if not found:
        cprint('File type could not be determined', 'red')
