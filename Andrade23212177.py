"""
Práctica 2:Sistema cardiovascular 

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Andrade Arellano Gael Sebastian
Número de control: 23212177
Correo institucional: l23212177@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""
import numpy as np
import math as m
import matplotlib.pyplot as plt
import control as ctrl
import pandas as pd

u = np.array(pd.read_excel('signal.xlsx',header=None))
u = np.reshape(signal.resample(u,len(t)),-1)

#Datos de la simulacion
x0,t0,tend,dt,w,h = 0,0,10,1E-3,7,3.5
N = round(tend/dt) + 1
t = np.linspace(t0,tend,N)
u1 = np.ones(N) #Step
u2 = np.zeros(N); u2[round(1/dt):round(2/dt)] = 1
u3 = t/tend #Ramp
u4 = np.sin(m.pi/2*t)
u = np.column_stack((u1,u2,u3,u4))
signals = ["HNH", "HIPOTENSO", "HIPERTENSO"]

# Componentes de NORMOTENSO

R,L,C,Z = 0.01,1.500,1.00,0.001
num = [C*L*R,C*R**2+L,R]
den = [C*L*R*Z +L(Z+R),2*R]
sys = ctrl.tf (num,den)
print(f"Funcion de tranferencia: {sys}\n")

# Polos del sistema
L = np.roots(den)
print(f"Polos del sistema: L1 = {L[0]:.3e}, L2 = {L[1]:.3e}\n")

# Componentes del controlador
kI = 169.694398112696
Cr = 1E-6
Re = 1/(Cr*kI)

numPID = [1]
denPID = [Re*Cr,0]
PID = ctrl.tf(numPID,denPID)
print(f"El valor de la capacitancia Cr es de {Cr} Faradios.\n")
print(f"El valor de la capacitancia Cr es de {Re} Ohms.\n")
print(f"Funcion de tranferencia del controlador PID: {PID}\n")

# Sistema de control en lazo cerrado
sysPID = ctrl.feedback(ctrl.series(PID,sys),1,sign = -1)
print(f"Funcion de transferencia del sistema de control en lazo cerrado: {sysPID}\n")

# Colores
clr1 = np.array([9, 21, 64])/255
clr2 = np.array([27, 44, 193])/255
clr3 = np.array([118, 146, 255])/255

# Funciones del sistema en lazo abierto y lazo cerrado
def openloop(t,sys,u):
    _,PAu = ctrl.forced_response(sys,t,u,x0)
    return PAu
def closedloop(t,sysPID,u):
    _,PIDu = ctrl.forced_response(sysPID,t,u,x0)
    return PIDu

# Respuestas: Simulaciones numericas
for i in range(0,4):
    PAu = openloop(t,sys,u[:,i])
    PIDu = closedloop(t,sysPID,u[:,i])
    fg = plt.figure(i+1)
    fg.set_size_inches(w,h)
    plt.rcParams['font.size'] = 11
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['Times New Roman']
    plt.plot(t,u[:,i],'-',color=clr1,label='Ve(t)')
    plt.plot(t,PAu,'--',color=clr2,label='Vs(t)')
    plt.plot(t,PIDu,':',linewidth=2.5,color=clr3,label='PID(t)')
    plt.xlim(0,10); plt.xticks(np.arange(0,11,1))
    if i == 0 or i == 1 or i == 2:
        plt.ylim(-0.1,1.2), plt.yticks(np.arange(-0.1,1.3,0.1))
    elif i == 3:
        plt.ylim(-1.2,1.2), plt.yticks(np.arange(-1.2,1.4,0.2))
    plt.xlabel('t [s]')
    plt.ylabel('Vi(t) [V]')
    plt.legend(bbox_to_anchor=(0.5,-0.25),loc='center',ncol=3,frameon=False)
    plt.show()
    fg.savefig(signals[i]+'_python.pdf',bbox_inches='tight')