import numpy as np
import scipy.constants as cnsts
from scipy.optimize import brentq

class DGFET:
    def __init__(self, parameters={}):
        self.__T = 295
        if "T" in parameters:
            self.__T = parameters["T"]
        self.__kins = 5.0 * cnsts.epsilon_0
        if "kins" in parameters:
            self.__kins = parameters["kins"] * cnsts.epsilon_0
        self.__ksc = 12 * cnsts.epsilon_0
        if "ksc" in parameters:
            self.__ksc = parameters["ksc"] * cnsts.epsilon_0
        self.__tins = 10e-9
        if  "tins" in parameters:
            self.__tins = parameters["tins"]*1e-9
        self.__tsc = 10e-9
        if "tsc" in parameters:
            self.__tsc = parameters["tsc"]*10e-9
        self.__ni = 1.5e16
        if "ni" in parameters:
            self.__ni = parameters["ni"]*1e6
        self.__L = 1e-6
        if "L" in parameters:
            self.__L = parameters["L"]*1e-6
        self.__Vfb = 0.0
        if "Vfb" in parameters:
            self.__Vfb = parameters["Vfb"]
        self.__mu = 0.01
        if "mu" in parameters:
            self.__mu = parameters["mu"]*1e-4
        
        self.__LB = np.sqrt((2*self.__ksc*cnsts.k*self.__T)/\
                            (cnsts.e*cnsts.e*self.__ni))
        
        #print(self.__LB)
    
    def setup_poisson(self,beta, VG, V):
        lhs = ((cnsts.e*(VG-self.__Vfb-V))/(2*cnsts.k*self.__T)) -\
            np.log(2*self.__LB/self.__tsc)
        
        rhs = np.log(beta) - np.log(np.cos(beta)) +\
            ((2*self.__ksc*self.__tins) / (self.__kins*self.__tsc))*\
                beta*np.tan(beta)
        
        return (lhs - rhs)
    
    def solve_poisson(self, VG, V):
        beta = brentq(self.setup_poisson, np.nextafter(0, 1),1.5, args=(VG, V))
        return beta
    
    def apply_bias(self, VG, VD):
        bs = self.solve_poisson(VG, 0)
        bd = self.solve_poisson(VG, VD)
        k = (self.__mu*4*self.__ksc*(2*cnsts.k*self.__T)**2) / \
            (self.__L*self.__tsc*cnsts.e*cnsts.e)
        k1 = (self.__ksc*self.__tins) / (self.__kins*self.__tsc)
        
        ks = bs*np.tan(bs) - ((bs**2)/2) + (k1*(bs**2)*(np.tan(bs))**2)
        kd = bd*np.tan(bd) - ((bd**2)/2) + (k1*(bd**2)*(np.tan(bd))**2)
        
        return k*(ks - kd)

parameters = {
    "T" : 297,
    "tins" : 10,
    "kins" : 5.0,
    "Ndop" : 1e17
    }

m = DGFET(parameters=parameters)
VG = 4
VD = 1
#print(m.setup_poisson(1e-5, VG, V))

ID = m.apply_bias(VG,VD)

print(ID)
