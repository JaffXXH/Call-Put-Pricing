# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:11:02 2020

@author: jaff_
"""
import numpy as np
import math
import pandas as pd

class BinomialModel(object):
    """Option Pricing via binomial tree.
    Attributes
    ==========
    PutCall: Str
    option type "put" or "call"
    S : float
    stock price
    K : float
    strike price
    T : float
    expiration time in year
    sigma : float
    volatility
    r : float
    risk-free rate
    cp : +1/-1 for call/put
    AmOpt : bool
    True/False for American/European option
    N : float
    binomial steps

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
    """ 
    def __init__(self,PutCall : str,  S: float, K: float, T: float, r: float, sigma: float, AmOpt:bool =False, N:float=100):
        self.PutCall = PutCall.lower()
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.AmOpt = AmOpt
        self.N = N
        #delta T
        self.DeltaT = self.T/self.N
        #up factor
        self.u= math.exp(self.sigma * math.sqrt(self.DeltaT))
        self.d = 1/self.u
        # #down factor
        self.drift = math.exp(self.r*self.DeltaT)
        #risk neutral drift
        self.q = (self.drift - self.d)/(self.u  - self.d)
        if self.PutCall == "call":
            self.cp = 1
        elif self.PutCall == "put":
            self.cp = -1
        else: 
            raise ValueError("expected 'put' or 'call' as value for PutCall")
        self.StkTree = np.zeros((self.N + 1, self.N + 1)) #Square matrix used to stock the tree of the stock price


        # generating the tree for the stock price
        self.StkTree[0, 0] = self.S
        for ii in range(1, self.N+1):
            self.StkTree[ii, 0] = self.StkTree[ii-1, 0] * self.u 
            for jj in range(1, ii+1):
                self.StkTree[ii,jj] = self.StkTree[ii-1, jj-1] * self.d
                
        my_df= pd.DataFrame(self.StkTree)
        my_df.to_csv('out.csv', index=True, header=True)

    def value(self):
        ''' value of the option calculated using 
        Backward recursion on the binomial tree
         '''
        OptTree = np.zeros((self.N + 1, self.N + 1))
        for jj in range(self.N+1):
            OptTree[self.N, jj] = max(0, self.cp * (self.StkTree[self.N,jj] - self.K))
        for ii in range(self.N-1, -1, -1):
            for jj in range(ii + 1):
                OptTree[ii, jj] = (self.q * OptTree[ii+1, jj] +
                                  (1 - self.q) * OptTree[ii + 1, jj + 1]) / self.drift
                if self.AmOpt:
                    OptTree[ii, jj] = max(
                        OptTree[ii, jj], self.cp * (self.StkTree[ii, jj] - self.K))
        return OptTree[0, 0]
    
    def delta_(self):
        '''price sensitivity to the underlying asset
        it's  the first derivative of the option price with respect 
        to the current value of the underlying.
        approximated using the intermediary values of the binomial tree'''
        OpUp = max(0, self.cp * (self.StkTree[1, 1]- self.K) )
        OpDn = max(0, self.cp * (self.StkTree[1, 0]- self.K ))
        delta = (OpUp - OpDn) / (self.StkTree[1, 1] - self.StkTree[1, 0])
        return delta
    
    def delta(self):
        value_init = self.value() #Initial option value
        #reevaluating parameters after bumping the volatility
        new_s = self.S*1.01
        
        NewTree = np.zeros((self.N + 1, self.N + 1)) #Square matrix used to stock the tree of the stock price
        # generating the tree for the stock price
        NewTree[0, 0] = new_s
        for ii in range(1, self.N+1):
            NewTree[ii, 0] = NewTree[ii-1, 0] * self.u
            for jj in range(1, ii+1):
                NewTree[ii,jj] = NewTree[ii-1, jj-1] * self.d
        #reevaluating option value after bump
        OptTree = np.zeros((self.N + 1, self.N + 1))
        for jj in range(self.N+1):
            OptTree[self.N, jj] = max(0, self.cp * (NewTree[self.N,jj] - self.K))
        for ii in range(self.N-1, -1, -1):
            for jj in range(ii + 1):
                OptTree[ii, jj] = (self.q * OptTree[ii+1, jj] +
                                  (1 - self.q) * OptTree[ii + 1, jj + 1]) / self.drift
                if self.AmOpt:
                    OptTree[ii, jj] = max(
                        OptTree[ii, jj], self.cp * (NewTree[ii, jj] - self.K))
        delta =  (OptTree[0, 0]- value_init)/( self.S*0.01) #Evaluation of the impact of the bump
        return delta
    
    def gamma(self):
        value_init = self.value() #Initial option value
        #reevaluating parameters after bumping the volatility
        new_s = [self.S*1.01, self.S*0.99]
        NewTree = np.zeros((self.N + 1, self.N + 1)) #Square matrix used to stock the tree of the stock price
        # generating the tree for the stock price
        result=np.zeros((1,2))
        a= 0
        for zz in new_s:
            NewTree[0, 0] = zz
            for ii in range(1, self.N+1):
                NewTree[ii, 0] = NewTree[ii-1, 0] * self.u
                for jj in range(1, ii+1):
                    NewTree[ii,jj] = NewTree[ii-1, jj-1] * self.d
            #reevaluating option value after bump
            OptTree = np.zeros((self.N + 1, self.N + 1))
            for jj in range(self.N+1):
                OptTree[self.N, jj] = max(0, self.cp * (NewTree[self.N,jj] - self.K))
            for ii in range(self.N-1, -1, -1):
                for jj in range(ii + 1):
                    OptTree[ii, jj] = (self.q * OptTree[ii+1, jj] +
                                      (1 - self.q) * OptTree[ii + 1, jj + 1]) / self.drift
                    if self.AmOpt:
                        OptTree[ii, jj] = max(
                            OptTree[ii, jj], self.cp * (NewTree[ii, jj] - self.K))
            result[0,a]= OptTree[0, 0]
            a+=1        
        gamma = (result[0, 0] + result[0, 1]- 2*value_init)/( self.S*0.01)**2 #Evaluation of the impact of the bump
        return gamma
    
    def gamma_(self):
        ''' Second order derivative with respect to change in the
        underlying spot price approximated using the intermediary 
        values of the binomial tree'''
        delta1 = (max(0, self.cp * (self.StkTree[2, 1]- self.K ) )- 
                  max(0, self.cp * (self.StkTree[2, 0]- self.K ) ))/(self.StkTree[2, 1] - self.StkTree[2, 0])
        delta2 = (max(0, self.cp * (self.StkTree[2, 2]- self.K )) -
                  max(0, self.cp * (self.StkTree[2, 1]- self.K ) ))/ (self.StkTree[2, 2] - self.StkTree[2, 1])
        gamma= (delta2 - delta1)/0.5*(self.StkTree[2, 2] - self.StkTree[2, 0])
        return gamma
    
    def theta_(self):
        '''price sensitivity to the time to maturity
        The rate of change in the value of the option per one day 
        decrease in the option time while other variables remain constant.
        '''
        theta = (max(0, self.cp * (self.StkTree[2, 1]- self.K )) - 
                 max(0, self.cp * (self.StkTree[0, 0]- self.K ) ))/2*self.DeltaT
        return theta
    
    def theta(self):
        value_init = self.value() #Initial option value
        #reevaluating parameters after bumping the volatility
        new_t = self.T*1.01
        new_dt = new_t/self.N
        #up factor
        uu= math.exp(self.sigma * math.sqrt(new_dt))
        dd = 1/uu
        # #down factor
        new_df = math.exp(self.r*new_dt)
        #risk neutral drift
        qq = (new_df - dd)/(uu  - dd)
        
        NewTree = np.zeros((self.N + 1, self.N + 1)) #Square matrix used to stock the tree of the stock price
        # generating the tree for the stock price
        NewTree[0, 0] = self.S
        for ii in range(1, self.N+1):
            NewTree[ii, 0] = NewTree[ii-1, 0] * uu
            for jj in range(1, ii+1):
                NewTree[ii,jj] = NewTree[ii-1, jj-1] * dd
        #reevaluating option value after bump
        OptTree = np.zeros((self.N + 1, self.N + 1))
        for jj in range(self.N+1):
            OptTree[self.N, jj] = max(0, self.cp * (NewTree[self.N,jj] - self.K))
        for ii in range(self.N-1, -1, -1):
            for jj in range(ii + 1):
                OptTree[ii, jj] = (qq * OptTree[ii+1, jj] +
                                  (1 - qq) * OptTree[ii + 1, jj + 1]) / new_df
                if self.AmOpt:
                    OptTree[ii, jj] = max(
                        OptTree[ii, jj], self.cp * (NewTree[ii, jj] - self.K))
        theta =  (OptTree[0, 0]- value_init)/( self.T*0.01) #Evaluation of the impact of the bump
        return theta
    
    def rho(self):
        '''price sensitivity to the interest rate
        The rate of change in the value of the option 
        per 1% change in the risk-free rate while other variables remain constant
        '''
        value_init = self.value() #option value before bump
        
        #Reevaluating the option after bumping the interest rate
        ddrift = math.exp((self.r+0.01)*self.DeltaT)
        qq = (ddrift - self.d)/(self.u  - self.d)
        
        OptTree = np.zeros((self.N + 1, self.N + 1))
        for jj in range(self.N+1):
            OptTree[self.N, jj] = max(0, self.cp * (self.StkTree[self.N,jj] - self.K))
        for ii in range(self.N-1, -1, -1):
            for jj in range(ii + 1):
                OptTree[ii, jj] = (qq * OptTree[ii+1, jj] +
                                  (1 - self.q) * OptTree[ii + 1, jj + 1]) / ddrift
                if self.AmOpt:
                    OptTree[ii, jj] = max(
                        OptTree[ii, jj], self.cp * (self.StkTree[ii, jj] - self.K))
        rho =  (OptTree[0, 0]- value_init)/0.01 #Evaluation of the impact of the bump
        return rho
    
    def vega(self):
        value_init = self.value() #Initial option value
        #reevaluating parameters after bumping the volatility
        uu = math.exp((self.sigma+0.01)*math.exp(self.DeltaT)) 
        dd= 1/uu
        qq = (self.drift - dd)/(uu  - dd)
        
        NewTree = np.zeros((self.N + 1, self.N + 1)) #Square matrix used to stock the tree of the stock price
        # generating the tree for the stock price
        NewTree[0, 0] = self.S
        for ii in range(1, self.N+1):
            NewTree[ii, 0] = NewTree[ii-1, 0] * uu
            for jj in range(1, ii+1):
                NewTree[ii,jj] = NewTree[ii-1, jj-1] * dd
        #reevaluating option value after bump
        OptTree = np.zeros((self.N + 1, self.N + 1))
        for jj in range(self.N+1):
            OptTree[self.N, jj] = max(0, self.cp * (NewTree[self.N,jj] - self.K))
        for ii in range(self.N-1, -1, -1):
            for jj in range(ii + 1):
                OptTree[ii, jj] = (qq * OptTree[ii+1, jj] +
                                  (1 - qq) * OptTree[ii + 1, jj + 1]) / self.drift
                if self.AmOpt:
                    OptTree[ii, jj] = max(
                        OptTree[ii, jj], self.cp * (NewTree[ii, jj] - self.K))
        vega =  (OptTree[0, 0]- value_init)/0.01 #Evaluation of the impact of the bump
        return vega
        
        
        
BM= (BinomialModel(PutCall = "call", S=150, K= 145, T= 2, sigma = 0.2, r=0.05, AmOpt= True, N=100))
# BM.value()

# dic= {}
# for j in range(1,50):
#     dic[j] = ( BinomialModel(PutCall = "call", S=100, K= 110, T= 2, sigma = 0.05, r=0.05, AmOpt= False, N=j)).value()

# import matplotlib.pylab as plt

# lists = sorted(dic.items()) # sorted by key, return a list of tuples

# x, y = zip(*lists) # unpack a list of pairs into two tuples

# plt.plot(x, y)
# plt.show()





