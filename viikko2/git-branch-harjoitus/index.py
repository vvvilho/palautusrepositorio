from logger import logger #muutos kloonin main haaraan
from summa import summa
from erotus import erotus
from tulo import tulo

logger("aloitetaan ohjelma")

x = int(input("luku 1: ")) #muutos alkuperäiseen main branchiin
y = int(input("luku 2: "))
print(f"{x} + {y} = {summa(x, y)}") 
print(f"{x} - {y} = {erotus(x, y)}") 
print(f"{x} * {y} = {tulo(x, y)}") 

logger("lopetetaan")
print("goodbye!")
