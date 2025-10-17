import colorama
import time
import os
from colorama import Fore, Back, Style


os.system('cls' if os.name == 'nt' else 'clear') # console kitorles
lyrics = open("lyrics.txt", "r", encoding="utf-8")
beolvasva = lyrics.read()
sorszamok = []
szavak = []
mondatok = beolvasva.split("\n")
hossz = len(mondatok)
for i in range(hossz):
    szavak += mondatok[i].split(" ") 
    sorszamok.append(len(mondatok[i].split(" ")))

szavak_hossza = len(szavak)

betuk = []

def run():
    szamlalo = 0 # ezzel nezzuk hol vagyunk
    for x in range(len(sorszamok)): #ennyi sor van osszesen, ennyi space kell
        
        for i in range(sorszamok[x]): # ez az adott sorban vegig megy a szavakon
            for betu in szavak[szamlalo]:
                betuk.append(betu)
                print("\033[1m" + Fore.RED + betu + "\033[0m", end="", flush=True) # ezt a flush = truet a chatgpttol szedtem, mert nem akart mukodni (betunkent irja ki nem soronkent)
                time.sleep(0.06)
            print(" ", end="", flush=True) # kell egy space hogy ne legyen egyben
            szamlalo+=1 # hozzaadom a valtozohoz hogy megvolt az adott szo
            
        print() #ha lefutott a ciklus egy ures sor kell 
run()

debug = True

if debug == True:
    print(mondatok)
    print("--------------------")
    print(szavak)
    print("--------------------")
    print(betuk)
    
def lyrics_easiest_version():
    file = open("lyrics.txt", encoding="utf-8")
    beolvas = file.read()
    for i in beolvas:
        time.sleep(0.1)
        print("\033[1m" + Fore.RED + i + "\033[0m", end="", flush=True) # ezt a flush = truet a chatgpttol szedtem, mert nem akart mukodni (betunkent irja ki nem soronkent)

