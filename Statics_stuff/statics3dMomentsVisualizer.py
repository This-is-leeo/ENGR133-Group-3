import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



point1 = np.array([0,0,0])
point2 = np.array([80,0,300])
point3 = np.array([-240,240,0])

fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection='3d')

ax1.quiver(point1[0], point1[2], point1[1], point2[0], point2[2], point2[1], color = 'r')
ax1.quiver(point2[0], point2[2], point2[1], point3[0], point3[2], point3[1], color = 'g')

ax1.set_xlabel('X Axis')
ax1.set_ylabel('Z Axis')
ax1.set_zlabel('Y Axis')
ax1.set_title('3D Vector Plot')



ax1.set_xlim([-240,80])
ax1.set_zlim([0, 80])
ax1.set_ylim([0, 300])    


plt.show()

print(f"answer: {ans}") 
# Create a figure and 3D axes
"""fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Starting points (x, y, z)
start_points = np.array([[0, 0, 0], [1, 1, 1], [-1, 2, -1]])

# Vector components (u, v, w)
vectors = np.array([[2, 1, 3], [-1, 2, -2], [3, -1, 4]])

# Plot each vector
ax.quiver(start_points[:, 0], start_points[:, 1], start_points[:, 2],
          vectors[:, 0], vectors[:, 1], vectors[:, 2], color='g')

# Set the limits for the axes
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])

# Set labels
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Vector Plot')

# Display the plot
plt.show()"""

