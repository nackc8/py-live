#!/usr/bin/env python3

import datetime
import json
import os
import platform
import re
import shutil
import subprocess
import urllib.request
from pathlib import Path
from typing import List
from urllib.error import URLError

fetch_url = "https://raw.githubusercontent.com/nackc8/kursmaterial/refs/heads/main/shared/satt-upp-visual-studio-code.md"

try:
    with urllib.request.urlopen(fetch_url) as response:
        markdown = response.read().decode("utf-8")
except URLError as e:
    raise SystemExit(f"❌ Failed to download setup document: {e}")

bash_block = next(
    (
        m
        for m in re.finditer(r"```bash\n(.*?)```", markdown, re.DOTALL)
        if "code --install-extension" in m.group(1)
    ),
    None,
)

if not bash_block:
    raise ValueError("No bash block with --install-extension lines found")

settings_block = next(
    (
        m
        for m in re.finditer(r"```json\n(.*?)```", markdown, re.DOTALL)
        if '"editor.' in m.group(1)
    ),
    None,
)

if not settings_block:
    raise ValueError("No settings JSON code block found in the document")

keybindings_block = next(
    (
        m
        for m in re.finditer(r"```json\n(.*?)```", markdown, re.DOTALL)
        if all(k in m.group(1) for k in ('"key"', '"command"', '"when"'))
    ),
    None,
)

if not keybindings_block:
    raise ValueError("No keybindings JSON code block found in the document")

extensions: List[str] = []
for line in bash_block.group(1).splitlines():
    line = line.strip()
    if line.startswith("code --install-extension "):
        extensions.append(line.removeprefix("code --install-extension ").strip())

if not extensions:
    raise ValueError("No extensions found in the bash block")

settings: str = settings_block.group(1).strip()

try:
    parsed = json.loads(settings)
except json.JSONDecodeError as e:
    raise ValueError(f"Settings JSON is not well-formed: {e}") from e
if not isinstance(parsed, dict):
    raise ValueError(
        "Settings JSON must be an object at the top level, not a list or other type"
    )

keybindings: str = keybindings_block.group(1).strip()

try:
    parsed_keybindings = json.loads(keybindings)
except json.JSONDecodeError as e:
    raise ValueError(f"Keybindings JSON is not well-formed: {e}") from e
if not isinstance(parsed_keybindings, list):
    raise ValueError(
        "Keybindings JSON must be a list at the top level, not an object or other type"
    )

system = platform.system()
if system == "Windows":
    settings_dir: Path = Path(os.environ["APPDATA"]) / "Code" / "User"
elif system == "Darwin":
    settings_dir = Path.home() / "Library" / "Application Support" / "Code" / "User"
else:  # Linux / other XDG
    config_home = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config"))
    settings_dir = config_home / "Code" / "User"

if shutil.which("code") is None:
    raise SystemExit(
        "❌ 'code' command not found. Make sure VS Code is installed and added to PATH."
    )

print("\n🧩 Extensions")
for ext in extensions:
    print(f"  {ext}...", end="", flush=True)
    result = subprocess.run(
        ["code", "--install-extension", ext],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        shell=(system == "Windows"),
    )
    print(" ✅" if result.returncode == 0 else " ❌")

settings_file = settings_dir / "settings.json"
settings_dir.mkdir(parents=True, exist_ok=True)

print("\n⚙️  Settings")
if settings_file.exists():
    timestamp = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    backup_file = settings_dir / f"settings_{timestamp}_backup.json"
    shutil.copy2(settings_file, backup_file)
    print(f"  📦 Backed up to {backup_file}")
settings_file.write_text(settings, encoding="utf-8")
print(f"  ✅ Written to {settings_file}")

print("\n⌨️  Keybindings")
keybindings_file = settings_dir / "keybindings.json"
if keybindings_file.exists():
    timestamp = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    backup_file = settings_dir / f"keybindings_{timestamp}_backup.json"
    shutil.copy2(keybindings_file, backup_file)
    print(f"  📦 Backed up to {backup_file}")
keybindings_file.write_text(keybindings, encoding="utf-8")
print(f"  ✅ Written to {keybindings_file}")
