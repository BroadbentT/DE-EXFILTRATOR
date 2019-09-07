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
# Details : Populate program with known variables extracted from wireshark analysis.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

domain   = ""
filename = ""
password = ""
message  = ""

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0                                                               
# Details : Display the above data to the user.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

print "Known Domain  : ",
print colored(domain,'yellow')
print "Known Filename: ",
print colored(filename,'yellow')
print "Known Password: ",
print colored(password,'yellow')
print "Known Message : \n"
print colored(message,'blue')

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0                                                               
# Details : Process the data.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

print "\nDecoding message..."

print "Processing - Removing known domain name...."
message = message[0:-len(domain)]

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
print colored(text,'red') + "\n"





