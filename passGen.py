import random
from colorama import Fore,Back,Style
import os
import pyperclip
import time

system=os.name
if system == 'nt': #Detectamos que sistema operativo se está utilizando y borramos el contenido de la terminal.
    os.system("cls")
else:
    os.system("clear")

print(Back.GREEN+Fore.WHITE+Style.BRIGHT+" *** CREEE SU CONTRASEÑA by Borja Escolar Colado. *** "+Back.RESET+Fore.RESET+Style.RESET_ALL+"\n")
print(Back.GREEN+Fore.WHITE+Style.BRIGHT+" ***    LinkedIn: https://acortar.link/1SOBtx     *** "+Back.RESET+Fore.RESET+Style.RESET_ALL+"\n")
letras_minusculas="abcdefghijklmnñopqrstuvwxyz"
letras_mayusculas=letras_minusculas.upper()
simbolos="#^Ç+-*¨~¡áéíóúñüÁÉÍÓÚÑÜºª¢€$¥£%&@+-*/\\|=_[]{}()<>:;,.`¡¿?\/\"'"
numeros="0123456789"

pedirMin=input(Back.WHITE+Fore.BLACK+" ¿Cuántas minúsculas quiere que tenga su contraseña?  "+Back.RESET+Fore.RESET+"\n")
pedirMay=input(Back.WHITE+Fore.BLACK+" ¿Cuántas mayúsculas quiere que tenga su contraseña?  "+Back.RESET+Fore.RESET+"\n")
pedirSim=input(Back.WHITE+Fore.BLACK+" ¿Cuántos símbolos quiere que tenga su contraseña?    "+Back.RESET+Fore.RESET+"\n")
pedirNum=input(Back.WHITE+Fore.BLACK+" ¿Cuántos números quiere que tenga su contraseña?     "+Back.RESET+Fore.RESET+"\n")

#Comprobamos que los valores que introduce el usuario sea un número.
if (pedirMin.isdigit() and pedirMay.isdigit() and pedirSim.isdigit() and pedirNum.isdigit() and pedirMin != "0" and pedirMay != "0" and pedirNum !="0" and pedirSim !="0"): #Si todos son caracteres alfanuméricos
    pedirMin=int(pedirMin) #convertimos a enteros
    pedirMay=int(pedirMay)
    pedirSim=int(pedirSim)
    pedirNum=int(pedirNum)
    suma=pedirMin+pedirMay+pedirSim+pedirNum #realizamos la suma
    if (suma == 0): #Si la suma es igual a 0 es decir si el usuario no ha introducido datos no se puede continuar.
        print("Al menos uno de los valores es cero y no se puede generar la contraseña.")
        time.sleep(1)
    else: #Si es diferente a 0 continuamos con el programa
        contra_min=[] #Arrays para guardar los datos de los for siguientes
        contra_may=[]
        contra_sim=[]
        contra_num=[]
        password=[]
        
        for a in range(pedirMin):
            elemento_min=random.choice(letras_minusculas)
            contra_min.append(elemento_min)

        for b in range(pedirMay):
            elemento_may=random.choice(letras_mayusculas)
            contra_may.append(elemento_may)

        for c in range(pedirSim):
            elemento_sim=random.choice(simbolos)
            contra_sim.append(elemento_sim)

        for d in range(pedirNum):
            elemento_num=random.choice(numeros)
            contra_num.append(elemento_num)

        password=contra_min+contra_may+contra_sim+contra_num #Array con los valores de los arrays llenados con los for anteriores.
        password_final=random.shuffle(password) # Crea eligiendo de forma aleatoria la contraseña a partir de los caracteres de password.
        password_mostrar="".join(password)
        print(Back.MAGENTA+Fore.BLACK+Style.DIM+"  Su contraseña tiene",suma,"caracteres y es:"+Fore.RESET+Back.RESET+Style.RESET_ALL,password_mostrar)
        pregunta=input("\n¿Desea copiar al portapapeles su contraseña?. (s para (sí)): ")
        
        if pregunta.upper() == "S":
            pyperclip.copy(password_mostrar) # Se copia la contraseña generada al portapapeles
            print("Contraseña copiada al portapapeles.")
            time.sleep(1)
        else:
            print("¡Hasta luego!")
            time.sleep(1)
else:
    print("Alguno/s de los valores no son correctos.")

print("PROGRAMA TERMINADO.")
time.sleep(1)
