from funciones import Us_api, Obten_timeline_us, DataInLive
import requests
import tweepy
import time
import json
import os


# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'

if __name__ == "__main__":

#zona de menu


    w = True
    while w:
        print ("""
--------Hola y bienvenido a capturas de twitter--------

Elija la opción que crea conveniente para su estudio

A) Extraer los twits de una cuenta
B) Extraer datos de una palabra en tiempo real
S) Salir

""")

        op= input('->')

        if op=='a' or op=='A':
            Obten_timeline_us()


        if op=='b' or op=='B':
            DataInLive()



#Salir
        if op=='s' or op=='S':
            
            print('\n\nGracias por usar el programa \n\n')
            time.sleep(3)
            w= False
            pass
#Error
        else:
            print('\n\nHa ingresado mal la opción :D \n\n')
            time.sleep(1)

