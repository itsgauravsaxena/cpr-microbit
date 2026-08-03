# Uge 4 — Pointtælling med flere sensorer + game over

**Mål:** 2-3 pointzoner med hver sin værdi, en liv/bold-tæller og en **GAME OVER**-skærm.

## Hvad I bygger
Forbind to kontakter/lyssensorer til pin **P1** og **P2** som bumpere med forskellig værdi, tæl ned fra 3 bolde, og rul GAME OVER med slutresultatet.

## Eksempelkode
<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 580 318" width="100%" style="max-width:580px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="250" height="32" rx="14" fill="#5c8aa8" />
<rect x="40" y="15" width="34" height="12" rx="6" fill="#5c8aa8" />
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on start</text>
<rect x="30" y="55" width="250" height="32" rx="7" fill="#ff8f1a" />
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set score to 0</text>
<rect x="30" y="90" width="250" height="32" rx="7" fill="#ff8f1a" />
<text x="44" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set balls to 3</text>
<rect x="30" y="140" width="250" height="32" rx="14" fill="#9857c9" />
<rect x="40" y="135" width="34" height="12" rx="6" fill="#9857c9" />
<text x="44" y="160.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on pin P1 pressed</text>
<rect x="30" y="175" width="250" height="32" rx="7" fill="#ff8f1a" />
<text x="44" y="195.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">change score by 10</text>
<rect x="30" y="225" width="250" height="32" rx="14" fill="#9857c9" />
<rect x="40" y="220" width="34" height="12" rx="6" fill="#9857c9" />
<text x="44" y="245.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on pin P2 pressed</text>
<rect x="30" y="260" width="250" height="32" rx="7" fill="#ff8f1a" />
<text x="44" y="280.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">change score by 50</text>
<rect x="310" y="20" width="250" height="32" rx="14" fill="#9857c9" />
<rect x="320" y="15" width="34" height="12" rx="6" fill="#9857c9" />
<text x="324" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button A pressed</text>
<rect x="310" y="55" width="250" height="32" rx="7" fill="#ff8f1a" />
<text x="324" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">change balls by -1</text>
<rect x="310" y="90" width="250" height="32" rx="7" fill="#59b04a" />
<text x="324" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">if  balls = 0  then</text>
<rect x="326" y="125" width="234" height="32" rx="7" fill="#2a7fff" />
<text x="340" y="145.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show string &quot;GAME OVER&quot;</text>
<rect x="326" y="160" width="234" height="32" rx="7" fill="#2a7fff" />
<text x="340" y="180.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show number score</text>
<rect x="310" y="125" width="8" height="67" rx="0" fill="#59b04a" />
<rect x="310" y="195" width="250" height="12" rx="6" fill="#59b04a" />
</svg>
</div>

```javascript
let score = 0
let balls = 3
input.onPinPressed(TouchPin.P1, function () {
    score += 10
})
input.onPinPressed(TouchPin.P2, function () {
    score += 50
})
input.onButtonPressed(Button.A, function () {
    balls += -1
    if (balls == 0) {
        basic.showString("GAME OVER")
        basic.showNumber(score)
    }
})
```

!!! tip "Valgfri udvidelse — radioresultattavle"
    Hurtig gruppe? Brug en **anden micro:bit** som ekstern resultattavle. Spilleplade-boardet radiosender pointtallet; tavle-boardet viser det. Bygger på Gruppe A's *Micro Chat*-idé.

    ```javascript
// --- Playfield micro:bit (sends the score) ---
radio.setGroup(1)
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(score)
})

// --- Scoreboard micro:bit (shows the score) ---
radio.setGroup(1)
radio.onReceivedNumber(function (receivedNumber) {
    basic.showNumber(receivedNumber)
})
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
