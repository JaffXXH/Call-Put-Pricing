# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 09:11:53 2020

@author: jaff_
"""
import DataManager as DM
class main(object):
    '''main class where the process is ran'''
    def __init__(self, flname):
        self.flname = flname
    def run (self):
        DM.DataManager(self.flname).pv_surface_csv()
        DM.DataManager(self.flname).sensi_csv()
        return print (' main run completed')
    
if __name__== '__main__':main("trades.csv").run()
    

        