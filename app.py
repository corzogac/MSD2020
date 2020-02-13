import Ploting as P
import numpy as np

x=np.random.randn(1000)
t=np.arange(len(x))
y=10*np.sin(t/200)

P.TS(t,y)

<<<<<<< HEAD
from bokeh.plotting import figure
from bokeh.io import output_notebook,show
f=figure(title="simple line example", x_axis_label='x', y_axis_label='y')
=======
P.Input()
>>>>>>> 8418b699c146f0642c3c5fe856ab7ac61352bb54

