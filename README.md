# DE-EXFILTRATOR
## A PYTHON SCRIPT FILE TO DECRYPT BASE64/RC4 ENCRYPTED DNS EXFILTRATION FILES CAPTURED VIA WIRESHARK.

Usage: python de-exfiltrator.py

| LANGUAGE | FILENAME          | MD5 Hash                                    |
|------    |------             | -------                                     |
| python   | de-exfiltrator.py | MD5 Hash - 6537dac7c3f7dfb2d5a15b320047396f |

- [x] Requires 3rd party [RC4](https://pypi.org/project/arc4/) to be installed.
- [x] See [DNSExfiltrator](https://github.com/Arno0x/DNSExfiltrator) for further information.

[DNSExfiltrator](https://github.com/Arno0x/DNSExfiltrator) uses the variables shown below as part of its exfiltration transmission, they can be extracted via elementary Wireshark analysis and decoded.

__VARIABLES__ </br>
Domain </br>
Filename </br>
Password </br>
Message </br>

### CONSOLE DISPLAY
![Screenshot](picture1.png)
