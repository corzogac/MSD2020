from bokeh.plotting import figure
from bokeh.io import output_notebook,show
from bokeh.layouts import column
from bokeh.plotting import figure


#To be able to plot we define first what type of output
output_notebook()
  

#now we create the figure 
f=figure(title="Trying", x_axis_label='x', y_axis_label='y')

#To be able to plot we define first what type of output
output_notebook()

f=figure(title="simple line example", x_axis_label='x', y_axis_label='y')

def TS(t,y):
    f.circle(t,y,size=3,color='navy')
    show(f)

def Input():
   
    from bokeh.io import output_file, show
    from bokeh.layouts import widgetbox
    from bokeh.models.widgets import Button, RadioButtonGroup, Select, Slider

    output_file("layout_widgets.html")

    # create some widgets
    slider = Slider(start=0, end=10, value=1, step=.1, title="Slider")
    button_group = RadioButtonGroup(labels=["Option 1", "Option 2", "Option 3"], active=0)
    select = Select(title="Option:", value="foo", options=["foo", "bar", "baz", "quux"])
    button_1 = Button(label="Button 1")
    button_2 = Button(label="Button 2")

    # put the results in a row
    show(widgetbox(button_1, slider, button_group, select, button_2, width=300))



