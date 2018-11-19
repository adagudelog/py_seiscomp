#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Realiza el envío de correos masivos con información obtenida de un archivo .CSV
v(1) 2018-07-26
autor: Daniel Siervo, Miguel Lizarazo
e-mail: dsiervo@sgc.gov.co, mlizarazo@sgc.gov.co
"""
from correo import correo
from crea_pdf import make_pdf

# "Invitaciones3dias.csv"
dest = open("destinatarios_prueba.csv").readlines()

def tilde_replace(a):
	return a.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ñ", "n").replace("Ñ", "N").replace("Á", "A").replace("É","E").replace("Í", "I").replace("Ó", "O").replace("Ú", "U")


for i in range(1,len(dest)):
	nombre = dest[i].split(",")[0].strip()+" "+dest[i].split(",")[1].strip()
	filiacion = dest[i].split(",")[2].strip()
	mail = dest[i].split(",")[3].strip("\n").strip()
	nombre_doc = tilde_replace(nombre)



	#send = raw_input("Enviar correo a: %s, %s, %s?"%(nombre, filiacion, mail))

	print nombre
	carta = make_pdf(nombre_doc, filiacion)
	print carta
	correo(mail, nombre, filiacion, carta)
