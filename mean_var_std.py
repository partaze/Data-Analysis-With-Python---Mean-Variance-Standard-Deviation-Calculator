'''@Author: Cheryl Vadivello
Function to calculate mean,variance,standard deviation,min,max,sum of a list
using Numpy'''
import numpy as np

def calculate(list):
  
  if len(list)!=9:
    raise ValueError("List must contain nine numbers.")
  else:
    calculations={}
    a = np.array(list).reshape(3,3)
    alist =[a.mean,a.var,a.std,a.max,a.min,a.sum]
    blist = [np.mean,np.var,np.std,np.max,np.min,np.sum]
    words = ["mean","variance","standard deviation","max","min","sum"]
#Little loop to reduce lines of code. Performs the passed statistical functions.
    for i in range(len(alist)):
      func,func1,word = alist[i],blist[i],words[i]
      a1,a2,a3= func(axis=0).tolist(),func(axis=1).tolist(),func1(list)
      calculations[word]= [a1,a2,a3]
    return calculations