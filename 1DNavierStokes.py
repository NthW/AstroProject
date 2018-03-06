import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
def datagen():


    #number nodes in x direction
    nx = 50

    xdim = np.arange(nx)
    #length dx (between nodes for wavelength 2)
    dx = (2/(nx-1))

    #number time steps
    nt = 200

    #increment of time
    dt = .01

    #initial condtions
    u = np.ones(nx)
    u[1:10] = 2
    ustg = np.zeros(shape=(nx,nt))
    #wavespeed
    c = 100
    ustg[:,0] = u
    for n in range(nt-1):
        for i in range(nx-1):
            if i==0 or i==nx-2:
                ustg[i, n + 1] = 1
            else:
                ustg[i,n+1] = ustg[i,n] - (c*(dt/dx)*(ustg[i,n] - ustg[i-1,n])/2)
    return ustg

u = datagen()



# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-.25, 1), ylim=(-2, 5))
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(0, 1, )
    y = u[:,i]
    line.set_data(x, y)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=100, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()