from bokeh.plotting import figure
from bokeh.io import output_notebook,show

import numpy as np
x=np.random.randn(1000)
t=np.arange(len(x))
y=10*np.sin(t/300)


#To be able to plot we define first what type of output
output_notebook()

#now we create the figure 
f=figure(title="simple line example", x_axis_label='x', y_axis_label='y')
f.circle(t,y,size=3,color='navy',legend="Wave",)
show(f)