#TEMA 1 ELECTRONICA DIGITALA

#Nume: Sturzu Cosmin
#Grupa: 322AB
#Facultatea de Automatica si Calculatoare, IS

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal


t = np.linspace(-0.1, 0.399, 499)
T_period = np.linspace(0, 0.201, 201)
Vmax = 5
semnal_intrare = Vmax/2+Vmax/2*signal.square(5*np.pi*t)



print("[Cazul 3*tau<T] - Introduceti valorile pentru R1 si C1: \n")
print("[Ex: 1600 ohmi] R1 = ")
R1 = input()
R1 = int(R1)
print("[Ex: 8 micro farazi] C1 = ")
C1 = input()
C1 = int(C1)
tau1 = (R1*C1)/1000000
print(3*tau1)
print('Valoarea rezistentei este: %s ohmi\nValoarea condensatorului este: %d micro farazi\n\n' % (R1, C1))



print("[Cazul 3*tau>T] - Introduceti valorile pentru R2 si C2: \n")
print("[Ex: 9100 ohmi] R2 = ")
R2 = input()
R2 = int(R2)
print("[Ex: 12 micro farazi] C2 = ")
C2 = input()
C2 = int(C2)
tau2 = (R2*C2)/1000000
print(3*tau2)
print('Valoarea rezistentei este: %s ohmi\nValoarea condensatorului este: %d micro farazi' % (R2, C2))



#vector pentru cazul 3*tau<T
grafic_1 = [None]*len(t)
j = 0
for i in range(len(t)):
       if(t[i] >= 0 and t[i] <= 1):
              if(semnal_intrare[i] != 0): #daca semnalul de intrare este pe 1 logic, condensatorul se incarca
                     if(j < 200):
                            grafic_1[i] = (Vmax*(1 - np.exp(-T_period[j]/tau1)))
                            j = j + 1
                            new_ampl = grafic_1[i]
                     elif(j == 200):
                            grafic_1[i] = new_ampl
                            j = 0
              else:#daca semnalul de intrare este pe 0 logic, condensatorul se descarca
                     if(j < 200): 
                                          #condensatorul se va descarca de la tensiunea maxima
                                          #la care a ajuns in urma incarcarii folosind "new_ampl"
                            grafic_1[i] = (new_ampl*(np.exp(-T_period[j]/tau1)))
                            j = j + 1
                     elif(j == 200):
                            grafic_1[i] = new_ampl
                            j = 0
       else:
              grafic_1[i] = 0



#vector pentru cazul 3*tau>T
grafic_2 = [None]*len(t)
j = 0
for i in range(len(t)):
       if(t[i] >= 0 and t[i] <= 1):
              if(semnal_intrare[i] != 0): #daca semnalul de intrare este pe 1 logic, condensatorul se incarca
                     if(j < 200):
                            grafic_2[i] = (Vmax*(1 - np.exp(-T_period[j]/tau2)))
                            j = j + 1
                            new_ampl = grafic_2[i] 
                     elif(j == 200):               
                            grafic_2[i] = new_ampl
                            j = 0
              else: #daca semnalul de intrare este pe 1 logic, condensatorul se descarca
                     if(j < 200):          
                                          #condensatorul se va descarca de la tensiunea maxima
                                          #la care a ajuns in urma incarcarii folosind "new_ampl"
                            grafic_2[i] = (new_ampl*(np.exp(-T_period[j]/tau2)))
                            j = j + 1
                     elif(j == 200):
                            grafic_2[i] = new_ampl
                            j = 0
       else:
              grafic_2[i] = 0

#Legarea condensatorului la Vcc
for i in range(len(t)):
       grafic_1[i]-=5
       grafic_2[i]-=5


fig1, ax = plt.subplots(3, 1, constrained_layout = True)
limit = [0]*len(t)

ax[0].plot(t, semnal_intrare)
ax[1].plot(t, grafic_1, color = 'green')
ax[1].plot(t, limit, linestyle = '--')
ax[2].plot(t, grafic_2, color = 'red')
ax[2].plot(t, limit, linestyle = '--')

ax[0].set_title('Semnal intrare')
ax[0].set_xlabel('Timp (s)')
ax[0].set_ylabel('Tensiune (V)')
ax[0].grid()

ax[1].set_title('Cazul 3*tau<T')
ax[1].set_xlabel('Timp (s)')
ax[1].set_ylabel('Tensiune (V)')
ax[1].grid()

ax[2].set_title('Cazul 3*tau>T')
ax[2].set_xlabel('Timp (s)')
ax[2].set_ylabel('Tensiune (V)')
ax[2].grid()

fig1.savefig("fig1.png")


fig2, all = plt.subplots(1, 1, constrained_layout = True)
all.plot(t, semnal_intrare, label = "Semnal intrare")
all.plot(t, grafic_1, color = 'green', label = "3*tau<T")
all.plot(t, grafic_2, color = 'red', label = "3*tau>T")
plt.legend()
all.set_xlabel('Timp (s)')
all.set_ylabel('Tensiune (V)')
all.grid()
fig2.savefig("fig2.png")
