import Ploting as P
import numpy as np

x=np.random.randn(1000)
t=np.arange(len(x))
y=10*np.sin(t/200)

P.TS(t,y)


#for imaginary
a=(2+3j)

m=np.linspace(-1,1,1000)
X1=m
X2=1j*m

P.Plot(X1,X2)