# -*- coding: utf-8 -*-
#PHYS 512 Problem set 1 — Julia Lascar — julia.lascar@mail.mcgill.ca
import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate


#-------------------------------------PROBLEM 1------------------------------------------
#A)
print("Problem 1",'\n',"A)")
#Working out the formula
#from Taylor series: f(x+delta)-f(x-delta)= 2*delta*f'(x) + 2*delta^3*f'''(x) + O(delta^5)
#[f(x+delta)-f(x-delta)]/[2*delta]= f'(x) + delta^2*f'''(x) + O(delta^4)
#from Taylor series: f(x+2delta)-f(x-2delta)= 4*delta*f'(x) + 2*(2delta)^3*f'''(x) + O(delta^5)
#[f(x+2delta)-f(x-2delta)]/2delta= 2*f'(x) + 8*(delta)^2*f'''(x) + O(delta^4)
#8*diff1-diff2= 6f'(x) + O(delta^5)
#f'(x)= [8*diff1-diff2]/6 - O(delta^5)

def firstderiv(x0,delta,fun):
    x=(x0-2*delta,x0-delta,x0+delta,x0+2*delta)
    y=fun(x)
    diff1= (y[2]-y[1])/(2*delta)
    diff2= (y[3]-y[0])/(2*delta)
    firstderiv= (8*diff1 -diff2)/6
    return firstderiv
     
#Sanity Check  
fd=firstderiv(1,0.0000001,np.exp)
print("We find that d(exp(x))/dx evaluated at 1 is:",fd)
print("Which corresponds to our expectation of",np.exp(1)) 
print("The error is",abs(np.exp(1)-fd))
#B)
print('\n',"B)")
#Since the leading order of delta is to the power of 5
#if we take machine precision to be epsilon=10e-16
#Delta should be (10e-16)^1/5
#for f(x)=exp(x)
delta=(10e-16)**(1/5)
exp=firstderiv(2,delta,np.exp)
print("We find that d(exp(x))/dx evaluated at 2 is",exp,"thus our error is:",abs(np.exp(2)-exp)) 

def e001(x):
    y=np.exp(np.asarray(x)*0.001)
    return y 

exp001=firstderiv(2,delta,e001)
print("We find that d(exp(0.001x))/dx evaluated at 2 is",exp001,"thus our error is:",abs(0.001*np.exp(0.001*2)-exp001)) 


#-------------------------------------PROBLEM 2------------------------------------------
print('\n',"Problem 2")
def temperature(V):
    data = np.loadtxt("Lascar512/lakeshore.txt")
    data = np.transpose(data)
    temperature, voltage = data[0], data[1]
    ind=np.argsort(voltage)
    temperature=temperature[ind]
    voltage=voltage[ind]
    spln=interpolate.splrep(voltage,temperature)
    yy=interpolate.splev(V,spln)
    return yy

V=1.4
T=temperature(V)
if (V<9.0681e-02) or (V>1.64429):
    print("A voltage of",V,"V is outside the bounds of this interpolation.")
else:
    print("For a voltage of ",V,"V the temperature is",T,"K.")

#estimate error 
#difference between linear fit and interpolation 

#just to get a nice plot:
data = np.loadtxt("Lascar512/lakeshore.txt")
data = np.transpose(data)
temp, volt = data[0], data[1]
plt.clf()
plt.plot(volt, temp,"*")
plt.plot(volt,temperature(volt))
plt.savefig("Interpolation of temperature as a function of voltage for Diodes DT-670.png")
#-------------------------------------PROBLEM 3------------------------------------------
print('\n',"Problem 3")

#This is just the code in class: figure out what is meant by "calling" a function multiple times
def intergrate(fun,a,b,tol=1e-8): #if you don't specify, it's 10^-8
    x=np.linspace(a,b,5) #get 5 points that are evenly spaced between a and b
    dx=(b-a)/4
    y=fun(x)
    dumb_integral=(y[0]+4*y[2]+y[4])/6.0*(b-a)
    less_dumb_integral=(y[0]+4*y[1]+2*y[2]+4*y[3]+y[4])/12*(b-a)
    myerr=np.abs(dumb_integral-less_dumb_integral)
    neval=5
    if myerr<tol:
        return (16*less_dumb_integral-dumb_integral)/15,neval
    x_mid=0.5*(b+a)
    left_integral,left_neval=integrate(fun,a,x_mid,tol/2.0)
    right_integral,right_neval=integrate(fun,x_mid,b,tol/2.0)
    integral=left_integral+right_integral
    return integral,nevalx

def linear (x):
    y=x
    return y 
    
def square(x):
    y=x**2
    return y
    
intx=intergrate(linear,0,2)
print( intx)
#---------------------------------PROBLEM 4--------------------------------------

