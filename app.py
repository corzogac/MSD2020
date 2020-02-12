from bokeh.plotting import figure,output_file,show

import numpy as np

x=np.random.randn(10)
y=10*np.sin(x)

#To be able to plot we define first what type of output
output_file('sine.html')

#now we create the figure 
f=figure(title="simple line example", x_axis_label='x', y_axis_label='y')
f.line(x,y,legend="Wave")
show(f)