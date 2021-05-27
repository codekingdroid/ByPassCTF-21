import time ,random

flag = "***********REDACTED***********"

seed = int(str(time.time()))
random.seed(seed)
encrypt = ''.join([chr(ord(char) ^ random.randint(0,10000)) for char in flag ])

file  = open("enc_flag",'w')
file.write(encrypt)

