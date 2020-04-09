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
        TBS = TestBlackSholes

        totest=  BS.BlackSholes(PutCall= TBS.PutCall1 ,S= TBS.S1, K= TBS.K1, 
                                T= TBS.T1, r= TBS.r1, sigma= TBS.sigma1)
        self.assertAlmostEqual(totest.value(), 1.2615662126069793e-08)
        
        totest=  BS.BlackSholes(PutCall= TBS.PutCall2 ,S= TBS.S2, K= TBS.K2, 
                                T= TBS.T2, r= TBS.r2, sigma= TBS.sigma2)
        self.assertAlmostEqual(totest.value(), 1e-15)

        totest=  BS.BlackSholes(PutCall= TBS.PutCall3 ,S= TBS.S3, K= TBS.K3, 
                                T= TBS.T3, r= TBS.r3, sigma= TBS.sigma3)
        self.assertAlmostEqual(totest.value(), 10)
        
    def test_delta(self):
        TBS = TestBlackSholes

        totest=  BS.BlackSholes(PutCall= TBS.PutCall1 ,S= TBS.S1, K= TBS.K1, 
                                T= TBS.T1, r= TBS.r1, sigma= TBS.sigma1)
        self.assertAlmostEqual(totest.delta(), -0.499999981)
        
        totest=  BS.BlackSholes(PutCall= TBS.PutCall2 ,S= TBS.S2, K= TBS.K2, 
                                T= TBS.T2, r= TBS.r2, sigma= TBS.sigma2)
        self.assertAlmostEqual(totest.delta(), 0)

        totest=  BS.BlackSholes(PutCall= TBS.PutCall3 ,S= TBS.S3, K= TBS.K3, 
                                T= TBS.T3, r= TBS.r3, sigma= TBS.sigma3)
        self.assertAlmostEqual(totest.delta(), 0)

    def test_gamma(self):
        TBS = TestBlackSholes

        totest=  BS.BlackSholes(PutCall= TBS.PutCall1 ,S= TBS.S1, K= TBS.K1, 
                                T= TBS.T1, r= TBS.r1, sigma= TBS.sigma1)
        self.assertAlmostEqual(totest.gamma(), 12615662.610100787)
        
        totest=  BS.BlackSholes(PutCall= TBS.PutCall2 ,S= TBS.S2, K= TBS.K2, 
                                T= TBS.T2, r= TBS.r2, sigma= TBS.sigma2)
        self.assertAlmostEqual(totest.gamma(), 0)

        totest=  BS.BlackSholes(PutCall= TBS.PutCall3 ,S= TBS.S3, K= TBS.K3, 
                                T= TBS.T3, r= TBS.r3, sigma= TBS.sigma3)
        self.assertAlmostEqual(totest.gamma(), 0)
        
    def test_theta(self):
        TBS = TestBlackSholes
        
        totest=  BS.BlackSholes(PutCall= TBS.PutCall1 ,S= TBS.S1, K= TBS.K1, 
                                T= TBS.T1, r= TBS.r1, sigma= TBS.sigma1)
        self.assertAlmostEqual(totest.theta(), -6307830.8050504)
        
        totest=  BS.BlackSholes(PutCall= TBS.PutCall2 ,S= TBS.S2, K= TBS.K2, 
                                T= TBS.T2, r= TBS.r2, sigma= TBS.sigma2)
        self.assertAlmostEqual(totest.theta(), 0)

        totest=  BS.BlackSholes(PutCall= TBS.PutCall3 ,S= TBS.S3, K= TBS.K3, 
                                T= TBS.T3, r= TBS.r3, sigma= TBS.sigma3)
        self.assertAlmostEqual(totest.theta(), 0)

    def test_rho(self):
        TBS = TestBlackSholes

        totest=  BS.BlackSholes(PutCall= TBS.PutCall1 ,S= TBS.S1, K= TBS.K1, 
                                T= TBS.T1, r= TBS.r1, sigma= TBS.sigma1)
        self.assertAlmostEqual(totest.rho(), 0)
        
        totest=  BS.BlackSholes(PutCall= TBS.PutCall2 ,S= TBS.S2, K= TBS.K2, 
                                T= TBS.T2, r= TBS.r2, sigma= TBS.sigma2)
        self.assertAlmostEqual(totest.rho(), 0)

        totest=  BS.BlackSholes(PutCall= TBS.PutCall3 ,S= TBS.S3, K= TBS.K3, 
                                T= TBS.T3, r= TBS.r3, sigma= TBS.sigma3)
        self.assertAlmostEqual(totest.rho(), 0)

    def test_vega(self):
        TBS = TestBlackSholes

        totest=  BS.BlackSholes(PutCall= TBS.PutCall1 ,S= TBS.S1, K= TBS.K1, 
                                T= TBS.T1, r= TBS.r1, sigma= TBS.sigma1)
        self.assertAlmostEqual(totest.vega(), 1.2615662610100787e-08)
        
        totest=  BS.BlackSholes(PutCall= TBS.PutCall2 ,S= TBS.S2, K= TBS.K2, 
                                T= TBS.T2, r= TBS.r2, sigma= TBS.sigma2)
        self.assertAlmostEqual(totest.vega(), 0)

        totest=  BS.BlackSholes(PutCall= TBS.PutCall3 ,S= TBS.S3, K= TBS.K3, 
                                T= TBS.T3, r= TBS.r3, sigma= TBS.sigma3)
        self.assertAlmostEqual(totest.vega(), 0)

if __name__== '__main__':unittest.main() 
