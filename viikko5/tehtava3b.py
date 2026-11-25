import random
import time

print("Katsotaan oletko onnekas")
time.sleep(3)

if random.random() > 0.5:
    print("Onnea voitit")
else:
    print("ePäonnea hävisit")
