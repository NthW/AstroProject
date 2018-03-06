import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import mpl_toolkits.mplot3d.axes3d as p3
from mpl_toolkits.mplot3d import Axes3D
def datagen():


    #number nodes in x direction
    nx = 100

    xdim = np.arange(nx)
    #length dx (between nodes for wavelength 2)
    dx = (4/(nx-1))

    #number time steps
    nt = 400

    #increment of time
    dt = .01

    #initial condtions
    u = np.ones(nx)
    u[0:10] = 2

    ustg = np.zeros(shape=(nx,nt))
    #wavespeed
    c = 10
    ustg[:,0] = u
    for n in range(nt-1):
        for i in range(nx):
            ustg[0,:] = 1
            ustg[i,n+1] = ustg[i,n] - (c*(dt/dx)*(ustg[i,n] - ustg[i-1,n])/2)

        print(np.sum(ustg[:,n]))

    return ustg

u1 = datagen()
#u2 = np.ndarray


# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')



# animation function.  This is called sequentially
def animate(i):

    x = np.linspace(0, 1,100)
    y = np.linspace(0, 1,100)

    z = u1[:,i]
    x,y = np.meshgrid(x,y)

    #plt.title("%s"%(np.sum(u[:,i])))
    ax.clear()

    line = ax.plot_wireframe(x, y,z)
    ax.set(xlim = (0,1), ylim = (0,1), zlim = (1,2) )
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate,
                               frames=300, interval=50, blit=False)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()