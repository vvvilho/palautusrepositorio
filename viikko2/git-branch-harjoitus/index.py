# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan")

x = int(input("luku 1: ")) # muutos mainissa
y = int(input("luku 2: ")) # muutos mainissa
print(f"{summa(x, y)}")
print(f"{erotus(x, y)}")

logger("lopetetaan")
print("goodbye!")
