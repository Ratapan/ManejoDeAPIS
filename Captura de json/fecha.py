import datetime
from datetime import timedelta
import time


def menu():
    men =True
    while men:
        now = datetime.datetime.now()#Extraigo la fecha del día Ej: 3 09 2020
        print("""
        Hola! Desea extraer datos del día de: 
        
        A) Hoy 
        B) Ayer 
        C) Hace x días atrás

        """)
        op = input('->')

        if op=='a' or op=='A':
            
            return now #Extraigo la fecha del día Ej: 3 09 2020 y lo retorno

        elif op=='b' or op=='B':
            
            ayer = now - timedelta(days = 1)#resto un dia
            return ayer #retorno el resultado

        elif op=='c' or op=='C':

            dsms = int(input('Indique el numero de días que el quiere restar a la fecha actual \n\n->'))#dias menos
            new_date = now - timedelta(days = dsms) #resto el numero de dias
            return new_date
        else:
            print('\n\n<---Error en el ingreso de datos--->\n\n')
            time.sleep(1)
            pass


def SCD(d): #suma 0 en el principio de un dia en caso de que este sea menor a 10
    if d < 10:

        di = (f'0{d}')
        return di

    else:
        return d
def SCM(m): #suma 0 en el principio de un mes en caso de que este sea menor a 10
    if m < 10:

        me = (f'0{m}')
        return me

    else:
        return m
 


def date():

    a    = menu()
    d    = a.day
    m    = a.month
    agno = a.year

    #retorno de valores de SCD y SCM (sumas de 0 en caso de ser necesario)
    dia = SCD(d) 
    mes = SCM(m)

    date_now = (f'{dia}{mes}{agno}')

    return date_now #esta funcion se encargara de retornar la fecha en el formato para la url

def hr(): #retorna un formato de hora para el guardado del archivo
   
    a   = datetime.datetime.now()
    hor = (f'{a.hour}_{a.minute}')
    return hor