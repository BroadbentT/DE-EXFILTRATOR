# DE-EXFILTRATOR
## A PYTHON SCRIPT FILE TO DECRYPT BASE64/RC4 ENCRYPTED DNS EXFILTRATION FILES CAPTURED VIA WIRESHARK.

Usage: python de-exfiltrator.py

| LANGUAGE | FILENAME          | MD5 Hash                                    |
|------    |------             | -------                                     |
| python   | de-exfiltrator.py | MD5 Hash - 6537dac7c3f7dfb2d5a15b320047396f |

- [x] Requires 3rd party [RC4](https://pypi.org/project/arc4/) to be installed.
- [ ] See [DNSExfiltrator](https://github.com/Arno0x/DNSExfiltrator) for further information.

A python script file to decrypt BASE64/RC4 encrypted DNS exfiltration files from known variables extracted via Wireshark.

__VARIABLES__

Domainname </br>
Filename </br>
Password </br>
Message </br>

DNSExfiltrator uses the above variables as part of its exfiltration transmission, they can be extracted via elementary Wireshark analysis.

### CONSOLE DISPLAY
![Screenshot](picture1.png)
