#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 08:10:55 2021

@author: leo
"""

import pandas as pd
import numpy as np

import datetime 


#lat = np.degrees(23.45)

def sol(lat, lon): 
    
    lon0 = float(lon)
    
    lat0 = float(lat)
    lat0 = np.degrees(lat0)
    phi = np.degrees(23.45)
    grados = np.arcsin(lat0/phi)
    grados = np.rad2deg(grados)
    nj = (365/360)*grados - 284
    dia = nj + 365
    
    dia2 = 172 - (nj+365) + 172
    
    f0 = (360/364)*((dia)-81)
    f = np.deg2rad(f0)
    
    ET = 9.87*np.sin(2*f) - 7.53**np.cos(f) - 1.5**np.sin(f)
    
    omega = -90.00
    
    TC = 12.00 - (1/60)*(ET) - (1/15)*(lon0 - omega) + 1
    
    fmt = '%Y%j'
    
    datestd1 = datetime.datetime.strptime('2021' + str(int(dia)), fmt).date()
    
    datestd2 = datetime.datetime.strptime('2021' + str(int(dia2)), fmt).date()
    
    hours = int(TC)
    minutes = (TC*60) % 60
    seconds = (TC*3600) % 60
    
    horacivil = "%d:%02d.%02d" % (hours, minutes, seconds)

        
    print(dia,dia2,TC, datestd1, datestd2, horacivil)
    
    return

lat = "22.771667"

lon = "-102.560556"

sol(lat, lon)

