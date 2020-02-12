from bokeh.plotting import figure
from bokeh.io import output_notebook,show

#To be able to plot we define first what type of output
output_notebook()

f=figure(title="simple line example", x_axis_label='x', y_axis_label='y')


def TS(t,y):
    
    #now we create the figure 
    f.circle(t,y,size=3,color='navy',legend="Wave")
    show(f)

def Plot(x,y):
    f.circle(x,y,size=3,color='navy',legend="Wave")
    show(f)
