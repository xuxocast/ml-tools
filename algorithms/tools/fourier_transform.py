import matplotlib.pyplot as plt
import numpy as np
import os
plt.rcParams.update({'font.size': 15})

############################# SERIE DE TIEMPO #############################
# Crea una función para generar una Serie de Tiempo como ejemplo
def time_func(t):
    # Estas son los periodos naturales que deberán de salir en la DFT
    periodos = [4,5,10]
    # ---------------------------------------------------------------
    freqs = [2*np.pi/T for T in periodos]
    # La serie de tiempo consta de una superposición de funciones 'seno'
    # que son funciones oscilatorias
    return sum([ np.sin(f*t) for f in freqs])
#-------------------------------------------------------------------
# Definimos cada cuándo se tendrán observaciones (sampleo)
delta_t = 1
# Definimos el no. de observaciones
nn = 200
# Generamos la serie de tiempo
t_sampl = [i*delta_t for i in range(nn)]
time_series = [time_func(x) for x in t_sampl]
#-------------------------------------------------------------------
############################# ANÁLISIS DE FOURIER #############################
def DFT(values,delta):
	# Recibe como parámetro la serie de tiempo y el delta de sampleo
	nn = len(values)
	dt_ft = (2/nn)*np.abs(np.fft.rfft(values))
	dt_freq = np.fft.rfftfreq(nn,delta)
	# Devuelve un par de arrays, el Primero contiene las frecuencias
	# y el Segundo la amplitud de las frecuencias.
	return [dt_freq, dt_ft]
	
# Efectuamos la transformada de Fourier
dft_ts = DFT(time_series,delta_t)
#-------------------------------------------------------------------
############################# GRAFICA #############################
## Los primeros valores de la DFT opacan al resto. Definimos el número de 
## primeros valores a no-mostrar para poder apreciar los periodos mas pequeños.
no_first = 14
## Los objetos a graficar:
# Periodos
xx = 1/dft_ts[0][no_first:]
# Valores
yy =  dft_ts[1][no_first:]

# Gráfica de la Serie de Tiempo y su Transformada de Fourier
fig, ax = plt.subplots(1,2,figsize=(20, 7))
ax[0].plot(t_sampl, time_series,'b')  
ax[1].plot(xx,yy,'r')
#-------------------------------------------------------------------
ax[0].set_ylabel('Time Series',fontsize=14)
ax[0].set_xlabel('time',fontsize=14)   
ax[1].set_ylabel('DFT Time Series',fontsize=14)
ax[1].set_xlabel('period',fontsize=14)
ax[1].set_xticks([x for x in range(2,15,1)]) 
ax[1].grid()
plt.suptitle('Example of Time Series Fourier Analysis',fontsize=16)
#-------------------------------------------------------------------
plt.tight_layout()
plt.savefig(os.path.join('..','data', 'Fourier_Time_Series.png'), dpi=300)
#-------------------------------------------------------------------
# Notemos que la transformada extrae satisfactoriamente los periodos 
# que elegimos en nuestra función 'time_func'.