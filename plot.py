# import statements 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# set plot style
plt.style.use('fivethirtyeight')

# create the figure
fig = plt.figure()

# create a 1 dimensional subplot as an animaiton canvas
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    # open the data
    plot_data = open('data.txt', 'r').read()
    points = plot_data.split('\n')

    # initialize data as empty lists
    xs = []
    ys = []

    for point in points:
        if len(points) > 1:
            x, y = point.split(',')

            # append values to initial lists
            xs.append(float(x))
            ys.append(float(y))
    
    ax1.clear()
    ax1.plot(xs,ys)

anim = FuncAnimation(fig, animate, interval=1000)
plt.show()