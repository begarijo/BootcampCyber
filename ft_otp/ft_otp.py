# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_otp.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: begarijo <begarijo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/26 12:39:00 by begarijo          #+#    #+#              #
#    Updated: 2023/05/01 10:26:43 by begarijo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import  argparse, os, hashlib, hmac, time, struct, pyotp, base64
from cryptography.fernet import Fernet

KEY = '.THE_KEY.key'

def arguments():
	arg = argparse.ArgumentParser()
	group = arg.add_mutually_exclusive_group(required=True)
	group.add_argument("-g", help="Generate an encrypted key")
	group.add_argument("-k", help="Generate an OTP")
	group.add_argument("-d", help="Delete unnecessary files", action="store_true")
	return arg.parse_args()

def open_file(arg):
	try:
		with open(arg, 'rb') as file:
			return (file.read())
	except:
		print("File can't be opened")

def	valid_file(arg):
	with open(arg, 'r') as file:
		file = file.read()
		try:
			if len(file) == 64 and int(file, 16):
				return True
			print("Not the right format")
			return False
		except:
			print("File is not hexadecimal")

def	generate_fernet():
	try:
		if args.g:
			key_aux = Fernet.generate_key()
			with open(KEY, 'wb') as fer:
				fer.write(key_aux)
			f = Fernet(key_aux)
		elif args.k:
			with open(KEY, 'rb') as fer:
				f = Fernet(fer.read())
		return f
	except:
		print("Files removed")

def create_key(key_g):
	en_file = encrypt(key_g)
	with open('ft_otp.key', 'wb') as file:
		file.write(en_file)
	print("Key successfully saved!")
	return (en_file)

def encrypt(key_g):
	en_file = f.encrypt(key_g)
	return (en_file)

def decrypt(key_k):
	de_file = f.decrypt(key_k)
	return (de_file)

def create_otp(de_file):
	hash_key = gen_hmac(de_file)
	otp = gen_otp(hash_key)
	return (otp)

def	gen_hmac(de_file):
	time_msg = int(time.time()//5)
	msg = struct.pack(">Q", time_msg)
	hash_key = hmac.digest(de_file, msg, hashlib.sha1)
	return (hash_key)

def gen_otp(hash_key):
	offset = hash_key[19] & 0xf
	bin_code = (hash_key[offset] & 0x7f) << 24 | (hash_key[offset + 1] & 0xff) << 16 | (hash_key[offset + 2] & 0xff) << 8 | (hash_key[offset + 3] & 0xff)
	return (bin_code % 1000000)

# Check if the TOTP is the right one
# def	check_otp(de_file):
# 	totp = pyotp.TOTP(base64.b32encode(de_file), interval=5)
# 	good = totp.now()
# 	return (good)

if (__name__=='__main__'):
	args = arguments()
	global f

	f = generate_fernet()
	if args.g:
		if valid_file(args.g):
			try:
				create_key(open_file(args.g))
			except:
				print("Error: key could not be encrypted.")
	elif (args.k):
		try:
			de_file = decrypt(open_file(args.k))
			otp = create_otp(de_file)
			print(otp)
			# totp = check_otp(de_file)
			# print(totp)
		except:
			print("Error: OTP could not be gerated.")
	elif args.d:
		if os.path.isfile('ft_otp.key'):
			os.remove('ft_otp.key')
		if os.path.isfile('.THE_KEY.key'):
			os.remove('.THE_KEY.key')
