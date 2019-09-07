# DE-EXFILTRATOR
## A PYTHON SCRIPT FILE TO DECRYPT BASE64/RC4 ENCRYPTED DNS EXFILTRATION ZIP-FILE MESSAGES CAPTURED VIA WIRESHARK.

Usage: python de-exfiltrator.py

| LANGUAGE | FILENAME          | MD5 HASH                         |
|------    |------             | -------                          |
| python   | de_exfiltrator.py | 631417f5666ccaabea230a9d33da81ab |

- [x] See [DNSExfiltrator](https://github.com/Arno0x/DNSExfiltrator) for further information.
- [x] Requires 3rd party [RC4](https://pypi.org/project/arc4/) to be installed.

[DNSExfiltrator](https://github.com/Arno0x/DNSExfiltrator) uses the variables shown below, as part of its exfiltration transmission. They can be easily detected and extracted via Wireshark analysis.

__KNOWN VARIABLES__ </br>
Domain </br>
Filename </br>
Password </br>
Message </br>

Once these variables have been obtained, plug them into the python file to reveal the stolen exfiltration data.

### CONSOLE DISPLAY
![Screenshot](picture1.png)
