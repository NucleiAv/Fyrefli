# Fyrefli
FyreFli is a python based obfuscator made by Anmol along with Suryansh and Sharvil. It can perform a variety of tasks.

# Contributions -
Anmol Vats : Python Script i.e. obfu.py file ; Sharvil Bhatt : R & D, DS Underdogs Webpage and Web-Development ; Suryansh Arya : API, All scripts/codes in JS.

Our website <a href = "https://dsunderdogs.github.io/websitedsunder.github.io/" >dsundergods.website</a>

# A Concise Definition:
FyreFli is a python based obfuscator. It can do a variety of tasks from encoding to encryption to obfuscation; from unicode character encoding methods like utf8, utf16 to hash functions like sha3-256, md5.

TechStack - Python, ReactJs, Js, Flask

# [obfu.py]
A script to obfuscate your payloads easily to your desired encodings.

# Obfuscation and how it's different than Encrytption
In network security, obfuscation refers to methods used to obscure an attack payload from inspection by network protection systems. In white-box cryptography, obfuscation refers to the protection of cryptographic keys from extraction when they are under the control of the adversary, e.g., as part of a DRM scheme.

Obfuscation, also referred to as beclouding, is to hide the intended meaning of the contents of a file, making it ambiguous, confusing to read, and hard to interpret. Encryption is to actually transform the contents of the file, making it unreadable to anyone unless they apply a special key.

# Usage:
```
$ python obfu.py -h                      
______________________________________________________________________________________________________________________________________

        FyreFli Obfuscator
........................................................................................................................................

usage: python obfu.py [-h] [-s STR] [-ueo] [-udi] [-e ENC] [-hash HASH] [-f]

Required Arguments:
  -s STR, --str STR  String to obfuscate

Optional Arguments:
  -ueo               URL Encode Output
  -udi               URL Decode Input
  -e ENC             Encoding type. eg: ibm037 , utf8 , utf16 , utf32 , etc
  -hash HASH         Enable Hash Input
  -f                 Enable File Input
  -cipher CIPHER     cipher to use
  -key KEY           additional info
  -task TASK         encrypt or decrypt

Example Usage:
$ python obfu.py -s 'input.txt' -f -e utf16 
________________________________________________________________________________________________________________________________________

        FyreFli Obfuscator
........................................................................................................................................



Input: input.txt

Buffer: 
Hello This is Anmol Vats.

FyreFli is a project by Anmol.

It is under the team of dsunderdogs.

Hatsoff to Suryansh and Sharvil for their contributions as well.

Hopre you like this tool.


Hash: None

Output: b'\xff\xfe\n\x00H\x00e\x00l\x00l\x00o\x00 \x00T\x00h\x00i\x00s\x00 \x00i\x00s\x00 \x00A\x00n\x00m\x00o\x00l\x00 \x00V\x00a\x00t\x00s\x00.\x00\n\x00\n\x00F\x00y\x00r\x00e\x00F\x00l\x00i\x00 \x00i\x00s\x00 \x00a\x00 \x00p\x00r\x00o\x00j\x00e\x00c\x00t\x00 \x00b\x00y\x00 \x00A\x00n\x00m\x00o\x00l\x00.\x00\n\x00\n\x00I\x00t\x00 \x00i\x00s\x00 \x00u\x00n\x00d\x00e\x00r\x00 \x00t\x00h\x00e\x00 \x00t\x00e\x00a\x00m\x00 \x00o\x00f\x00 \x00d\x00s\x00u\x00n\x00d\x00e\x00r\x00d\x00o\x00g\x00s\x00.\x00\n\x00\n\x00H\x00a\x00t\x00s\x00o\x00f\x00f\x00 \x00t\x00o\x00 \x00S\x00u\x00r\x00y\x00a\x00n\x00s\x00h\x00 \x00a\x00n\x00d\x00 \x00S\x00h\x00a\x00r\x00v\x00i\x00l\x00 \x00f\x00o\x00r\x00 \x00t\x00h\x00e\x00i\x00r\x00 \x00c\x00o\x00n\x00t\x00r\x00i\x00b\x00u\x00t\x00i\x00o\x00n\x00s\x00 \x00a\x00s\x00 \x00w\x00e\x00l\x00l\x00.\x00\n\x00\n\x00H\x00o\x00p\x00r\x00e\x00 \x00y\x00o\x00u\x00 \x00l\x00i\x00k\x00e\x00 \x00t\x00h\x00i\x00s\x00 \x00t\x00o\x00o\x00l\x00.\x00'

_________________________________________________________________________________________________________________________________________

$ python obfu.py -s 'param=<svg/onload=prompt()//' -e ibm037 -ueo
        FyreFli Obfuscator

Input: param=<svg/onload=prompt()//
Buffer: (If Any, But here it's not shown as no file is present)
Hash: (If Any, But here it's "None")
Output: %97%81%99%81%94~L%A2%A5%87a%96%95%93%96%81%84~%97%99%96%94%97%A3M%5Daa
```
# Sidenote:
This script can encode in all types of formats which are supported by the Python Engine. Made by Anmol Vats, Suryansh Arya, Sharvil Bhatt under the team/flagship of DS Underdogs.
