# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 15:53:07 2020

@author: jaff_
"""
import unittest 
import BlackSholesModel as BS

class TestBlackSholes(unittest.TestCase):


    
    def test_value(self):
        T1, T2, T3  = 10**-15, 1, 10
        S1, S2, S3= 1, 10**-15, 10
        sigma1, sigma2, sigma3= 1, 10**-15, 10
        K1, K2, K3= 1, 10**-15, 10
        PutCall1, PutCall2, PutCall3 = 'put', 'call', 'call'
        r1, r2, r3= 1, 0.0005, 10

        totest=  BS.BlackSholes(PutCall= PutCall1 ,S= S1, K= K1, 
                                T= T1, r= r1, sigma= sigma1)
        self.assertAlmostEqual(totest.value(), 1.2615662126069793e-08)
        
        totest=  BS.BlackSholes(PutCall= PutCall2 ,S= S2, K= K2, 
                                T= T2, r= r2, sigma= sigma2)
        self.assertAlmostEqual(totest.value(), 1e-15)

        totest=  BS.BlackSholes(PutCall= PutCall3 ,S= S3, K= K3, 
                                T= T3, r= r3, sigma= sigma3)
        self.assertAlmostEqual(totest.value(), 10)
    def test_delta(self):
        T1, T2, T3  = 10**-15, 1, 10
        S1, S2, S3= 1, 10**-15, 10
        sigma1, sigma2, sigma3= 1, 10**-15, 10
        K1, K2, K3= 1, 10**-15, 10
        PutCall1, PutCall2, PutCall3 = 'put', 'call', 'call'
        r1, r2, r3= 1, 0.0005, 10

        totest=  BS.BlackSholes(PutCall= PutCall1 ,S= S1, K= K1, 
                                T= T1, r= r1, sigma= sigma1)
        self.assertAlmostEqual(totest.delta(), -0.499999981)
        
        totest=  BS.BlackSholes(PutCall= PutCall2 ,S= S2, K= K2, 
                                T= T2, r= r2, sigma= sigma2)
        self.assertAlmostEqual(totest.delta(), 0)

        totest=  BS.BlackSholes(PutCall= PutCall3 ,S= S3, K= K3, 
                                T= T3, r= r3, sigma= sigma3)
        self.assertAlmostEqual(totest.delta(), 0)

    def test_gamma(self):
        T1, T2, T3  = 10**-15, 1, 10
        S1, S2, S3= 1, 10**-15, 10
        sigma1, sigma2, sigma3= 1, 10**-15, 10
        K1, K2, K3= 1, 10**-15, 10
        PutCall1, PutCall2, PutCall3 = 'put', 'call', 'call'
        r1, r2, r3= 1, 0.0005, 10

        totest=  BS.BlackSholes(PutCall= PutCall1 ,S= S1, K= K1, 
                                T= T1, r= r1, sigma= sigma1)
        self.assertAlmostEqual(totest.gamma(), 12615662.610100787)
        
        totest=  BS.BlackSholes(PutCall= PutCall2 ,S= S2, K= K2, 
                                T= T2, r= r2, sigma= sigma2)
        self.assertAlmostEqual(totest.gamma(), 0)

        totest=  BS.BlackSholes(PutCall= PutCall3 ,S= S3, K= K3, 
                                T= T3, r= r3, sigma= sigma3)
        self.assertAlmostEqual(totest.gamma(), 0)
        
    def test_theta(self):
        T1, T2, T3  = 10**-15, 1, 10
        S1, S2, S3= 1, 10**-15, 10
        sigma1, sigma2, sigma3= 1, 10**-15, 10
        K1, K2, K3= 1, 10**-15, 10
        PutCall1, PutCall2, PutCall3 = 'put', 'call', 'call'
        r1, r2, r3= 1, 0.0005, 10
        totest=  BS.BlackSholes(PutCall= PutCall1 ,S= S1, K= K1, 
                                T= T1, r= r1, sigma= sigma1)
        self.assertAlmostEqual(totest.theta(), -6307830.8050504)
        
        totest=  BS.BlackSholes(PutCall= PutCall2 ,S= S2, K= K2, 
                                T= T2, r= r2, sigma= sigma2)
        self.assertAlmostEqual(totest.theta(), 0)

        totest=  BS.BlackSholes(PutCall= PutCall3 ,S= S3, K= K3, 
                                T= T3, r= r3, sigma= sigma3)
        self.assertAlmostEqual(totest.theta(), 0)

    def test_rho(self):
        T1, T2, T3  = 10**-15, 1, 10
        S1, S2, S3= 1, 10**-15, 10
        sigma1, sigma2, sigma3= 1, 10**-15, 10
        K1, K2, K3= 1, 10**-15, 10
        PutCall1, PutCall2, PutCall3 = 'put', 'call', 'call'
        r1, r2, r3= 1, 0.0005, 10

        totest=  BS.BlackSholes(PutCall= PutCall1 ,S= S1, K= K1, 
                                T= T1, r= r1, sigma= sigma1)
        self.assertAlmostEqual(totest.rho(), 0)
        
        totest=  BS.BlackSholes(PutCall= PutCall2 ,S= S2, K= K2, 
                                T= T2, r= r2, sigma= sigma2)
        self.assertAlmostEqual(totest.rho(), 0)

        totest=  BS.BlackSholes(PutCall= PutCall3 ,S= S3, K= K3, 
                                T= T3, r= r3, sigma= sigma3)
        self.assertAlmostEqual(totest.rho(), 0)

    def test_vega(self):
        T1, T2, T3  = 10**-15, 1, 10
        S1, S2, S3= 1, 10**-15, 10
        sigma1, sigma2, sigma3= 1, 10**-15, 10
        K1, K2, K3= 1, 10**-15, 10
        PutCall1, PutCall2, PutCall3 = 'put', 'call', 'call'
        r1, r2, r3= 1, 0.0005, 10

        totest=  BS.BlackSholes(PutCall= PutCall1 ,S= S1, K= K1, 
                                T= T1, r= r1, sigma= sigma1)
        self.assertAlmostEqual(totest.vega(), 1.2615662610100787e-08)
        
        totest=  BS.BlackSholes(PutCall= PutCall2 ,S= S2, K= K2, 
                                T= T2, r= r2, sigma= sigma2)
        self.assertAlmostEqual(totest.vega(), 0)

        totest=  BS.BlackSholes(PutCall= PutCall3 ,S= S3, K= K3, 
                                T= T3, r= r3, sigma= sigma3)
        self.assertAlmostEqual(totest.vega(), 0)

if __name__== '__main__':unittest.main() 

   
        
        