# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:20:13 2020

@author: jaff_
"""
#### UNitest File
### 1 unit test file per function 
### name conventionn : test_funtion()
import BlackSholesModel as BS
import InputTest as IT
import BM  as BM
import datetime as date
import pandas as pd
import numpy as np
#data collection
class DataManager(object):
    '''data handler class
    import and export the data 
    
    flname: str
    input file with a list of trades
    trades: dataframe
    store the data provided by the trade.csv file
    '''
    
    def __init__(self, flname:str ):
        self.flname = flname
        self.trades = pd.read_csv(self.flname)
    
    
    #name of the input file
    
    
    #put a while no erro for the loop 
    # on the input. then test on them for error
    #then run report
    #data are ok for input
    #---run test on imported data
    
    
    def pv_surface_csv(self):
        '''export a csv file with all trade's PV surface  '''
        for ii in range(0,len(self.trades.index)):
            '''importing the data trade by trade'''            
            trades = pd.read_csv("trades.csv")
            option = trades.loc[ii,:] 
            diff_t = (date.datetime.strptime(option['OptionExpiry'], "%d/%m/%Y") - 
             date.datetime.strptime(option['ReportDate'], "%d/%m/%Y"))
            T = float(str(diff_t.days))/365
            S= option['MarketPrice']
            sigma= option['Volatility']
            K= option['Strike']
            PutCall = option['OptionType']
            am = option['ExpiryType']
            r= option['InterestRate']
            
            pv_surface = np.zeros((9,9 ))
            
            IT.InputTest(PutCall ,S,  K, T, r, sigma, am).typetest()
            
            IT.InputTest(PutCall ,S,  K, T, r, sigma, am).valuetest()

            '''the lader used in the table '''
            lader = (-0.12, -0.09, -0.06, -0.03, 0, 0.03, 0.06, 0.09, 0.12)
            '''cecking the type of exercise of the option'''
            if am.lower() == "european": 
                for i in range(0, len(lader)):
                    new_sigma= sigma+lader[i]
                    for j in range(0, len(lader)):
                        new_S= S*(1+lader[j])
                        bsm =BS.BlackSholes(PutCall= PutCall ,S= new_S, K= K, T= T, r= r, sigma= new_sigma)
                        pv_surface[i, j]=bsm.value()
            else:
                for i in range(0, len(lader)):
                    new_sigma= sigma+lader[i]
                    for j in range(0, len(lader)):
                        new_S= S*(1+lader[j])
                        bsm =BM.BinomialModel(PutCall= PutCall ,S= new_S, K= K, T= T, r= r, sigma= new_sigma, AmOpt= True)
                        pv_surface[i, j]=bsm.value()
            my_df= pd.DataFrame(pv_surface)
            #Column name
            header_to_add = ['P0 - 12%','P0 - 9%','P0 - 6%','P0 - 3%','P0','P0 + 3%','P0 + 6%','P0 + 9%','P0 + 12%']
            # index_to_add = pd.DataFrame['V0 - 12%','V0 - 9%','V0 - 6%','V0 - 3%','V0','V0 + 3%','V0 + 6%','V0 + 9%','V0 + 12%']
            # my_df.rename(index = index_to_add )
            my_df.to_csv( am +'_'+ PutCall +'_'+ 'pv_surface.csv', index = True,  header=header_to_add)
        return print(' pv_surface export completed')

    def sensi_csv(self):
        '''export a csv file with all trades' sensi'''
        sensi = np.zeros((len(self.trades.index),11), dtype = object) #add self later
        for ii in range(0,len(self.trades.index)):
            '''importing the data trade by trade'''
            
            option = self.trades.loc[ii,:] 
            diff_t = (date.datetime.strptime(option['OptionExpiry'], "%d/%m/%Y") - 
             date.datetime.strptime(option['ReportDate'], "%d/%m/%Y"))
            T = float(str(diff_t.days))/365
            S= option['MarketPrice']
            sigma= option['Volatility']
            K= option['Strike']
            PutCall = option['OptionType']
            am = option['ExpiryType']
            r= option['InterestRate']
            #call function check
            
            IT.InputTest(PutCall ,S,  K, T, r, sigma, am).typetest()
            
            IT.InputTest(PutCall ,S,  K, T, r, sigma, am).valuetest()

            '''cecking the type of exercise of the option'''
            if am.lower() == "european":
                val = BS.BlackSholes(PutCall= PutCall ,S= S, K= K, T= T, r= r, sigma= sigma)
            else:
                val = BM.BinomialModel(PutCall= PutCall ,S= S, K= K, T= T, r= r, sigma= sigma, AmOpt= True)
            sensi[ii,0]= PutCall +"_"+ am   #Type
            sensi[ii,1]= T                  #Time To Maturity in Y
            sensi[ii,2]= S                  #Price of the underlying
            sensi[ii,3]= sigma              #Volatility
            sensi[ii,4]= r                  #interest Rate
            sensi[ii,5]= val.value()        #value of the option
            sensi[ii,6]= val.delta()        #Delta
            sensi[ii,7]= val.gamma()        #Gamma
            sensi[ii,8]= val.theta()        #Theta
            sensi[ii,9]= val.vega()         #vega            
            sensi[ii,10]= val.rho()         #Rho
        my_df= pd.DataFrame(sensi)
        #Column name
        header_to_add = ['Type','Time to Maturity (Years)','Price','Volatility','Interest Rate','Value','Delta','Gamma','Theta','Vega','Rho']
        my_df.to_csv( 'sensi.csv', index = True,  header=header_to_add)
        return print(' sensi csv export completed')         


