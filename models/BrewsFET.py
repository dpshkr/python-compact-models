# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 17:24:22 2023

@author: Pushkar
"""

import numpy as np

class BrewsFET:
    def __init__(self, parameters={}):
        self.__T = 295
        if "T" in parameters:
            self.__T = parameters["T"]
        self.__tins = 10e-9
        if  "tins" in parameters:
            self.__tins = parameters["tins"]*1e-9
        self.__kins = 5.0
        if "kins" in parameters:
            self.__kins = parameters["kins"]
        self.__Ndop = 1e23
        if "Ndop" in parameters:
            self.__Ndop = parameters["Ndop"]*1e6
        
        print(self.__T)
    
    def apply_bias(self, VG, VD):
        pass


parameters = {
    "T" : 297,
    "tins" : 10,
    "kins" : 5.0,
    "Ndop" : 1e17
    }

m = BrewsFET(parameters=parameters)