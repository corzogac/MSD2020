
from bokeh.plotting import figure
from bokeh.io import output_notebook,show
from bokeh.layouts import column


#To be able to plot we define first what type of output
output_notebook()
  

#now we create the figure 
f=figure(title="Mandelbot", x_axis_label='x', y_axis_label='y')

#for imaginary
a=(2+3j)

m=np.linspace(-1,1,1000)
X1=m
X2=1j*m
max_iter=1000

rows=np.linspace(1,100,100)
cols=np.linspace(1,100,100)
width=100
height=100

for i in rows:
    for j in cols:
        c_re=(j - width/2.0)*4.0/width
        c_im=(i - height/2.0)*4.0/width
        iteration=0
        x=0
        y=0
        while(x**2+y**2<=4 and iteration<max_iter):
            Xnew=x**2+y**2+c_re
            y=2*x*y+c_im
            x=Xnew
        if(iteration<max_iter):
            f.circle(x,y,size=3,color='navy',legend="Wave")
        else:
            f.circle(x,y,size=3,color='black',legend="Wave")

show(f)



P.Pt(X1,X2)