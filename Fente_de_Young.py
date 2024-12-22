import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Distance entre l'écran et les trous
D = 1
 
# Taille de l'écran
ecran_x, ecran_y = 0.05, 0.1 

 # Distance entre les trous
a = 1e-4

# longueur d'onde
wave_length = 500e-9

print(f"Interfrange { D*wave_length/a:.2e}",)

# Nb de points sur l'écran
Nx = 501
Ny = 10001

# Intensité des sources
I1 = 1
I2 = 1

# Maillage de l'écran
xm, ym = np.meshgrid(np.linspace(-ecran_x/2, ecran_x/2, Nx), \
                     np.linspace(-ecran_y/2, ecran_y/2, Ny))

S1M = np.sqrt(xm**2 + (ym - a/2)**2 + D**2)
S2M = np.sqrt(xm**2 + (ym + a/2)**2 + D**2)

# diffrence de marche
delta = S2M - S1M

# Formule de l'intensité
I = I1 + I2 + 2*np.sqrt(I1*I2)*np.cos(2*np.pi/wave_length * delta)


fig, ax = plt.subplots()

ax.plot(1000*ym[:,Nx//2], I[:,Nx//2])
ax.set_title("Intensité lumineuse en x = 0")
ax.set_xlabel('y (mm)')
ax.set_ylabel('Intensité')
ax.set_xlim(-10, 10)
ax.grid()

plt.figure()
plt.pcolormesh(xm*1000, ym*1000, I, cmap=mpl.colormaps['gray'])
plt.colorbar()
plt.title("Intensité sur l'écran")
plt.xlabel('x (mm)')
plt.ylabel('y (mm)')
plt.show()
