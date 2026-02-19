# Variabler och typer

Vi använder Python REPL för att experimentera. Den startas genom att
bara skriva:

```bash
python3
```

Vi använder:

- `print(s)` - skriver ut texten s till stdout
- `type(t)`  - skriver ut typen på t

Variabel:
    - Ett lagrat värde i datorns minne
    - Namn (identifier i Python Language för hur det kan vara skrivet)

Typer:
    - sträng: text eller mening, som iofs kan innehålla siffror... som text
    - int: heltal, både positiva och negativa och noll
    - float: flyttal, decimaltal så gott en dator kan representera sådana
      - har avrundningsfel, ej lämpligt för pengar
      - lämplig för koordinater i 3d
    - boolean: True eller False - inget annat
    - list: en sekvens [ 12, 88, "Hej", 3.5 ]
      - blandat = [ 12, 88, "Hej", 3.5 ]
        blandat[2] ---> "Hej"
      - Index fås med hakparanteser och position som börjar med noll
      - printa med: print(blandat)
    - range(siffra)
      - Får man en sekvens med numren 0 .. siffra:n
      - Skriver ut sig som en sträng enligt: range(0, 7)
    - se vilken typ något är: type(x)
Typkonvertering:
    Exempel:
        list(range(5))
             ^^^^^^^^  en range, som vi skickar in i en list(..)
        ^^^^^^^^^^^^^^ en lista som ges tillbaka av list-funktionen

Operatorer:
    - Gör saker med värden, de "opererar" på dem
    - Vanliga: + - / *(gånger är*)
    - 1 + 2 ----> 3
    - Division till heltal, kastar decimaldelen i soporna: 10 // 3
    - % modulo, ger tillbaka resten vid division: 3 % 2 ---> 1

Conditional logic

    Operatorer som utvärderar/jämför och resulterar i True eller False

    Nedanstående tar ett värde till vänster och ett till höger
        >
        <
        >=
        <=
        ==
