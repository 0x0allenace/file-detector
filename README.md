# file_detector.py
**Lightweight file type detector for reverse engineering, DFIR, and malware analysis.**

## Overview
`file_detector.py` is a lightweight Python tool that identifies the true file type of a file by analyzing its magic bytes (binary signatures), rather than relying on file extensions.

This makes it especially useful in DFIR, malware analysis, and reverse engineering, where file extensions are often misleading or intentionally manipulated.



## Features
- ✅ Detects common file types: **EXE**, **ELF**, **ZIP**, and **PDF** files  
- ✅ Uses **magic byte signature** analysis (not file extensions)  
- ✅ Color-coded terminal output using `termcolor`  
- ✅ Safe for **malware triage and static analysis**  
- ✅ Easily extendable with additional file signatures

## Installation
```bash
git clone https://github.com/0x0allenace/file-detector.git
cd file-detector
pip install termcolor
```

## Usage
```bash
python3 file_detector.py
```

## Example
```bash
Enter file name: invoice.exe.zip
Found file type: ZIP
```

If unknown:
```text
File type could not be identified
```

## How It Works

Files contain unique identifiers called magic bytes at the beginning of their binary structure.

| File Type | Signature (Hex) |
|----------|------------------|
| EXE      | `4D 5A (MZ)`     |
| ELF      | `7F 45 4C 46`    |
| ZIP      | `50 4B 03 04`    |
| PDF      | `25 50 44 46 2D` |

## Use Cases

Perfect for:
- Malware triage and safe file inspection  
- Digital forensics investigations  
- Reverse engineering workflows  
- Suspicious file verification
- Security lab environments  

## Project Structure
```text
file-detector/
├── file_detector.py
└── README.md
```

## Future Enhancements
- [ ] Add more file signatures (PNG, JPG, DOCX, etc.)  
- [ ] Generate file hashes (SHA256, MD5) 
- [ ] Integrate into a DFIR automation pipeline 
- [ ] Build a GUI version (drag & drop support)  

## 👨🏾‍💻 Author  
**Allen Ace**  
Cybersecurity Enthusiast | Reverse Engineering & DFIR | Machine Learning 

📍 **LinkedIn:** [linkedin.com/in/allen-ace-soc-analyst](https://www.linkedin.com/in/allen-ace-soc-analyst/)  
🐙 **GitHub:** [github.com/0x0allenace](https://github.com/0x0allenace)  
🕊️ **X (Twitter):** [x.com/allen_acee](https://x.com/allen_acee)


## Keywords
`Cybersecurity` · `Reverse Engineering` · `DFIR` · `Malware Analysis` · `Python` · `Magic Bytes` · `Forensics`
