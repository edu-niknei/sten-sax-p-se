#importerar random biblioteket
import random

#Här matar man in spelarens namn och antal rundor
print("Hej! Jag är ett Sten Sax Påse program.")
namn = input("Vad heter du? ")

#Antal rundor + test om val är ett heltal
while True:
    try:
        antal = int(input("Hur många rundor vill du spela? "))
        if antal > 0:
            break
        else:
            print("Skriv ett heltal större än 0")
    except ValueError:
        print("Fel! Du måste skriva ett heltal, Försök igen.")
 
#poängräkning
poäng_spelare = 0
poäng_dator = 0
spelomgång = 1

#alternativ för spelet
val = ["sten", "sax", "påse"]


#huvudloopen för spelet
for runda in range(antal):
    spelare = input(f"spelomgång {spelomgång}\n---------\n Välj sten / sax / påse: ").lower()
    while spelare not in val:
        print("Fel! skriv sten, sax eller påse")
#Datorns val
        spelare = input(f"Välj sten / sax / påse: ").lower()
    dator = random.choice(val)

    #Avgöra vinnare och förlorare
    if spelare == dator:
        print("\noavgjort!\n")
    elif (spelare == "sten" and dator == "sax" or spelare == "sax" and dator == "påse" or spelare == "påse" and dator == "sten" ):
        print(f"\n{namn} är vinnaren av spelomgång {spelomgång}!\n")
        poäng_spelare += 1
    else: 
        print(f"\nDatorn är vinnaren av spelomgång {spelomgång}!\n")
        poäng_dator += 1

    #Räknar spelomgångar
    spelomgång += 1
# Slutresultat – vinnaren skrivs först

if poäng_spelare > poäng_dator:
    print(f"\n{namn} vann spelet!\n")
elif poäng_dator > poäng_spelare:
    print("\nDatorn vann spelet!\n")
else:
    print("\nSpelet är oavgjort.\n")

print("Spelresultat\n=============")
print(f"{namn}: {poäng_spelare}p")
print(f"dator: {poäng_dator}p\n")

print("programmet avslutades normalt")
