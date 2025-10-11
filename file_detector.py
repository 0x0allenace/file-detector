from termcolor import cprint
import os

file_signatures = {
    'EXE': {
        'magic_bytes': b'\x4d\x5a',
        'offset': 0,
        'number_bytes': 2
    },
    'ELF': {
        'magic_bytes': b'\x7f\x45\x4c\x46',
        'offset': 0,
        'number_bytes': 4
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
    raise SystemExit(1)
if os.path.isdir(file_name):
    cprint(f'Error: "{file_name}" is a directory, not a file!', 'red')
    raise SystemExit(1)

# open file safely
try:
    f = open(file_name, 'rb')
except Exception as e:
    cprint(f'Error opening file: {e}', 'red')
    raise SystemExit(1)

found = False
try:
    for file_type, attributes in file_signatures.items():
        f.seek(int(attributes['offset']))
        magic_bytes = f.read(attributes['number_bytes'])
        if magic_bytes == attributes['magic_bytes']:
            cprint(f'Found file type: {file_type}', 'green')
            found = True
            break  # stop after detecting the type
finally:
    f.close()

if not found:
    cprint('File type could not be identified', 'red')
