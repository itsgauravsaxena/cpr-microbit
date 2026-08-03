# Uge 2 — Programmér grundlæggende pointtælling

**Mål:** et tryk på en knap eller kontakt = **+10 point**, afspil en lyd, og vis pointtallet. Dette er hjertet i hele maskinen.

**Reference:** https://makecode.microbit.org/projects/love-meter og https://makecode.microbit.org/projects/guess for blok-inspiration

## Hvad I bygger
En `score`-variabel, der starter på 0 og stiger med 10, hver gang en bumper (knap/kontakt) rammes, med et bip og tallet vist på LED'erne.

## Eksempelkode
```blocks
on start:
    set score = 0

on button A pressed:          // a bumper / switch is hit
    change score by 10
    play tone (Middle C) for (1/2 beat)
    show number score
```

## Sessionsforløb (60 min)
- 10 min — opsummér variabler
- 40 min — byg programmet: en `score`-variabel, +10 ved tryk, et `music`-bip, vis pointtallet
- 10 min — test i simulatoren, derefter på en rigtig micro:bit med en krokodillenæb-kontakt

## Noter
_(plads til sessionsnoter)_
