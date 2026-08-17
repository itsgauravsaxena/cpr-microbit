# Uge 6 — Radio-multiplayer: sten, saks, papir

> ✊✋✌️ Ryst for at vælge, radio for at sammenligne, og boardet fortæller, hvem der vandt — en hel gruppeturnering i ét program.

**Mål:** send og sammenlign data mellem mange boards, og skriv logikken, der afgør vinderen.

<div style="text-align:center;margin:1.25rem 0;" markdown="0">
<svg width="200" height="200" viewBox="0 0 162 162" role="img" aria-label="sten, saks og papir der skifter" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="162" height="162" rx="20" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<rect x="14" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="126" width="22" height="22" rx="5" fill="#2b3038"/><g fill="#ff4d4d"><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.5s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="1;0;0"/><rect x="42" y="42" width="22" height="22" rx="5"/><rect x="70" y="42" width="22" height="22" rx="5"/><rect x="98" y="42" width="22" height="22" rx="5"/><rect x="42" y="70" width="22" height="22" rx="5"/><rect x="70" y="70" width="22" height="22" rx="5"/><rect x="98" y="70" width="22" height="22" rx="5"/><rect x="42" y="98" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="98" y="98" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.5s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;1;0"/><rect x="14" y="14" width="22" height="22" rx="5"/><rect x="42" y="14" width="22" height="22" rx="5"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="98" y="14" width="22" height="22" rx="5"/><rect x="126" y="14" width="22" height="22" rx="5"/><rect x="14" y="42" width="22" height="22" rx="5"/><rect x="126" y="42" width="22" height="22" rx="5"/><rect x="14" y="70" width="22" height="22" rx="5"/><rect x="126" y="70" width="22" height="22" rx="5"/><rect x="14" y="98" width="22" height="22" rx="5"/><rect x="126" y="98" width="22" height="22" rx="5"/><rect x="14" y="126" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/><rect x="98" y="126" width="22" height="22" rx="5"/><rect x="126" y="126" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.5s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;0;1"/><rect x="14" y="14" width="22" height="22" rx="5"/><rect x="126" y="14" width="22" height="22" rx="5"/><rect x="42" y="42" width="22" height="22" rx="5"/><rect x="98" y="42" width="22" height="22" rx="5"/><rect x="70" y="70" width="22" height="22" rx="5"/><rect x="42" y="98" width="22" height="22" rx="5"/><rect x="98" y="98" width="22" height="22" rx="5"/><rect x="14" y="126" width="22" height="22" rx="5"/><rect x="126" y="126" width="22" height="22" rx="5"/></g></g>
</svg>
</div>

## Hvad I bygger

Ryst for at vælge 0/1/2, send det over radio, sammenlign med modstanderens valg, og vis vundet/tabt/uafgjort.

## Eksempelkode

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 604 183" width="100%" style="max-width:604px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="262" height="32" rx="14" fill="#9857c9"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on shake</text>
<rect x="30" y="55" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set mine to pick random 0 to 2</text>
<rect x="30" y="90" width="262" height="32" rx="7" fill="#2a7fff"/>
<text x="44" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show my icon</text>
<rect x="30" y="125" width="262" height="32" rx="7" fill="#c2185b"/>
<text x="44" y="145.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">radio send number mine</text>
<rect x="322" y="20" width="262" height="32" rx="14" fill="#c2185b"/>
<rect x="332" y="15" width="34" height="12" rx="6" fill="#c2185b"/>
<text x="336" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on radio received</text>
<rect x="322" y="55" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="336" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set theirs to receivedNumber</text>
<rect x="322" y="90" width="262" height="32" rx="7" fill="#59b04a"/>
<text x="336" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">compare and show result</text>
</svg>
</div>

```javascript
let mine = 0
let theirs = 0
radio.setGroup(8)
input.onGesture(Gesture.Shake, function () {
    mine = randint(0, 2)                 // 0 rock, 1 paper, 2 scissors
    if (mine == 0) { basic.showIcon(IconNames.Square) }
    else if (mine == 1) { basic.showIcon(IconNames.Yes) }
    else { basic.showIcon(IconNames.Scissors) }
    radio.sendNumber(mine)
})
radio.onReceivedNumber(function (receivedNumber) {
    theirs = receivedNumber
    basic.pause(500)
    if (mine == theirs) {
        basic.showString("=")
    } else if ((mine + 1) % 3 == theirs) {
        basic.showIcon(IconNames.Sad)     // they beat me
    } else {
        basic.showIcon(IconNames.Happy)   // I win
    }
})
```

## Sessionsplan (60 min + 20 min pause + 30 min)

### Blok 1 — 60 min
- 10 min — opsummér at sende tal over radio
- 25 min — byg ryst-for-at-vælge og send
- 20 min — vinder-logikken: regn `(mine + 1) % 3`-tricket ud sammen
- 5 min — klasseturnering

### ☕ Pause — 20 min
Snacks og løbe rundt. Boards bliver på bordet.

### Blok 2 — 30 min · Vælg dit træk
- 15 min — byt tilfældigt ud med **rigtige valg**: A = sten, B = papir, A+B = saks
- 10 min — klasseturnering, bedst af fem, hold point på tavlen
- 5 min — udvidelse: hvad ville du ændre for at tilføje et fjerde træk?

## ✅ Færdig når
- Et ryst vælger et symbol og sender det.
- Begge spillere ser det rigtige resultat: vundet, tabt eller uafgjort.

## Sådan virker det

Sten (0), papir (1), saks (2) er bare tal, og det gør vinderreglen til ren matematik: **`(mine + 1) % 3 == theirs`** betyder, at *de* slår dig. `%` er 'rest', som får 2 til at rulle tilbage til 0.

## Ekstra udfordringer
- Lad spillerne *vælge* med knapper i stedet for tilfældigt.
- Bedst af fem med løbende pointtal.
- Tilføj en fjerde mulighed (øgle!) og find ud af de nye regler.

## Hvis det ikke virker
- Alle får uafgjort hver gang? I sammenligner jeres egen besked — ignorér beskeder, I selv har sendt.
- Resultatet vises for tidligt? Tilføj en kort `pause`, så begge boards har valgt.

## Links & referencer
- Officielle MakeCode-projekter: <https://makecode.microbit.org/projects>
- micro:bit Foundations lektioner & videoer: <https://microbit.org/projects/make-it-code-it/>
- Blok-reference (slå enhver blok op): <https://makecode.microbit.org/reference>

!!! note "Tilføj dit eget link"
    Fundet en god video eller et MakeCode-projekt til denne uge? Indsæt linket her
    (og læg `.hex`-filen eller delelinket i ugens `code/`-mappe).

## Noter
_(plads til sessionsnoter)_
