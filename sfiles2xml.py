#-*-coding:utf-8-*-
# ---- dsiervo@sgc.gov.co -------

from obspy import UTCDateTime
from obspy.core.event import read_events
from obspy.core.event import Catalog
from obspy.core.event.event import EventDescription
from obspy.core.event.origin import OriginQuality
import os
import pandas as pd
#import clicks
from Region_distance import find_region
import sys

def get_loc_cha(station, sta):
    """ Devuelve el codigo de localización, el canal y la red de una
    estación dada. Los datos se toman del dataframe de pandas 
    alimentado por el fichero statios.csv
    
    :type station: str
    :param station: Nombre de la estación
    :type sta: Pandas Dataframe
    :param: Dataframe de pandas con la información de las estaciones 
    que adquiere el SGC. 
    """
    
    loc_cod = 0
    net = ""
    
    columns = ["name", "net", "cod"]
    
    # quitando espacios antes y despues
    for col in columns:
        sta[col] = sta[col].apply(lambda x: x.strip())


    
    df_sta = sta[sta["name"]==station]
    
    # se prueba con los codigos de localizacion posibles priorizando
    # los banda ancha (00)
    codes = ["00", "20", "10", "40"]
    
    cha = {"00":"HHZ", "20":"EHZ", "10":"HNZ", "40":"HLZ", 0:""}
    
    "Si la estacion se encuentra en el data frame:"
    if not df_sta.empty:
        for cod in codes:
            loc_cod = df_sta[sta["cod"] == cod]["cod"].any()
            #print(loc_cod)
            if loc_cod != 0: break

        #print(station)
        net = df_sta["net"].values[0]
    
    return str(loc_cod), cha[loc_cod], net



def sfiles2xml(xml_name="cat.xml", folder="sfiles/"):

    cat = Catalog()

    sta = pd.read_csv("stations.csv", error_bad_lines=False,
	                   names=["net", "name", "lat", "lon", "z",
	                          "cod", "country"], header=None)
    
    sfiles = [i for i in os.listdir(folder) if os.path.isfile(os.path.join(folder,i))]
    for sfile in sfiles:
            #if sfile[10:13] == "L.S":
            print(sfile, len(cat))
            event = read_events(folder+sfile, format="NORDIC",
                                encoding='latin-1')
            
            # seleccionando el origen
            o = event.events[0].origins[0]
            
            o.creation_info.agency_id = "SGC"
            o.creation_info.author = "seisan@RSNC.dnl"
            o.creation_info.creation_time = UTCDateTime()
            phases = len(event.events[0].picks)
            o.used_phase_count = OriginQuality(used_phase_count=phases,
            	                               associated_phase_count=phases)

            region = find_region([o.latitude, o.longitude])
            print(region)
            event[0].event_descriptions[0] = EventDescription(text=region,
                                                           type="region name")

            for pick in event.events[0].picks:

                station = pick.waveform_id.station_code

                if station[:4] != "SPEC":
                    # asignando a cada picada el código de localización
                    # el canal y la red
                    loc, cha, net = get_loc_cha(station, sta)

                    pick.waveform_id.location_code = loc
                    pick.waveform_id.channel_code = cha
                    pick.waveform_id.network_code = net

            # agregando el evento al catalogo
            cat.append(event.events[0])
        # escribiendo el catalogo en formato xml SEISCOMP3
    cat.write(xml_name, format="SC3ML")

if __name__ == "__main__":
    sfiles2xml("30_enero_2017.xml")
