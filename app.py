import Ploting as P
import numpy as np

x=np.random.randn(1000)
t=np.arange(len(x))
y=10*np.sin(t/200)

P.TS(t,y)

from bokeh.plotting import figure
from bokeh.io import output_notebook,show
f=figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# This is a comment


Probando 1 2 3

