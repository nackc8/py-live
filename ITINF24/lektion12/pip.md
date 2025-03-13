# Externa beroenden:

- https://pypi.org/ (sök efter beroenden)
- Installeras med t.ex: pip install pytest

# Separat miljö rekommenderas!

Använd modulen [venv][1]:

Skapa en ny miljö i katalogen .venv:

```bash
python -m venv .venv
```

Aktivera miljön för att installera paket i den:

Linux
```bash
source .venv/bin/activate
```
Windows
```powershell
.venv>\Scripts\Activate.ps1
```

https://docs.python.org/3.11/library/venv.html#how-venvs-work


[1]: https://docs.python.org/3.11/library/venv.html
