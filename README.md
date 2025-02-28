# Programmering i Python – "Live"

Detta repo innehåller terminalexempel och kodfiler från varje lektion. Det är en gemensam plats för flera kursversioner.

## Lektionsdag

I din klassmapp finns en katalog för varje lektionsdag som innehåller:

- **Kod och filer** (skript, program, data) direkt i lektionskatalogen.
- **Terminalinspelningar** i katalogen `recordings`.

## Följ lektionen "Live"

Varje lektionsdag har en egen Git-gren. Commits läggs till och pushas löpande.

1. Kör `bin/daystart` (från Bash, t.ex. Git Bash på Windows) för att checka ut dagens gren.
2. Använd `git pull` regelbundet för att få in nya ändringar.
   *(Du kan även lägga detta i en loop för kontinuerlig uppdatering:)*

   ```bash
   while true; do git pull; sleep 5; done
   ```

3. Vid dagens slut sammanfogas allt till `main`.

> **Obs!** I Windows fungerar skriptet endast i Git Bash, inte i PowerShell.

## Spela in och spela upp terminalsessioner

### Installation av `script` och `scriptreplay`

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
