#H atom
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import genlaguerre
n_values=np.arange(1,4,1)
R=np.arange(0,10,0.001)
def l_values(n):
    return np.arange(0,n,1)
for n in n_values:
    for l in l_values(n):
        m=n-l-1
        n=2*l+1
        plt.plot(R,genlaguerre(m,n)(R),label='$L_{}^{}$'.format(m,n))        
plt.title('Laguerre polynomials $L_{n-l-1}^{2l+1}$')
plt.ylabel('$L_{n-l-1}^{2l+1}(x)$')
plt.legend('x')
plt.grid()
plt.legend()
plt.show()

    


