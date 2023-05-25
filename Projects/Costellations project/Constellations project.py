# Constellations visualisation project:
# Help astronomers map out the stars in the Orion constellation using 2D, 3D scatter plots

# Import internal library
import codecademylib3

# 1
# Import libraries and modules
# Import matplotlib
import matplotlib.pyplot as plt
# Import 3D visualization library
from mpl_toolkits.mplot3d import Axes3D

# 2
# View given x,y,z coordinates
x = [-0.41, 0.57, 0.07, 0.00, -0.29, -0.32,-0.50,-0.23, -0.23]
y = [4.12, 7.71, 2.36, 9.10, 13.35, 8.13, 7.19, 13.25,13.43]
z = [2.06, 0.84, 1.56, 2.07, 2.36, 1.72, 0.66, 1.25,1.38]

# 3
# Create a figure
fig = plt.figure()
# Add your subplot
ax = fig.add_subplot(1,1,1)
# Create a scatter plot
ax.scatter(x,y,color="yellow")
ax.set_facecolor("black")
plt.title("2D Visualisation of Orion Constellation")
plt.show()

# 4
# Create a figure
fig_3d = plt.figure()
# Add your subplot
ax = fig_3d.add_subplot(1,1,1,projection="3d")
# Create a scatter plot
ax.scatter(x,y,z,color="yellow")
ax.set_facecolor("black")
plt.title("3D Visualisation of Orion Constellation")
plt.show()
 