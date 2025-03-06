# Programmering i Python – "Live"

Detta Git-repo innehåller exempel från terminalen och filer för varje lektion där sådant förekommit. Det är en samlad plats för flera versioner av kursen.

## Lektionsdag

I din klassmapp finns en katalog för varje lektionsdag som innehåller:

- **Kod och filer** (skript, program, data) direkt i lektionskatalogen.
- **Terminalinspelningar** i katalogen `recordings`.

## Följ lektionen "Live"

Varje lektionsdag får en egen Git-gren där commits automatiskt läggs till och pushas under dagen. För att följa med "live", checka ut den aktuella grenen genom att köra Bash-skriptet `bin/daystart` på morgonen. Om du använder Windows kan du köra skriptet från "Git Bash" men tyvärr inte från PowerShell.

1. Vid dagens slut sammanfogas allt till `main`.

Om du vill få de senase ändringarna kontinuerligt så kan du t.ex. använda en liten loop som kör git pull var 5:e sekund:

    ```
    while true; do git pull; sleep 5; done
    ```

Vid dagens slut slås förändringarna ihop till en commit som går över till `main`-grenen.

## Att spela upp eller se inspelade terminalen terminalsessioner

### "Videoinspelning" och uppspelning av terminalen

- **Linux:** Finns ofta redan installerat. Annars:

  ```bash
  sudo apt-get install util-linux
  ```

- **macOS:** Inbyggt på många versioner. Om du saknar det, installera via Homebrew:

  ```bash
  brew install util-linux
  ```

- **Windows:** Använd Git Bash eller WSL (Windows Subsystem for Linux) där `script`/`scriptreplay` fungerar som i Linux. Alternativt kan du använda Cygwin.

### Inspelningsfiler

Vid inspelning resulterar i tre filer:

1. `<tid>_cleaned.txt` (syns först en stund efter avslutad session)
2. `<tid>.txt`
3. `<tid>_timing.txt`

### Uppspelning

1. **Visa filinnehållet (rå text)**

   ```bash
   cat "<tid>.txt"
   ```

   Detta visar all text, inklusive färgkoder.

2. **Realtidsuppspelning**

   ```bash
   scriptreplay "<tid>_timing.txt" "<tid>.txt"
   ```

3. **Snabbare uppspelning (t.ex. 150%)**

   ```bash
   scriptreplay -d 1.5 --timing "<tid>_timing.txt" "<tid>.txt"
   ```

4. **Begränsa långa pauser (max 2 sek)**

   ```bash
   scriptreplay -m 2 --timing "<tid>_timing.txt" "<tid>.txt"
   ```

Nedan är en förkortad version utan rådet om Windows-genvägar:

## Mjuka länkar (symlinks) från datumkataloger till `KLASS/lektionN`

I `date/dYYMMDD` finns mjuka länkar (symlinks) som pekar på `KLASS/lektionN`. Dessa är redan skapade av utbildaren och versionerade i Git.

### Linux och macOS

- **Fungerar direkt** när du kör `git pull`.

### Windows

Git kan checka ut symlinks på olika sätt, beroende på din konfiguration:

1. **Riktiga symlinks**
   - Aktivera "Developer Mode" (Inställningar → Uppdatering och säkerhet → För utvecklare).
   - Ställ in i Git:

     ```bash
     git config core.symlinks true
     ```

   - Nu hanteras symlinks som faktiska länkar i Windows.

2. **Textfiler**
   - Om Developer Mode inte är aktivt skapas länkarna som små textfiler som visar sökvägen, men beter sig inte som länkar i Explorer.

3. **Windows Subsystem for Linux (WSL)**
   - Använder du WSL och arbetar i WSL:s filsystem (t.ex. `/home/...`) fungerar symlinks som i Linux/macOS.
