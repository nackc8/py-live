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

Lista paket just nu:

$ pip list
Package    Version
---------- -------
pip        23.0.1
setuptools 66.1.1

Installera pytest

$ pip install pytest
Collecting pytest
  Using cached pytest-8.3.5-py3-none-any.whl (343 kB)
Collecting iniconfig

$ pip list
Package    Version
---------- -------
iniconfig  2.0.0
packaging  24.2
pip        23.0.1
pluggy     1.5.0
pytest     8.3.5
setuptools 66.1.1

Frys miljön för att kunna använda den senare:

$ pip freeze
iniconfig==2.0.0
packaging==24.2
pluggy==1.5.0
pytest==8.3.5

Spara i en fil, konventionen requirements.txt

pip freeze >requirements.txt

Checka in med git!


[1]: https://docs.python.org/3.11/library/venv.html
