# file_detector.py
**Lightweight file type detector for reverse engineering, DFIR, and malware analysis.**

## Overview
`file_detector.py` is a simple Python script that identifies the real type of a file by reading its **magic bytes** — the unique signatures stored at the beginning of most binary files.

This helps reverse engineers, forensic analysts, and cybersecurity learners quickly identify file formats (EXE, ELF, ZIP, PDF, etc.) — even when extensions are missing or intentionally disguised.


## Features
- ✅ Detects **EXE**, **ELF**, **ZIP**, and **PDF** files  
- ✅ Uses **magic byte matching** (not file extensions)  
- ✅ Displays results in color-coded output with `termcolor`  
- ✅ Safe to use for **malware triage and static analysis**  
- ✅ Easily extendable — just add more signatures  


## Example Usage
```bash
python3 file_detector.py
Enter file name: invoice.exe.zip
Found file type: ZIP
```

If the file type isn’t recognized:
```bash
File type could not be identified
```

## Why It’s Useful for Reverse Engineering
When analyzing unknown binaries, you can’t always trust the file extension.  
Attackers often rename `.exe` files as `.txt` or `.zip` to evade detection.  
This tool lets you **peek into the binary header** to verify what the file truly is — safely and quickly, without executing anything.

Perfect for:
- Malware triage  
- Binary research  
- DFIR workflows  
- Forensic file identification  

## 🧩 How It Works
Each file type has a *magic byte sequence* — a small identifier stored at the start of the file.  
Example:
- **EXE:** `4D 5A` (`MZ`)  
- **ELF:** `7F 45 4C 46`  
- **ZIP:** `50 4B 03 04`  
- **PDF:** `25 50 44 46 2D`

The script reads the first few bytes, compares them against known signatures, and prints the matching file type.

## Requirements
- Python 3.x  
- `termcolor` module

Install with:
```bash
pip install termcolor
```

## Future Enhancements
- [ ] Add more file signatures (PNG, JPG, DOCX, etc.)  
- [ ] Generate SHA256 hashes for each file  
- [ ] Integrate into a DFIR automation toolkit  
- [ ] Optional GUI version with drag & drop  

## 👨🏾‍💻 Author  
**Allen Ace**  
Cybersecurity Enthusiast | Reverse Engineering & DFIR Learner  

📍 **LinkedIn:** [linkedin.com/in/allen-ace-soc-analyst](https://www.linkedin.com/in/allen-ace-soc-analyst/)  
🐙 **GitHub:** [github.com/0x0allenace](https://github.com/0x0allenace)  
🕊️ **X (Twitter):** [x.com/allen_acee](https://x.com/allen_acee)


## Keywords
`Cybersecurity` · `Reverse Engineering` · `DFIR` · `Malware Analysis` · `Python` · `Magic Bytes` · `Forensics`
