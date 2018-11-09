 -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  save_earthworm_data.py
#   Purpose:   Read and save data from earthworm
#   Author:    Juan Santiago Velasquez
#   Email:     js.velasquez123@gmail.com
#   License:   GNU Lesser General Public License, Version 3
#
# -------------------------------------------------------------------

from obspy import UTCDateTime
from obspy.clients.earthworm import Client
from datetime import date, datetime, timedelta
import numpy as np
import os

# ----------- Funcion para crear lista de fechas desde start hasta end cada delta --------------
def perdelta(start, end, delta):
	curr = start
	while curr <= end:
		yield curr
		curr += delta


# MAIN


client = Client("10.100.100.229", 21666)
response = client.get_availability('CM')

#response = response[:5]
print("\n\n")
cont1 = 0
with open("log_file", "w") as log_file, open("log_error", "w") as error_file:
	for el in response:
		net = el[0]
		sta = el[1]
		loc = el[2]
		cha = el[3]
		t1 = el[4]
		t2 = el[5]
		d1 = t1.date
		d2 = t2.date
		cont1 += 1
		print("\n* %s.%s.%s.%s   Datos desde %s hasta %s  (%s/%s) \n \ " % (net, sta, loc, cha, d1, d2, cont1, len(response)))
		log_file.write("\n* %s.%s.%s.%s   Datos desde %s hasta %s\n \ \n" % (net, sta, loc, cha, d1, d2))
		"""	
                f = list(perdelta(d1, d2, timedelta(days=1)))
		cont2 = 0
		s = 0
		for d in f:
			t0 = UTCDateTime(d)
			tf = t0 + 86400.
			jday = t0.julday
			year = t0.year
			name_wf = "%s.%s.%s.%s.D.%s.%03d" % (net, sta, loc, cha, year, jday)
			path = os.path.join(str(year), net, sta, "%s.D" % cha) ## Ruta donde se guarda
			if not os.path.exists(path):
				os.makedirs(path)
			try:
				#st = client.get_waveforms(net,sta,loc,cha,t0,tf)
				#st.write(os.path.join(path, name_wf), format='MSEED')
				client.save_waveforms(os.path.join(path, name_wf), net, sta, loc, cha, t0, tf, format='MSEED')
				s = os.path.getsize(os.path.join(path, name_wf))
			except Exception as e:
				print(e)
				error_file.write("\nError en: %s\n%s\n" % (os.path.join(path, name_wf), e))
			
			cont2 += 1
			print(" |-- %s   (%d/%d)  %s bytes" % (d, cont2, len(f), s))
			log_file.write(" |-- %s   (%d/%d)  %s bytes\n" % (d, cont2, len(f), s))

 
		"""
