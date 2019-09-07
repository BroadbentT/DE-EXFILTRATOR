# DE-EXFILTRATOR
## A PYTHON SCRIPT FILE TO DECRYPT BASE64/RC4 ENCRYPTED DNS EXFILTRATION FILES CAPTURED VIA WIRESHARK.

Usage: python de-exfiltrator.py

| LANGUAGE | FILENAME          | MD5 HASH                         |
|------    |------             | -------                          |
| python   | de-exfiltrator.py | 6537dac7c3f7dfb2d5a15b320047396f |

- [x] See [DNSExfiltrator](https://github.com/Arno0x/DNSExfiltrator) for further information.
- [x] Requires 3rd party [RC4](https://pypi.org/project/arc4/) to be installed.

[DNSExfiltrator](https://github.com/Arno0x/DNSExfiltrator) uses the known variables shown below as part of its exfiltration transmission, they can be easily extracted via Wireshark and decoded for analysis.

__KNOWN VARIABLES__ </br>
Domain </br>
Filename </br>
Password </br>
Message </br>

### CONSOLE DISPLAY
![Screenshot](picture1.png)
