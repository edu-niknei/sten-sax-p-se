#importerar random biblioteket
import random

#Här matar man in spelarens namn och antal rundor
print("Hej! Jag är ett Sten Sax Påse program.")
namn = input("Vad heter du? ")
antal = int(input("Hur många rundor vill du spela? ")) 
 
#poängräkning
poang_spelare = 0
poang_puton = 0

#alternativ för spelet
val = ["sten", "sax", "påse"]

#huvudloopen för spelet
for runda in range(antal):
    spelare = input("Välj sten / sax / påse: ").lower()
    while spelare not in val:
        print("Fel! skriv sten, sax eller påse")
        spelare = input("Försök igen: ").lower()

