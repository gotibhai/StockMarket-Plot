import matplotlib.pyplot as plt
import numpy as np
t = np.arange(0., 5., 0.2)
# red dashes, blue squares and green triangles
plt.plot(t**4, t**2, 'r--', t**2, t, 'bs', t**2, t**4, 'g^')
plt.show()