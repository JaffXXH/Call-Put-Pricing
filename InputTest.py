# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 17:45:11 2020

@author: jaff_
"""
class InputTest(Exception):
    '''Check if the input are of the type and the value expected 
    before performing the run'''
    def __init__(self, PutCall= None ,S= None,  K= None, T= None, r= None, sigma= None, am= None ):
        self.T = getattr(T, "tolist", lambda: T)()
        self.S= getattr(S, "tolist", lambda: S)()
        self.sigma=  getattr(sigma, "tolist", lambda: sigma)()
        self.K= getattr(K , "tolist", lambda: K)()
        self.PutCall = getattr(PutCall , "tolist", lambda: PutCall)()
        self.am =  getattr(am, "tolist", lambda: am)()
        self.r=  getattr(r, "tolist", lambda: r)()
        self.scope_completed = {"T":self.T, "S":self.S, "sigma":self.sigma, "K":self.K,"PutCall": self.PutCall, "am":self.am, "r":self.r}
        self.scope={}
        
        for yy in self.scope_completed.keys() :
            if self.scope_completed[yy] != None:
                self.scope[yy]= self.scope_completed[yy]
        if len (self.scope)==0:
            raise TypeError("No input provided") 
    
    def typetest(self):
        '''Testing if numerical variable have been assigned 
        matching type values'''
        self.scope_raise={}
        ErrStr= ""
        '''the scope of numerical variable'''
        inf_fl = ["T", "S", "sigma", "K", "r"]
        for yy in self.scope.keys():
            if yy in  inf_fl and type(self.scope[yy])not in [int, float]:
                self.scope_raise[yy]= type(self.scope[yy])
        '''checking if a type mismatch was found'''
        ErrFlot= ""
        if len(self.scope_raise)> 0:
            ErrFlot=("wrong type {0} assigned to {1} float expected".format(list(self.scope_raise.values()), 
                                                                            list(self.scope_raise.keys()) ))
            
        str_list = ["PutCall", "am"]
        self.scope_raise={}
        for yy in self.scope.keys():
            if yy in  str_list and not isinstance(self.scope[yy], str) :
                self.scope_raise[yy]= type(self.scope[yy])
        if len(self.scope_raise)> 0:
              ErrStr= ("wrong type {0} assigned to {1} str expected".format(list(self.scope_raise.values()),
                                                                            list(self.scope_raise.keys()) ))
        if len(ErrFlot + ErrStr)>0:
            raise TypeError( ErrFlot +'\n' + ErrStr)
        # return print ( " Inputs type are as expected")

    def valuetest(self):
        self.scope_raise= {}
        ErrPos= ""
        ErrBin= ""
        pos_list = ["T", "S", "sigma", "K"]
        for yy in self.scope.keys():
            if yy in pos_list and  self.scope[yy]<=0 :
                self.scope_raise[yy]= (self.scope[yy])
        if len(self.scope_raise)> 0:
            ErrPos = ("wrong value " + str(list(self.scope_raise.values()))+" assigned to " +str(list(self.scope_raise.keys()))
                            +"positive numbers expected")
            
        self.scope_raise={}
        bin_list = ["PutCall", "am"]
        for yy in self.scope.keys():
            if yy in bin_list and  yy== "PutCall":
                while self.scope[yy].lower() not in ["put", "call"]:
                    self.scope_raise[yy]= ["put"or "call"]
            if yy in bin_list and  yy== "am":
                while self.scope[yy].lower() not in ["american", "european"]:
                    self.scope_raise[yy]= ['"american" or "european"']
        if len(self.scope_raise)> 0:
            ErrBin = ("wrong value   assigned to " +str(list(self.scope_raise.keys()))
                            +" expected" + str(list(self.scope_raise.values())))
        if len(ErrPos + ErrBin)>0:
            raise ArithmeticError ( ErrPos +"\n" + ErrBin)
        # return print( " Input values are as expected")
