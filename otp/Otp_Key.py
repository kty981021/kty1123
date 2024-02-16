import random
import sys
import os
import pyotp
import datetime

i=0

li = [50,51,52,53,54,55,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]

choice = [random.choice(li) for i in range(31)]

while True:
    file = 'OtpKey.txt'
    if os.path.exists(file):
        break
    else:
        Txtsave = open('OtpKey.txt', 'w')

        while i in range(31):
            Txtsave.write(str(chr(choice[i])))
            i=i+1



f = open("OtpKey.txt", 'r')

OtpKey = f.readline()

totp = pyotp.TOTP(OtpKey)

now = datetime.datetime.now()

print('OTP Seriel Number : ' + OtpKey)
print("now otp: " + totp.now())


