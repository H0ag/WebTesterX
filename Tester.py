#!/usr/bin/env 
from termcolor import colored # Importer la librairie 'therm.colored' pour mettre des couleurs du terminal, c plus joli ;)
I = 'cyan'

print(colored("[i] Importing 'subprocess'", I))
import subprocess

print(colored("[i] Importing 'requests'", I))
import requests

print(colored("[i] Importing 're'", I))
import re

print(colored("[i] Importing 'logging'", I))
import logging

print(colored("[i] Importing 'plaform'", I))
import platform

print(colored("[i] Importing 'time'", I))
import time
      

logging.basicConfig(filename='webtesterx.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')
logger = logging.getLogger()
logger.info('Libraries imported')

def ping(host, time):
    # Parametre pour le nombre de paquets en fonction du système d'exploitation
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, str(time), host]
    result = subprocess.call(command)

    return result

# Creer la classe principal
class Tester():
    # Creer la fonction Connect, elle va permettre d'établir une connexion avec le lien de l'utilisateur, je vais demander à ce que l'user donne son lien, via la variable "link"
    def connectREQUEST(self, link, maxtimeout):
        # Convertir le lien envoyé par l'utilisateur en chaine de caractere
        link = str(link)
        # Verifier avec re, pour savoir s'il y a ecrit http, ou https, au debut du lien de l'user
        match_obj=re.match(r'^(?:http)s?://',link,re.I|re.M)
        # Si oui, alors ne rien toucher
        if(match_obj):
            # Ecrire le lien de l'user en vert
            print(f'url: {colored(link, "green")}')
        # Sinon ajouter "http://" devant le lien de l'user
        else:
            link = "http://"+link
            # Ecrit le lien de l'user en vert
            print(f'url: {colored(link, "green")}')

        try:
            start_time = time.time()
            req = requests.get(link, timeout=int(maxtimeout))
            end_time = time.time()
            response_time = end_time - start_time
            req = req.status_code
            logger.info(f"{link} -- The server is reachable -- Response code: {req}")
        except requests.exceptions.Timeout:
            req = colored(f"The server did not respond within the specified time. [{maxtimeout}s]", 'red')
            logger.error(f"{link} -- The server did not respond within the specified time. [{maxtimeout}s]")
            response_time = "Never"
        
        # Renvoyer le resultat de la requete
        return req, response_time
    
    # Creer la fonction "connectPING" pour établir la connexion au site de l'user en envoyant des pings
    def connectPING(self, link, duration):
        logger.info(f"Using Method PING {duration} times")
        link = str(link)
        # Verifier avec re, pour savoir s'il y a ecrit http, ou https, au debut du lien de l'user
        p = '(?:http.*://)?(?P<host>[^:/ ]+).?(?P<port>[0-9]*).*'
        # Rechercher s'il y a un http, ou https
        p = re.search(p,link)
        # Rechercher l'host
        p = p.group('host')
        # Ecrire l'url
        print(f'url: {colored(p, "green", attrs=["bold"])}')
        print(colored(f"Pinging {link} {duration} times", "yellow"))

        req = ping(p, str(duration))
        if(req == 0):
            logger.info(f"{p} -- Server reachable") 
            print(colored(f"\n{p} -- Server reachable", "green", attrs=['bold']))
        else:
            logger.error(f"{p} -- The server is unreachable")
            print(colored(f"\n{p} -- The server is unreachable", "red", attrs=['bold']))
        return req