import numpy as np
import matplotlib.pyplot as plt

# numero a generar 
N_numbers = 100000
N_bins = 100

# randon
np.random.seed(0)

# generar el 2d
x, y = np.random.multivariate_normal(
    mean=[0.0, 0.0], 
    cov=[[1.0, 0.4],
         [0.4, 0.25]],
    size=N_numbers
).T 


plt.hist2d(x, y, bins=N_bins, cmap='plasma')


cb = plt.colorbar()
cb.set_label('Number of entries')


plt.title('Heatmap of 2D normally distributed data points')
plt.xlabel('x axis')
plt.ylabel('y axis')


plt.show()

