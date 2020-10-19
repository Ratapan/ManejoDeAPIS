from key_setings import API_key, API_key_secret, Bearer_token, Access_token, Access_token_secret
import datetime
import tweepy
import time
import json
import os

def Us_api():
    cons_key       = API_key()
    cons_key_secre = API_key_secret()
    acc_tok        = Access_token()
    acc_tok_sec    = Access_token_secret()

    auth = tweepy.OAuthHandler(cons_key, cons_key_secre)
    auth.set_access_token(acc_tok, acc_tok_sec )
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    return api

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

def datefile():

    a    = datetime.datetime.now()
    d    = a.day
    m    = a.month
    agno = a.year

    dia = SCD(d) 
    mes = SCM(m)

    date_now = (f'{agno}{mes}{dia}')

    return date_now


def Imprimir(li,tipo, t,us):

    fecha = datefile()
    file = open(f"Captura_de_twits\\{tipo}_Day_{fecha}_{us}_{t}.json", "w")     
    file.write(li)
    file.close

def ImprimirInLive(inf,tipo,clave):

    fecha = datefile()
    file = open(f"Captura_de_twits\\{tipo}_Day_{fecha}_{clave}.txt", "a",encoding='utf-8') 
    file.write( f'\n{inf}')
    file.close

def Obten_timeline_us():

    api= Us_api()
    iteracion=0
    tipo= 'Tml_usr'#time line usuario
    lista= []
    w= True

    while w:
        print('\n\nIndique el nombre de la cuenta')
        usr= input('->')

        if len(usr) >2 and len(usr) <16:
            while w:
                print('\n\nNumero de twitts a extraer')
                num= int(input('->'))
                if num > 0:

                    for tweet in tweepy.Cursor(api.user_timeline, screen_name=usr, tweet_mode="extended").items(num):
                        lista= (json.dumps(tweet._json,  indent=4))

                        iteracion= iteracion+1
                        li= "".join(lista)
                        Imprimir(li,tipo,iteracion,usr)

                    print (lista)
                    
                    print('\n\nListo!!! busqulo en la carpeta de capturas\n\n')
                    time.sleep(1)
                    w= False

                else:
                    print('El numero tiene que ser mayor a 0')
                    pass
                
            



        elif len(usr) >=16 or usr== 'twitter' or usr=='admin':
            print('\n\nError al ingresar el nombre de usuario: el nombre de usuario no puede superar los 15 caracteres, tampoco ser Twitter o Admin')
            pass
        else:
            print('\n\nError al ingresar el nombre de usuario')
            pass

def DataInLive():

    
    class TweetsListener(tweepy.StreamListener):
        it= 1
        def on_connect(self):
            print("Conexión exitosa!")

        def on_status(self, status):
            print(status.text)
            st= status.text
            ImprimirInLive(st,tipo,clave)


        def on_error(self, status_code):
            print("Error", status_code)



    print('Que palabra desea trakear?')
    clave= input('->')
    tipo= 'TrackReal'


    fecha = datefile()
    file = open(f"Captura_de_twits\\{tipo}_Day_{fecha}_{clave}.txt", "w") 
    file.write('')
    file.close


    api= Us_api()
    stream = TweetsListener()
    streamingApi = tweepy.Stream(auth=api.auth, listener=stream)
    streamingApi.filter(track=[f"{clave}"],locations=[-78.4660873375,-55.3456890411,-64.2224872201,-16.6508411759])
    #,locations=[-78.4660873375,-55.3456890411,-64.2224872201,-16.6508411759]