#!/usr/bin/env 
from Tester import Tester
from termcolor import colored
import os
import argparse
# Efface l'écran de la console
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')


print("""
__        __   _   _____         _             __  __
\ \      / /__| |_|_   _|__  ___| |_ ___ _ __  \ \/ /
 \ \ /\ / / _ \ '_ \| |/ _ \/ __| __/ _ \ '__|  \  / 
  \ V  V /  __/ |_) | |  __/\__ \ ||  __/ |     /  \ 
   \_/\_/ \___|_.__/|_|\___||___/\__\___|_|    /_/\_\                                                      
""")
__version__ = "Stable -- 1.0"
print("\n","-"*50,"\n")
print(colored(f"Developped by Hoag and Eagle_", "green", attrs=['bold']))
print(colored("2nd Systèmes Numériques | Saint Aspais Melun(77)", 'green'))
print(colored(f"Version: {colored(__version__, attrs=['bold'])}", "yellow"))
print("\n","-"*50,"\n")
# Verifier que le fichier est bien le principal,
if "__main__" == __name__:
    # Creer mon agent, qui appelle la classe Tester()
    agent = Tester()
    parser = argparse.ArgumentParser(description='WebTesterX -- Server tester developped by SALLON Maël and MARTIN Amaury')
    
    # Group for --url and --sites-list options
    parser.add_argument_group('TESTS options')
    group1 = parser.add_mutually_exclusive_group(required=True)
    group1.add_argument('--url', type=str, help='The Server to ping')
    group1.add_argument('--list', type=str, help='The list of sites to ping (.txt, separated by returns)')

    # Group for -r and -p options
    parser.add_argument_group('URL argument')
    group2 = parser.add_mutually_exclusive_group(required=True)
    group2.add_argument('-r', action='store_true', help='Trying 1 time to access to the server and get a response code')
    group2.add_argument('-p', type=int, help='Sending pings to the server')
    # Optional argument for -t
    parser.add_argument('-t', type=int, help='Timeout for server response in seconds (Default: 10s)', default=None)

    args = parser.parse_args()

    if args.t and not args.r:
        parser.error("-t is required when -r is specified.")

    if args.t:
        timeout = args.t
    else:
        timeout = 10

    servers = []
    if args.list:
        list_path = args.list
        if not os.path.exists(list_path):
            print("Erreur : le chemin spécifié pour le fichier de liste est invalide.")
            exit()
        if not os.path.isfile(list_path):
            print("Erreur : le chemin spécifié doit être un fichier.")
            exit()
        if not list_path.endswith(".txt"):
            print("Erreur : le fichier de liste doit être au format .txt.")
            exit()

        with open(list_path, "r") as f:
            for line in f:
                servers.append(line.strip())
    else:
        servers.append(args.url)

    if(args.r):
        for i in servers:
            # Appeller la fonction "connectREQUEST" pour etablir une connexion au site de l'user en fesant des requetes
            connection = agent.connectREQUEST(i, timeout)
            response_code, response_time = connection
            if(response_code == 200):
                print(colored('[ok]', 'green', attrs=['bold']), colored(f'[{"{:.2f}".format(response_time)}s]', 'blue'), colored(i, 'yellow'), '--', colored('The website is working well', 'magenta'), '-- Response:', colored(response_code, attrs=['bold']),"\n")
            else:
                print(colored("[!]", 'red', attrs=['bold']), colored(i, 'yellow'), "--", colored("The website isn't working well...", 'red'), "-- Response:", colored(response_code, 'cyan', attrs=['bold']))
    elif(args.p):
        for i in servers:
            # Appeller la foncition "connectPING" pour etablir une connexion au site de l'user par la methode ping
            connection = agent.connectPING(i, args.p)
    else:
        exit(colored("Error...", "red"))