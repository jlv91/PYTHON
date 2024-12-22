import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

   
class dalembert_simu():
    def __init__(self, x, y0, coef, end_fixed = True):
        self.x, self.y0, self.coef = x, y0, coef
        self.end_fixed = end_fixed
        self.y_prev, self.y, self.y_new = np.copy(y0), np.copy(y0), np.zeros_like(y0)

    def shift_left(self, arr):
        result = np.roll(arr, -1)
        result[-1] = result[-2]
        return result
    
    def shift_right(self, arr):
        result = np.roll(arr, 1)
        result[0] = result[1]
        return result

    def step(self, i):
        # calcule y_new selon l'equation des ondes de d'Alembert à partir de y et y_prev
        self.y_new = 2 * self.y - self.y_prev + self.coef * (self.shift_left(self.y) - 2 * self.y + self.shift_right(self.y))
        
        # on force l'extrémité en 0 à 0 car elle ne bouge pas
        self.y_new[0] = 0
        # on peut avoir l'autre extrémité fixe ou libre
        if self.end_fixed:
            self.y_new[-1] = 0

        # switch list
        self.y_prev = np.copy(self.y)
        self.y = self.y_new

        return self.y_new

class generateur_profil():    
    def __init__(self, x, A):
        self.x, self.A = x, A
        
    def corde_frappee(self) :
        # frappee au milieu
        x0, dl = 50, 20
        y0 = np.zeros_like(self.x)
        
        mask = ((self.x >= x0 - dl / 2) & (self.x <= x0 + dl / 2))
        y0[mask] = self.A
        return y0  
    
    def corde_pincee(self, x0 = 10, dl = 20) :
        x_left, x_right = x0 - dl / 2, x0 + dl / 2
        
        y0 = np.zeros_like(self.x)

        mask = (self.x >= x_left) & (self.x < x0)
        y0[mask] = self.A * (self.x[mask] - x_left) / (x0 - x_left)
        
        mask = (self.x >= x0) & (self.x <= x_right)
        y0[mask] = self.A * (x_right - x[mask]) / (x_right - x0)
        return y0

    def corde_frappee_attenuation_phenomene_GIBBS(self) :
        x0, dl, dl2 = 50, 20, 3
        y0 = np.zeros_like(self.x)
        x_left_start = x0 - dl / 2
        x_left_end = x_left_start + dl2
        x_right_start = x0 + dl / 2 - dl2
        x_right_end = x0 + dl / 2
        
        mask = (self.x >= x_left_start) & (self.x < x_left_end)
        y0[mask] = self.A * (self.x[mask] - x_left_start) / dl2

        mask = (self.x >= x_left_end) & (self.x <= x_right_start)
        y0[mask] = self.A

        mask = (self.x > x_right_start) & (self.x <= x_right_end)
        y0[mask] = self.A * (x_right_end - x[mask]) / dl2
        return y0
    
nb_frames = 5000
L = 100 # longueur de la corde
N = 1001 # nombre de point sur la corde

x = np.linspace(0, L, N)

Ampl = 0.1
generateur_profil = generateur_profil(x, Ampl)
#y0 = generateur_profil.corde_frappee_attenuation_phenomene_GIBBS()
#y0 = generateur_profil.corde_frappee()
y0 = generateur_profil.corde_pincee(50, 20)
# y0 = generateur_profil.corde_pincee()

# description du milieu de propagation
# on peut utiliser n'importe quel profil de célérité (indice) pour c
# permettrait de simuler la transmission et la réflexion d'une onde sur un changement de milieu (indice)
# On prend un milieu homogène avec une célérité de 1
c0 = 1
c = c0 * np.ones(N)

# Définition du coefficent r de l'equation discrète de propagation
dx = L/(N-1) # on pourrait avoir un dx local
dt = dx / c0 * 0.5 # pas de temps, pour que ça converge il faut dt < dx/c0
coef = (c * dt / dx)**2

# init simulation
simu = dalembert_simu(x, y0, coef)


fig, ax = plt.subplots()
line, =  ax.plot(simu.x, simu.y0)
plt.title("Onde progressive")

ax.set_ylim([-1.5 * Ampl, 1.5 * Ampl])
ax.axhline(y=0, alpha=0.5, color="black")
ax.grid(True)

label = ax.text(80, -0.1, "", ha='center', va='center', fontsize=15, color="Red")

def update(i):
    line.set_ydata(simu.step(i))
    label.set_text("{0:>5.0f}/{1}".format(round(i, -1), nb_frames))
    return line,label

ani = anim.FuncAnimation(fig, update, frames=range(nb_frames), blit=True, interval=1, repeat=False)

plt.show()
plt.close()