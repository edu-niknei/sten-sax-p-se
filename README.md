Lektion 1

Vi startade projektet och gjorde en introduktion där spelaren får skriva sitt namn. Vi planerade även vilka funktioner spelet skulle innehålla och skapade en enkel struktur att bygga vidare på.

Problem som uppstod:

Inputs fungerade bara om man skrev exakt likadant som koden förväntade, annars blev det fel.

Lösning:

Vi lade senare till .lower() för att hantera både stora och små bokstäver och för att undvika oväntade fel direkt från början.

Lektion 2

Vi fortsatte med inmatning av antal rundor. Här tränade vi också på felhantering, som är viktigt när användaren kan skriva vad som helst.

Problem som uppstod:

Programmet kraschade om användaren skrev bokstäver istället för siffror.

Spelet kunde starta även om man skrev 0 eller ett negativt tal.

Lösning:

Använde try/except för att fånga ValueError.

Lade till en extra kontroll så endast heltal större än 0 godkänns.
Det gjorde spelet mer stabilt och användarvänligt.

Lektion 3

Vi implementerade själva spelintyget — alltså att spelaren väljer sten, sax eller påse inför varje omgång.

Problem som uppstod:

Om spelaren skrev något fel blev spelet helt förvirrat.

Det var svårt att få loopen att stanna kvar tills ett giltigt val gjorts.

Lösning:

En while-loop används för att repetera frågan tills valet är korrekt.

Ett tydligt felmeddelande lades till för att guida spelaren.

Lektion 4

Denna lektion fokuserade vi på spelets logik och utskrifter för varje omgång — vem vann, förlorade eller om det blev oavgjort.

Problem som uppstod:

Fel spelare vann ibland på grund av ofullständig if-logik.

Det blev svårt att läsa resultatet eftersom utskrifterna inte var strukturerade.

Lösning:

Skrev om alla regler ordentligt och testade olika kombinationer.

Lade till tydligare uppdelning mellan rundorna med linjer och radbrytningar.

Lektion 5

Här lade vi till datorns val och det riktiga poängsystemet. Vi använde random.choice() för att datorn skulle vara slumpmässig.

Problem som uppstod:

Poängen uppdaterades inte som det skulle vid vinster.

Variablerna för poängen låg först på fel plats i koden.

Lösning:

Flyttade poängvariablerna utanför loopen så de inte nollställdes.

Testade många rundor tills poängen räknades korrekt.

Detta var en stor milstolpe eftersom spelet nu gick att spela hela vägen.

Lektion 6

Vi färdigställde slutresultatsdelen av spelet. Tanken var att vinnaren skulle presenteras först, och att spelet avslutas snyggt.

Problem som uppstod:

Utskriften blev konstig när det var oavgjort.

Ordningen spelare/dator växlade inte automatiskt beroende på vem som vann.

Lösning:

En if–elif–else struktur användes för att särskilja vinnarscenarier och oavgjort.

Vi lade även till avslutande text:

“programmet avslutades normalt”
