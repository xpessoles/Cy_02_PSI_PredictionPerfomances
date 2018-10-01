import numpy as np
import matplotlib.pyplot as plt

les_t = np.logspace(1,2,10000)
les_g = np.sqrt(2-2*np.cos(.1*les_t))
les_g  =20*np.log10(les_g)
les_phi = np.arctan(np.sin(les_t)/(1-np.cos(les_t)))
#plt.loglog(les_t,les_g)
plt.semilogx(les_t,les_phi)
plt.grid()
plt.show()