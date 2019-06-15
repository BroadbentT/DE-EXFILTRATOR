#!/usr/bin/python
# coding:UTF-8

# -------------------------------------------------------------------------------------
#    PYTHON UTILITY FILE TO CRACK ENCRYPTED DNS EXFILTRATION CAPTURED VIA WIRESHARK
#               BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)
# -------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0                                                                
# Details : Load required imports.
# Modified: N/A
# -------------------------------------------------------------------------------------

import os
import base64
from arc4 import ARC4		# see https://pypi.org/project/arc4/
from termcolor import colored	# pip install termcolor

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0                                                               
# Details : Display my universal header.    
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

os.system("clear")
print " ____  _____      _______  _______ ___ _   _____ ____      _  _____ ___  ____   "
print "|  _ \| ____|    | ____\ \/ /  ___|_ _| | |_   _|  _ \    / \|_   _/ _ \|  _ \  "
print "| | | |  _| _____|  _|  \  /| |_   | || |   | | | |_) |  / _ \ | || | | | |_) | "
print "| |_| | |__|_____| |___ /  \|  _|  | || |___| | |  _ <  / ___ \| || |_| |  _ <  "
print "|____/|_____|    |_____/_/\_\_|   |___|_____|_| |_| \_\/_/   \_\_| \___/|_| \_\ "
print "                                                                                "
print "             BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)              "
print "                                                                                "

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0                                                               
# Details : Define and populate program variables.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

domainname = "totallylegit.com"
filename = "secret.txt"
password = "TryHarder"
message = "0.0ejXWsr6TH-P_1xkEstaVwi7WDy8AcxufnGotWXH3ckb2Lh5A-qFljIWOAOLUS0.T1W8P4CpiCZbCM7_QKcv-r0JG29RpsyYY5YkZRxo7YDIYUJpHlGgxu5PWV1G_DA.KNrmnrktfbeDgzcpPJBjPTeMYx3Qs1Q6bAuFhROWXemJ80gPTYIz0xl8usJQN3m.w.totallylegit.com"

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0                                                               
# Details : Display the above data to the user.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

print "Known Domain  : " + domainname
print "Known Filename: " + filename
print "Known Password: " + password
print "Known Message : \n"
print colored(message,'green')

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0                                                               
# Details : Process the data.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

print "\nDecoding message...\n"

print "Processing - Removing known domain name...."
message = message[0:-len(domainname)]

print "Processing - Making remaining string base64 complient..."
chunkNumber, chunkData = message.split('.', 1)
chunkNumber = int(chunkNumber)  # We have only one chunk with index 0
dataChunks = []
dataChunks.append(chunkData.replace(".", ""))
filedata = ''.join(dataChunks)
filedata = filedata.replace("_", "/").replace("-", "+")
filedata += "=" * ((4 - len(filedata) % 4) % 4)
filedata = bytearray(filedata, 'utf-8')

print "Processing - Undertaking base64 decode..."
filedata = base64.urlsafe_b64decode(filedata)

print "Processing - Undertaking RC4 decode..."
arc4 = ARC4(password)
filedata = arc4.decrypt(filedata)

print "Processing - Saving data to zipfile..."
with open("./secret.zip", 'w') as fileHandle:
    fileHandle.write(filedata)
fileHandle.close()

print "Processing - Opening zip file and reading data..."
os.system("unzip secret.zip > F1.txt")
readline = open(filename).readline().rstrip()

print "Processing - Tidying up system files...\n"
os.system("rm F1.txt")
os.system("rm secret.zip")
os.system("rm secret.txt")

text = str(readline)
print colored(text,'green')





