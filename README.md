# Programmering i Python – “Live”-exempel

Detta Git-repo innehåller exempel från terminalen och filer för varje lektion. Det är en samlad plats för flera versioner av kursen.

## Lektionsdag

Under din klassmapp finns en katalog för varje lektionsdag. Denna katalog innehåller två viktiga delar:

- **Terminalinspelningar:** En underkatalog `recordings` med inspelningar av allt som skrivs i terminalen under lektionsdagen via **asciinema**.
- **Resten:** De skript/program som vi skapar och kör samt eventuella datafiler kopplade till dem läggs oftast direkt i katalogen.

Se nedan för hur du kan spela upp inspelningarna.

## Att följa med “Live”

Varje lektionsdag får en egen Git-gren där commits automatiskt läggs till och pushas under dagen. För att följa med “live”, checka ut den aktuella grenen genom att köra skriptet `./bin/daystart` på morgonen.

Efter det kan du antingen köra `git pull` i terminalen eller använda din utvecklingsmiljö för att hämta de senaste ändringarna från utbildaren. Kom ihåg att upprepa detta varje gång du vill få de senaste ändringarna.

Vid dagens slut slås förändringarna ihop till en commit som går över till `main`-grenen.

Ett sätt att automatisera uppdateringarna är att t.ex. köra följande i Bash-rad inuti ditt klonade repo:

```bash
while true; do git pull ; sleep 10; done
```

## Att spela upp den inspelade terminalen

Inspelningarna i `recordings/` är gjorda med **asciinema**. Formatet är en fil som slutar på `.cast`.

### Webbläsaren

Kör skriptet `bin/play` från repo-roten:

```bash
python3 bin/play.py
```

Det startar en lokal webbserver och skriver ut en URL, t.ex. `http://localhost:7777/`. Öppna länken i webbläsaren för att enkelt kunna spela upp inspelningarna.

### Terminalen

#### Installera asciinema

Du behöver installera **asciinema**.

##### Linux (Debian/Ubuntu)

```bash
sudo apt update
sudo apt install asciinema
````

##### macOS (Homebrew)

```bash
brew install asciinema
```

##### Windows

Använd **WSL** (Windows Subsystem for Linux), t.ex. Debian/Ubuntu, och följ instruktionerna ovan.

#### Spela upp en inspelning

Gå till repo-roten och kör:

```bash
asciinema play "<klasskatalog>/<lektionskatalog>/recordings/<tid>.cast"
```

#### Justera uppspelningen

##### Ändra hastighet

Spela upp i t.ex. 150 % hastighet:

```bash
asciinema play -s 1.5 "<fil>.cast"
```

##### Pausa och fortsätt

Under uppspelning:

- `Space` – pausa / fortsätt
- `.` – stega fram en frame när pausad

Detta gör att du kan följa i din egen takt direkt i terminalen.

## Filinnehåll

För varje terminalinspelning finns normalt en fil:

- `<tid>.cast`: asciinema-inspelning (terminalens innehåll + timing)
