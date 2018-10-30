
#-*-coding:utf-8-*-
# ---- dsiervo@sgc.gov.co -------
# script para obtener el municipio mas cercano a un sismo
import pandas as pd
import numpy as np


def euc_dist(x, point):
    a_min_b = np.asarray([x["lat"],x["lon"]])-np.asarray(point)
    dist = np.sqrt(np.einsum('i,i', a_min_b, a_min_b))
    return dist


def find_region(point):
    """
    :type point: List of floats
    :param point: coordinates of the point at which 
                  the distance will be calculated
                
                point = [lat,lon]
    """
    names=["ID", "lat", "lon", "municipio","departamento"]
    df = pd.read_csv("municipios.txt", sep=r'\s{2,}', names=names,
                     index_col=0, header=None)

    df["lat"] = pd.to_numeric(df["lat"])
    df["lon"] = pd.to_numeric(df["lon"])

    df["distance"] = df.apply(lambda x: euc_dist(x, point), axis=1)
    df.sort_values("distance", inplace=True, ascending=True)
    return df.municipio.values[0]+" - "+df.departamento.values[0]

