#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Función que realiza el envío de correos con información obtenida de redes internacionales (NEIC, GEOFON)
v(1) 2016-05-21
autor: Daniel Siervo
e-mail: dsiervo@sgc.gov.co
"""
import smtplib
#from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from os import system
import sys
##import time

def correo(mail_destinatario, nombre_destinatario, entidad, carta):

	print mail_destinatario, nombre_destinatario, entidad

	#lee datos del remitente
	datosr=open('.remitente.txt','r').readlines()

	#Prepara correos electrónicos con información del sismo.boletin
	print 'Preparando correo...'
	remitente = datosr[0] 
	passw= datosr[1]
	destinatario = mail_destinatario
	asunto = "Respuesta asistentes “Primer foro internacional de redes sismológicas, \
	amenaza sísmica y gestión del riesgo de desastres”" 
	mensaje=open('mensaje.html').read()%(nombre_destinatario, entidad)

	print mensaje

	msg = MIMEMultipart()
	msg['Subject'] = asunto
	msg['From'] = "Servicio Geológico Colombiano"

	#Prepara destinatarios y adjunta imagen
	msg['To'] = destinatario
	pdf = file(carta).read()

	with open(carta, "rb") as opened:
	    openedfile = opened.read()
	attachedfile = MIMEApplication(openedfile, _subtype = "pdf")
	attachedfile.add_header('content-disposition', 'attachment',
		filename = "Invitacion_%s.pdf"%nombre_destinatario)
	msg.attach(attachedfile)

	msg.attach(MIMEText(mensaje, 'html'))

	server = smtplib.SMTP('smtp.gmail.com:587') 
	server.starttls()
	server.login(remitente,passw)

	server.sendmail(remitente, destinatario, msg.as_string())

	server.quit()
	print "Correo enviado."

if __name__ == '__main__':

	correo("dsiervo@sgc.gov.co", "Don Daniel", "SGC", "carta.pdf")
