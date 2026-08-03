# Uge 4 — Pointtælling med flere sensorer + game over

**Mål:** 2-3 pointzoner med hver sin værdi, en liv/bold-tæller og en **GAME OVER**-skærm.

## Hvad I bygger
Forbind to kontakter/lyssensorer til pin **P1** og **P2** som bumpere med forskellig værdi, tæl ned fra 3 bolde, og rul GAME OVER med slutresultatet.

## Eksempelkode
```blocks
on start:
    set score = 0
    set balls = 3

on pin P1 pressed:            // low bumper
    change score by 10

on pin P2 pressed:            // top bumper — worth more!
    change score by 50

on button A pressed:          // the ball drained out
    change balls by -1
    if balls = 0 then:
        show string "GAME OVER"
        show number score
```

!!! tip "Valgfri udvidelse — radioresultattavle"
    Hurtig gruppe? Brug en **anden micro:bit** som ekstern resultattavle. Spilleplade-boardet radiosender pointtallet; tavle-boardet viser det. Bygger på Gruppe A's *Micro Chat*-idé.

    ```blocks
// --- Playfield micro:bit (sends the score) ---
on start:
    radio set group (1)
on button B pressed:
    radio send number (score)

// --- Scoreboard micro:bit (shows the score) ---
on start:
    radio set group (1)
on radio received (receivedNumber):
    show number (receivedNumber)
```

## Sessionsforløb (60 min)
- 10 min — opsummering
- 40 min — forbind og programmér pointzonerne, tilføj en liv/bold-tæller og GAME OVER-skærmen
- 10 min — test hele pointløkken (og radioresultattavlen, hvis I prøvede den)

## ✅ Færdig når
- De to bumpere (**P1**, **P2**) lægger **forskellige** antal point til.
- Boldtælleren tæller **ned fra 3**.
- Når bolde når **0**, ruller boardet **GAME OVER** og viser slutresultatet.
- *(Valgfri udvidelse)* en anden micro:bit viser pointtallet over radio.

## Noter
_(plads til sessionsnoter)_
