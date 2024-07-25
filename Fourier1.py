import numpy as np
import matplotlib.pyplot as plt
## Differential Equation

Ts = 0.001
Tf = 3
T0 = 1
w0 = 2*np.pi/T0
t = np.arange(-10,Tf,Ts)
N = 5




xf = 5*np.ones(t.size)
print(xf)
print(xf.size)

for i in range(1,N):

    xf = xf + 20/np.pi*(np.sin(i*np.pi/2)/i)*np.cos(2*i*np.pi*t)


plt.plot(t,xf)
plt.title("Fourier Series")
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()