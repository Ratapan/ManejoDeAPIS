#! python3
from fecha import date, datefile
from fecha import hr
import requests 
import time
import os


#si marca error por no encontrarlo tiene que instalar el paquete poniendo:'pip install requests' en el cmd

if __name__ == "__main__":


   f_url = date()#llamada a fecha con el formato exacto actual
   f_file= datefile()
   hora  = hr()


#r_act = (os.getcwd())
   r_n   = os.getcwd()
   url = 'http://api.mercadopublico.cl/servicios/v1/publico/licitaciones.json'
   agrs = {'fecha':f_url,'ticket':'BB6C695D-5ECF-4DA3-961A-594E3FF2E5E9'}

   response = requests.get(url, params=agrs)
   cont = response.content#guardo el contenido de la pagina

   file = open(f"Capturas\\Day_{f_file}_hr_{hora}.json", "wb")     
   file.write(cont)
   file.close

   time.sleep(0.5)
   input("Todo salio bien!!! Enter para salir")
   time.sleep(1)


