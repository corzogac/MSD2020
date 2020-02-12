from bokeh.plotting import figure
from bokeh.io import output_notebook,show


def TS(t,y):
    #To be able to plot we define first what type of output
    output_notebook()

    #now we create the figure 
    f=figure(title="simple line example", x_axis_label='x', y_axis_label='y')
    f.circle(t,y,size=3,color='navy',legend="Wave",)
    show(f)