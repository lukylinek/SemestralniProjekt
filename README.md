# SemestralniProjekt

# 2D Soccer Game

## Popis
Tento projekt je jednoduchá 2D futbalová hra vytvorená v Pygame. Hráč môže ovládať dvoch hráčov a snažiť sa skórovať proti súperovi. Hra obsahuje brankárov, power-upy a časový limit.

## Požiadavky
Pre spustenie hry je potrebné mať nainštalované:
- Python 3
- Knižnicu Pygame
- Knižnicu Pillow (pre manipuláciu s obrázkami)

### Inštalácia požiadaviek
Spustite nasledovný príkaz:
```
pip install pygame pillow
pip install sys
pip install random
pip install
```

## Spustenie hry
Pre spustenie hry spustite hlavný skript:
```
python PythonApplication1
```

## Herné mechaniky
- **Ovládanie hráčov:**
  - Hráč 1: `WASD`
  - Hráč 2: `Šípky`
- **Power-upy:**
  - Rýchlostný boost pre hráča po nazbieraní power-upu.
- **Brankári:**
  - Automaticky sa pohybujú hore a dole podľa polohy lopty.
- **Časový limit:**
  - Hra má prednastavený čas, po ktorého uplynutí vyhráva tím s vyšším skóre.

## Herné súbory
- `PythonApplication1.py` - hlavný spúšťací skript hry
- `player.py` - trieda hráča
- `goalkeeper.py` - trieda brankára
- `ball.py` - trieda lopty
- `powerup.py` - power-up mechanika
- `variables.py` - premenné a konfigurácie hry

## Autori
des. ček. Lukáš Kumpan
