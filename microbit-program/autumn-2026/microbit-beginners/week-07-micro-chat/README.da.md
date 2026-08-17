# Uge 7 — Micro Chat (radio, del 1 af 2)

📡 To micro:bits, der snakker tværs over rummet — uden ledninger! Send hemmelige beskeder gennem luften, som walkie-talkies.

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="230" height="230" viewBox="0 0 196 196" role="img" aria-label="radiobølger mellem micro:bits" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="196" height="196" rx="22" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<g fill="#2b3038"><rect x="17" y="17" width="26" height="26" rx="6"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="153" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="17" y="153" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/><rect x="153" y="153" width="26" height="26" rx="6"/></g>
<g fill="#ff4d4d"><animate attributeName="opacity" values="1;0.3;1" dur="1.2s" repeatCount="indefinite"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/></g>
</svg>
</div>

**Mål:** to micro:bits, der taler sammen over radio — introduktion til radiobeskeder. Dette er den første af et to-ugers radioprojekt; uge 8 bygger det om til et "find den skjulte beacon"-spil.

**Officiel tutorial:** https://makecode.microbit.org/projects/micro-chat

## Sessionsplan (60 min + 20 min pause + 30 min)

### Blok 1 — 60 min
- 5 min opsummering
- 45 min — Micro Chat-tutorial: to boards sender beskeder til hinanden, introduktion til radiogrupper/-kanaler
- 10 min — dan par og test at sende beskeder på tværs af lokalet

### ☕ Pause — 20 min
Snacks og løbe rundt. Boards bliver på bordet.

### Blok 2 — 30 min · Hemmelige koder
- 15 min — aftal en **hemmelig kode** med din makker (1 = hej, 2 = mød mig, 3 = kig bag dig)
- 10 min — **beskedstafet**: stil jer på række og send en besked fra den ene ende til den anden via radio
- 5 min — hvad sker der, hvis to par bruger samme gruppenummer? prøv det og se

## Eksempelkode

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 580 198" width="100%" style="max-width:580px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="250" height="32" rx="14" fill="#5c8aa8"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#5c8aa8"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on start</text>
<rect x="30" y="55" width="250" height="32" rx="7" fill="#c2185b"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">radio set group 1</text>
<rect x="30" y="105" width="250" height="32" rx="14" fill="#9857c9"/>
<rect x="40" y="100" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="44" y="125.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button A pressed</text>
<rect x="30" y="140" width="250" height="32" rx="7" fill="#c2185b"/>
<text x="44" y="160.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">radio send string &quot;HI&quot;</text>
<rect x="310" y="20" width="250" height="32" rx="14" fill="#c2185b"/>
<rect x="320" y="15" width="34" height="12" rx="6" fill="#c2185b"/>
<text x="324" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on radio received</text>
<rect x="310" y="55" width="250" height="32" rx="7" fill="#2a7fff"/>
<text x="324" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show string (receivedString)</text>
</svg>
</div>

```javascript
radio.setGroup(1)
input.onButtonPressed(Button.A, function () {
    radio.sendString("HI")
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
```

## ✅ Færdig når
- To micro:bits på samme **radiogruppe** kan sende beskeder.
- Et tryk på **A** på den ene får beskeden til at dukke op på den anden.

## Noter
_(plads til sessionsnoter)_

## Reference
- Radiogrupper er som walkie-talkie-kanaler — samme kanalnummer = samme samtale, indstilles i `on start`
- Fortsætter næste uge: [Uge 8 — Heartbeat Beacon](../week-08-heartbeat-beacon/README.md)
