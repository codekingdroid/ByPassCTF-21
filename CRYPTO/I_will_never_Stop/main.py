import hashlib, os, random, string, random

flag = "******************REDACTED*******************"

def random_strings(num):
	return ''.join(random.choices(string.ascii_uppercase +string.digits, k = num))

random.seed(1337)
order = 0
for chars in flag:
	zip_name = random_strings(random.randint(1,10))
	os.system(f"mkdir {zip_name}")
	md5_encode = hashlib.md5(chars.encode())
	flag_hash = md5_encode.hexdigest()
	md5_encode = hashlib.md5(zip_name.encode())
	zip_pass = md5_encode.hexdigest()
	length = 0 
	while length < 32 :
		print(length)
		os.system(f'cd {zip_name}; touch {length//2}.{flag_hash[length:length+2]}')
		os.system(f'cd {zip_name}; touch {length//2}.{random_strings(random.randint(4,6))}')
		length +=2
	os.system(f"cd {zip_name}; zip -P {zip_pass} {order}.{zip_name}.zip *; mv *.zip ../ ; cd ../ ; rm -r {zip_name}")
	order +=1

