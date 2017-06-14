import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate 
import matplotlib.ticker as tick


v = plt.figure()
v.suptitle("Velocity", fontsize=14, fontweight='bold')
x, y = np.loadtxt('droptower_vdata.txt', float,'#','   ', unpack = True )
print("Time: ", x)
print("Velocity: ", y)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
#set x axis intervals
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.yticks(np.arange(-24, 24,  2.0))

plt.plot(x,y, marker = 'o')
plt.savefig('velocity.png')


acceleration = np.diff(y)
a_time = np.delete(x, len(x)-1)
print("Acceleration: ", acceleration)

a=plt.figure()
a.suptitle("Acceleration", fontsize=14, fontweight='bold')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration ( $m^2$ /s)')
plt.xticks(np.arange(min(a_time), max(a_time)+1, 1.0))

plt.plot(a_time, acceleration, marker= 'o')
plt.savefig('acceleration.png')




position = integrate.cumtrapz(y, initial = 0)
print("Dsiplacement: " , position)

p=plt.figure()
p.suptitle("Displacement", fontsize=14, fontweight='bold')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.xticks(np.arange(min(x), max(x)+1, 1.0))

plt.plot(x, position, marker = 'o')
plt.savefig('position.png')


all_three= plt.figure()
plt.plot(x,y,color='r',marker='o', label = 'Velocity (m/s)')
plt.plot(x,position, color='b',marker='v', linestyle= 'dotted', label= 'Position (m)')
plt.plot(a_time,acceleration, color= 'g', marker='s', linestyle= 'dashed', label = 'Acceleration ( $m^2$ /s)')
plt.xlabel('Time (s)')
plt.suptitle("Motion of Drop Tower", fontsize=14, fontweight='bold')
plt.legend()
plt.xticks(np.arange(min(x), max(x)+1, 1))

f, axarr = plt.subplots(3, sharex=True)
axarr[0].plot(x,y,color='r',marker='o')
axarr[0].set_xlim([0,10])
axarr[0].set_title('Velocity (m/s)')
axarr[1].plot(a_time,acceleration, color= 'g', marker='s', linestyle= 'dashed')
axarr[1].set_title('Acceleration ( $m^2$ /s)')
axarr[2].plot(x,position, color='b',marker='v', linestyle= 'dotted')
axarr[2].set_title('Position (m)')
plt.xlabel('Time (s)')
f.subplots_adjust(hspace=0.3)
plt.suptitle("Motion of Drop Tower", fontsize=14, fontweight='bold')
plt.xticks(np.arange(min(x), max(x)+1, 1))
plt.show()