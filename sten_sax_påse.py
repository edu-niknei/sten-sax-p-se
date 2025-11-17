#importerar random biblioteket
import random

#Här matar man in spelarens namn och antal rundor
print("Hej! Jag är ett Sten Sax Påse program.")
namn = input("Vad heter du? ")
antal = int(input("Hur många rundor vill du spela? ")) 
 
#poängräkning
poäng_spelare = 0
poäng_dator = 0

#alternativ för spelet
val = ["sten", "sax", "påse"]

#huvudloopen för spelet
for runda in range(antal):
    spelare = input("Välj sten / sax / påse: ").lower()
    while spelare not in val:
        print("Fel! skriv sten, sax eller påse")
        spelare = input("Försök igen: ").lower()
dator = random.choice(val)

#Avgöra vinnare och förlorare
if spelare == dator:
    print("oavgjort!")
elif (spelare == "sten" and dator == "sax" or spelare == "sax" and dator == "påse" or spelare == "påse" and dator == "sten"):
    print(f"{namn} Vann rundan!")
    poäng_spelare += 1
else: 
    print("Datorn vann rundan!")
    poäng_dator += 1
