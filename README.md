# Test data creator

## Vad
Ett sätt att skapa testdata i form av personer med Skatteverkets testpersonnummer och namn och adresser som ser realistiska ut.  
Det här är för att visa hur det skulle kunna göras, det är en generell implementation med data som antagligen inte passar nånstans utan modifiering.   

## Varför
Det är jobbigt att sitta och hitta på informationen och skriva in där den skall användas  
En tanke är att de olika  datafältens innehåll skall gå att känna igen som namn, adresser mm.  
Det skulle säkert funka med tex UUID, men då har du ingen aning om ifall förnamn har hamnat i efternamns-fältet.  

## Hur
Personnumren är avsedda för test. Läs mer hos Skatteverket: https://www.skatteverket.se/omoss/digitalasamarbeten/omvaraoppnadata/testpersonnummersomoppendata.4.5b35a6251761e6914202df9.html  
Personnummer tas från en lista (drygt 25000 personnummer från 1950 till 2009).   
Adresser skapas genom att kombinera ett prefix (t.ex "Kungs") med ett suffix (t.ex "vägen") till "Kungsvägen".  
Det kanske blir lite krystat ibland, men det är igenkännligt som en address och du ser om datan hamnat på fel ställe eller om den förändrats.  
Namn skapas genom att kombinera 200 förnamn med drygt 500 efternamn, taget från SCBs listor över de vanligaste namnen.  
Gatunummer är slumpmässigt 1-128  
Telefonnummer är slumpmässigt 0100000000 - 0999999999)  
"postnummer_ort" är riktiga kombinationer, hämtat hos Postnord.  


## Se upp!
Eventuell likhet med riktiga personer är slumpmässig. Telefonnummer kan vara riktiga telefonnummer.  

## Kom igång

### Installation och konfiguration
För att prova på UV (som verkar lovande) har jag använt det för att hantera beroenden.  
- Klona detta repo  
- Installera UV https://github.com/astral-sh/uv  
- Har du inte Python kan UV installera det.   
- Skapa ett Virtual Environment (venv) i repo-katalogen med `uv venv`  
- Aktivera venv: `source .venv/bin/activate`  
- Installera dependencies med `uv sync` (synkar ditt venv mot innehållet i uv-lock, installerar det du inte har och tar bort sånt som eventuellt inte finns i lock-filen)  

### Kör
- `python main.py` - skapar 10 testpersoner i en jsonlines / ndjson-fil. Antalet kan styras med miljövariabeln NUMBER_OF_PERSONS (default 10)   
- filer med timestamp sparas i katalogen `output`  
- filerna är i jsonlines-format / ndjson. En json-post per rad.  

## Tester
Finns i katalogen tests. Körs med `pytest tests`


## Utöka
Vill du lägga till mer data:  
Lägg till rader i textfilerna i `indata`-katalogen  
Även namn skulle kunna skapas med regler istället för att ha långa listor.  
Christ-ian - er- ina (också med K istället för Ch: Krist-ian - er -ina)  
Efternamn: son-namn eller två natur-termer: Berg-gren  
Dubbelförnamn: Sven-Göran  
Lägg till snutnamn https://snutnamn.blogspot.com  
Hämta fler personnummer från Skatteverket (för andra årskullar än de jag hämtat)  
Lägg till test-Samordningsnummer från Skatteverket.  
Modifiering av vad som ingår i en "person" görs i `create_person`-funktionen i `src/test_data_creator.py`  


## Unikhet
personnummer är unika för varje körning  
All annan data skulle kunna bli identisk. 

### Formattering och linting
Görs med `ruff format`respektive `ruff check`

