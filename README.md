# Test data creator

## Vad
Ett sätt att skapa testdata i form av personer med Skatteverkets testpersonnummer och namn och adresser som ser realistiska ut.  
Det här är för att visa hur det skulle kunna göras, det är en generell implementation med data som antagligen inte passar nånstans utan modifiering.   

## Varför
Det är jobbigt att sitta och hitta på informationen och skriva in där den skall användas  
En tanke är att de olika  datafältens innehåll skall gå att känna igen som namn, adresser mm.  
Det skulle säkert funka med tex UUID, men då har du ingen aning om ifall förnamn har hamnat i efternamns-fältet.  

## Resultat
en person-post kan se ut så här:
```
{
  "personnummer": "198202142397",
  "first_name": "Katarina",
  "last_name": "Lönn",
  "adress": "Gjuterigatan",
  "gatunummer": "35",
  "postnummer_ort": "522 91 Tidaholm",
  "phone": "0380163594",
  "active": true,
  "start_date": "2019-01-19-155310"
}
```
### Personnummer
Personnumren är avsedda för test. [Läs mer hos Skatteverket](https://www.skatteverket.se/omoss/digitalasamarbeten/omvaraoppnadata/testpersonnummersomoppendata.4.5b35a6251761e6914202df9.html )  
Det finns en lista med 25924 personnummer från 1950 till 2009 i detta repo. Hämta fler och lägg till om du vill ha med äldre eller yngre personer.  
Eftersom personnummer är unika kan du inte skapa fler testpersoner än det finns testpersonnummer i filen.

### Namn
Namn skapas genom att ta ett slumpmässigt förnamn av ca 200 och ett slumpmässigt efternamn av ca 500. De är från SCBs listor över de vanligaste namnen.   

### Adress
Adresser skapas genom att kombinera ett prefix (t.ex "Kungs") med ett suffix (t.ex "vägen") till "Kungsvägen".  
Det kanske blir lite krystat ibland, men det är igenkännligt som en address och du ser om datan hamnat på fel ställe eller om den förändrats.  

Gatunummer är slumpmässigt 1-128  
"postnummer_ort" är riktiga kombinationer, hämtat hos Postnord. 

### Telefonnummer
Telefonnummer är slumpmässigt 0100000000 - 0999999999)  Riktnumret (som det kan vara) matchar inte orten i adressen.


## Se upp!
Eventuell likhet med riktiga personer är slumpmässig. Telefonnummer kan vara riktiga telefonnummer.  

## Kom igång

### Installation och konfiguration
För att prova på UV (som verkar lovande) har jag använt det för att hantera beroenden.  
- Klona detta repo  
- Installera UV https://github.com/astral-sh/uv  
- Har du inte Python 3.12 kan UV installera det.   
- Skapa ett Virtual Environment (venv) i repo-katalogen med `uv venv`  
- Aktivera venv: `source .venv/bin/activate`  
- Installera dependencies med `uv sync` (synkar ditt venv mot innehållet i uv-lock, installerar det du inte har och tar bort sånt som eventuellt inte finns i lock-filen)  

### Kör
- `python main.py` - skapar 10 testpersoner i en jsonlines / ndjson-fil. 
- filer med timestamp sparas i katalogen `output`  
- filerna är i jsonlines-format / ndjson. En json-post per rad.  

### Miljövariabler
Inläsning sker i `src/settings.py`
`NUMBER_OF_PERSONS` styr hur många testpersoner som skapas. Om inget värde anges eller om variablen inte är ett tal används defaultvärdet 10.  
`PRINT`: om resultatet skall skrivas till stdout under körning. Default: True
miljövariabler sätts med `set`på Windows, `export`på Mac/Linux.  
`set NUMBER_OF_PERSONS=25`  (Windows)  
`export NUMBER_OF_PERSONS=25`  (Mac & Linux)  

## Tester
Finns i katalogen tests. Körs med `pytest tests`


## Utöka
Vill du lägga till mer data:  
Lägg till rader i textfilerna i `indata`-katalogen  
Även namn skulle kunna skapas med regler istället för att ha långa listor.  
Christ-ian - er- ina (också med K istället för Ch: Krist-ian - er -ina)  
Efternamn: son-namn eller två natur-termer: Berg-gren  
Dubbelförnamn: Sven-Göran  
Lägg till [snutnamn](https://snutnamn.blogspot.com)  
Hämta fler personnummer från Skatteverket (för andra årskullar än de jag hämtat)  
Lägg till test-Samordningsnummer från Skatteverket.  
Modifiering av vad som ingår i en "person" görs i `create_person`-funktionen i `src/test_data_creator.py`  
epostadresser kan använda `example.com`som domän, [den är gjord för exempel och "finns inte på riktigt"](https://www.iana.org/help/example-domains).
gatunummer kan vara högre än vad jag lagt in i funktionen. Kan din applikation hanetra gatunummer > 999?


## Unikhet
personnummer är unika för varje körning  
All annan data skulle kunna bli duplicerad i flera testpersoner. Att varje mobiltelefon/epostadress hör till en person är bara en konvention och om det inte används för inloggning är det ett bra edge case att testa.

### Formattering och linting
Gjord med `ruff format`respektive `ruff check`

