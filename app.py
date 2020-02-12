import Ploting as P
import numpy as np

x=np.random.randn(1000)
t=np.arange(len(x))
y=10*np.sin(t/200)

P.TS(t,y)
