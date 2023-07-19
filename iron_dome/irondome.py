# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    irondome.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: begarijo <begarijo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/30 13:17:22 by begarijo          #+#    #+#              #
#    Updated: 2023/06/08 17:18:39 by begarijo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import psutil, os, daemon, argparse, time, logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def arguments():
	arg = argparse.ArgumentParser("Iron Dome: Detects anomalous activity by monitoring different OS parameters.")
	arg.add_argument("args", nargs="+")
	return arg.parse_args()

def	mem_use():
    print("Esa memoria wena")

def	entrop_changes(p, e, ent):
    p
    e
    ent
    print("La super entropia")

def	crypto_act():
    print("Encriptame esta")

def	disk_abuse(r_disk, w_disk):
    r_disk
    w_disk
    print("Abusadora, mata hombres")

def	monitor(p, e=None):
	logging.basicConfig(filename='/var/log/irondome/irondome.log', level=logging.INFO, format='%(arctime)s %(message)s')
	# Event handler y observer, class Event y tal
	entro_ini = {}
	r_disk_ini = psutil.disk_io_counters().read_count
	w_disk_ini = psutil.disk_io_counters().write_count
	# Como es en perpetuidad, necesita bucle infinito
	while True:
		try:
			# timer = time.time()
			# Aquí necesito comprobación del tiempo, para meterlo en el bucle y que el uso de memoria no sea tanto?
			mem_use()
			entro_ini = entrop_changes(p, e, entro_ini)
			crypto_act()
			r_disk_ini, w_disk_ini = disk_abuse(r_disk_ini, w_disk_ini)
		except:
			print("upsi")

def	iron_dome():
	if len(args) > 0:
		with daemon.DaemonContext():
			if os.path.exists(p) and e:
				monitor(p, e)
			elif os.path.exists(p) and not e:
				monitor(p)
	else:
		print("ERROR: The program requires an existen path.")

if __name__=='__main__':
	global p, e
	args = arguments()
	p = args.p
	e = args.e
	if os.getuid() == 0:
		iron_dome()
	else:
		print("ERROR: This program must be launched as root.")