# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 09:10:05 2020

@author: jaff_
"""
from math import exp, log, sqrt
from scipy.stats import norm


#### make a class above as model

class BlackSholes(object):
    ''' Class European put option in the Black Scholes model.
    Attributes
    ==========
    PutCall: String
    the option type Either "Put" or "Call"
    S: float
    initial stock price
    K: float
    strike value
    T: float
    maturity (in year fractions)
    r: float
    risk free rate
    sigma: float
    volatility
    Methods
    =======
    value: float
    returns the present value of the option
    delta: float
    returns the delta of the option
    gamma: float
    returns the gamma of the option
    theta: float
    returns the theta of the option
    rho: float
    returns the rho of the option        
    vega: float
    returns the vega of the option
    '''
    def __init__(self,PutCall : str,  S: float, K: float, T: float, r: float, sigma: float):
        self.PutCall = PutCall.lower()
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.d1num = (log(self.S/self.K) + (self.r + 0.5 * self.sigma * self.sigma) * self.T)
        self.d1 = self.d1num / (self.sigma * sqrt(self.T))
        self.d2 = self.d1 - self.sigma * sqrt(self.T)
        if self.PutCall == "call":
            self.cp = 1
        elif self.PutCall == "put":
            self.cp = -1
        else: 
            raise ValueError("expected 'put' or 'call' as value for PutCall")
           
    
    def value(self):
        '''the option's value'''              
        value = self.cp*( self.S * norm.cdf(self.cp*self.d1) - self.K * exp(- self.r*self.T)* norm.cdf(-self.d2))
        return value
    
    def delta (self):
        '''price sensitivity to the underlying asset
        it's  the first derivative of the option price with respect 
        to the current value of the underlying.
        '''
        delta = self.cp*(norm.cdf(-self.d1))
        return delta
    
    def gamma (self):
        ''' Second order derivative with respect to change in the
        underlying spot price'''
        gamma = norm.pdf(self.d1) / (self.S * self.sigma * sqrt(self.T))
        return gamma

    def theta (self):
        '''price sensitivity to the time to maturity
        The rate of change in the value of the option per one day 
        decrease in the option time while other variables remain constant.
        '''
        theta = -(self.S * norm.pdf(self.d1) * self.sigma / (2 * sqrt(self.T))) - self.cp* (self.r * self.K * exp(-self.r * self.T) * norm.cdf(self.cp*self.d2))
        return theta

    def rho (self):
        '''price sensitivity to the interest rate
        The rate of change in the value of the option 
        per 1% change in the risk-free rate while other variables remain constant
        '''
        rho = (self.cp*self.T * self.K * exp(-self.r*self.T) * norm.cdf(self.cp*self.d2))
        return rho
    
    def vega(self):
        '''price sensitivity to the volatility
        The rate of change in the value of the option 
        per 1% change in volatility while other variables remain constant
        '''
        vega = (self.S * norm.pdf(self.d1) * sqrt(self.T))
        return vega
        