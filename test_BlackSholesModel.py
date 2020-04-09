# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 15:53:07 2020

@author: jaff_
"""
import unittest 
import BlackSholesModel as BS

class TestBlackSholes(unittest.TestCase):
    T1, T2, T3  = 10**-15, 1, 10
    S1, S2, S3= 1, 10**-15, 10
    sigma1, sigma2, sigma3= 1, 10**-15, 10
    K1, K2, K3= 1, 10**-15, 10
    PutCall1, PutCall2, PutCall3 = 'put', 'call', 'call'
    r1, r2, r3= 1, 0.0005, 10

    
    def test_value(self):


        totest=  BS.BlackSholes(PutCall= TestBlackSholes.PutCall1 ,S= TestBlackSholes.S1, K= TestBlackSholes.K1, 
                                T= TestBlackSholes.T1, r= TestBlackSholes.r1, sigma= TestBlackSholes.sigma1)
        self.assertAlmostEqual(totest.value(), 1.2615662126069793e-08)
        
        totest=  BS.BlackSholes(PutCall= TestBlackSholes.PutCall2 ,S= TestBlackSholes.S2, K= TestBlackSholes.K2, 
                                T= TestBlackSholes.T2, r= TestBlackSholes.r2, sigma= TestBlackSholes.sigma2)
        self.assertAlmostEqual(totest.value(), 1e-15)

        totest=  BS.BlackSholes(PutCall= TestBlackSholes.PutCall3 ,S= TestBlackSholes.S3, K= TestBlackSholes.K3, 
                                T= TestBlackSholes.T3, r= TestBlackSholes.r3, sigma= TestBlackSholes.sigma3)
        self.assertAlmostEqual(totest.value(), 10)
        
    def test_delta(self):

        totest=  BS.BlackSholes(PutCall= TestBlackSholes.PutCall1 ,S= TestBlackSholes.S1, K= TestBlackSholes.K1, 
                                T= TestBlackSholes.T1, r= TestBlackSholes.r1, sigma= TestBlackSholes.sigma1)
        self.assertAlmostEqual(totest.delta(), -0.499999981)
        
        totest=  BS.BlackSholes(PutCall= TestBlackSholes.PutCall2 ,S= TestBlackSholes.S2, K= TestBlackSholes.K2, 
                                T= TestBlackSholes.T2, r= TestBlackSholes.r2, sigma= TestBlackSholes.sigma2)
        self.assertAlmostEqual(totest.delta(), 0)

        totest=  BS.BlackSholes(PutCall= TestBlackSholes.PutCall3 ,S= TestBlackSholes.S3, K= TestBlackSholes.K3, 
                                T= TestBlackSholes.T3, r= TestBlackSholes.r3, sigma= TestBlackSholes.sigma3)
        self.assertAlmostEqual(totest.delta(), 0)

    def test_gamma(self):

        totest=  BS.BlackSholes(PutCall= TestBlackSholes.PutCall1 ,S= TestBlackSholes.S1, K= TestBlackSholes.K1, 
                                T= TestBlackSholes.T1, r= TestBlackSholes.r1, sigma= TestBlackSholes.sigma1)
        self.assertAlmostEqual(totest.gamma(), 12615662.610100787)
        
        totest=  BS.BlackSholes(PutCall= TestBlackSholes.PutCall2 ,S= TestBlackSholes.S2, K= TestBlackSholes.K2, 
                                T= TestBlackSholes.T2, r= TestBlackSholes.r2, sigma= TestBlackSholes.sigma2)
        self.assertAlmostEqual(totest.gamma(), 0)

        totest=  BS.BlackSholes(PutCall= TestBlackSholes.PutCall3 ,S= TestBlackSholes.S3, K= TestBlackSholes.K3, 
                                T= TestBlackSholes.T3, r= TestBlackSholes.r3, sigma= TestBlackSholes.sigma3)
        self.assertAlmostEqual(totest.gamma(), 0)
        
    def test_theta(self):

        totest=  BS.BlackSholes(PutCall= TestBlackSholes.PutCall1 ,S= TestBlackSholes.S1, K= TestBlackSholes.K1, 
                                T= TestBlackSholes.T1, r= TestBlackSholes.r1, sigma= TestBlackSholes.sigma1)
        self.assertAlmostEqual(totest.theta(), -6307830.8050504)
        
        totest=  BS.BlackSholes(PutCall= TestBlackSholes.PutCall2 ,S= TestBlackSholes.S2, K= TestBlackSholes.K2, 
                                T= TestBlackSholes.T2, r= TestBlackSholes.r2, sigma= TestBlackSholes.sigma2)
        self.assertAlmostEqual(totest.theta(), 0)

        totest=  BS.BlackSholes(PutCall= TestBlackSholes.PutCall3 ,S= TestBlackSholes.S3, K= TestBlackSholes.K3, 
                                T= TestBlackSholes.T3, r= TestBlackSholes.r3, sigma= TestBlackSholes.sigma3)
        self.assertAlmostEqual(totest.theta(), 0)

    def test_rho(self):

        totest=  BS.BlackSholes(PutCall= TestBlackSholes.PutCall1 ,S= TestBlackSholes.S1, K= TestBlackSholes.K1, 
                                T= TestBlackSholes.T1, r= TestBlackSholes.r1, sigma= TestBlackSholes.sigma1)
        self.assertAlmostEqual(totest.rho(), 0)
        
        totest=  BS.BlackSholes(PutCall= TestBlackSholes.PutCall2 ,S= TestBlackSholes.S2, K= TestBlackSholes.K2, 
                                T= TestBlackSholes.T2, r= TestBlackSholes.r2, sigma= TestBlackSholes.sigma2)
        self.assertAlmostEqual(totest.rho(), 0)

        totest=  BS.BlackSholes(PutCall= TestBlackSholes.PutCall3 ,S= TestBlackSholes.S3, K= TestBlackSholes.K3, 
                                T= TestBlackSholes.T3, r= TestBlackSholes.r3, sigma= TestBlackSholes.sigma3)
        self.assertAlmostEqual(totest.rho(), 0)

    def test_vega(self):

        totest=  BS.BlackSholes(PutCall= TestBlackSholes.PutCall1 ,S= TestBlackSholes.S1, K= TestBlackSholes.K1, 
                                T= TestBlackSholes.T1, r= TestBlackSholes.r1, sigma= TestBlackSholes.sigma1)
        self.assertAlmostEqual(totest.vega(), 1.2615662610100787e-08)
        
        totest=  BS.BlackSholes(PutCall= TestBlackSholes.PutCall2 ,S= TestBlackSholes.S2, K= TestBlackSholes.K2, 
                                T= TestBlackSholes.T2, r= TestBlackSholes.r2, sigma= TestBlackSholes.sigma2)
        self.assertAlmostEqual(totest.vega(), 0)

        totest=  BS.BlackSholes(PutCall= TestBlackSholes.PutCall3 ,S= TestBlackSholes.S3, K= TestBlackSholes.K3, 
                                T= TestBlackSholes.T3, r= TestBlackSholes.r3, sigma= TestBlackSholes.sigma3)
        self.assertAlmostEqual(totest.vega(), 0)

if __name__== '__main__':unittest.main() 
