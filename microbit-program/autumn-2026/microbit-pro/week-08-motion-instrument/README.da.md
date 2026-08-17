# Uge 8 — Bevægelsesinstrument

> 🎵 Vip for at ændre tonehøjden — din micro:bit bliver et musikinstrument, du spiller ved at vifte med det.

**Mål:** omsæt en sensorværdi til et andet interval (`map`) — idéen bag næsten alle fede gadgets.

<div style="text-align:center;margin:1.25rem 0;" markdown="0">
<svg width="200" height="200" viewBox="0 0 162 162" role="img" aria-label="en node der hopper" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="162" height="162" rx="20" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<rect x="14" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="126" width="22" height="22" rx="5" fill="#2b3038"/><g fill="#ff4d4d"><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="0.9s" repeatCount="indefinite" keyTimes="0.0000;0.5000" values="1;0"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="98" y="14" width="22" height="22" rx="5"/><rect x="126" y="14" width="22" height="22" rx="5"/><rect x="70" y="42" width="22" height="22" rx="5"/><rect x="70" y="70" width="22" height="22" rx="5"/><rect x="14" y="98" width="22" height="22" rx="5"/><rect x="42" y="98" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="14" y="126" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="0.9s" repeatCount="indefinite" keyTimes="0.0000;0.5000" values="0;1"/><rect x="42" y="14" width="22" height="22" rx="5"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="98" y="14" width="22" height="22" rx="5"/><rect x="42" y="42" width="22" height="22" rx="5"/><rect x="42" y="70" width="22" height="22" rx="5"/><rect x="14" y="98" width="22" height="22" rx="5"/><rect x="42" y="98" width="22" height="22" rx="5"/><rect x="14" y="126" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/></g></g>
</svg>
</div>

## Hvad I bygger

Hold A nede og vip: tonen glider op og ned med vinklen. Tilføj lysniveau som lydstyrke, hvis I vil.

## Eksempelkode

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 312 203" width="100%" style="max-width:312px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="262" height="32" rx="14" fill="#14a3a3"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#14a3a3"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">forever</text>
<rect x="30" y="55" width="262" height="32" rx="7" fill="#59b04a"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">if button A is pressed</text>
<rect x="30" y="90" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="44" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set pitch to map(rotation pitch, -90, 90, 200, 1000)</text>
<rect x="30" y="125" width="262" height="32" rx="7" fill="#d94fb0"/>
<text x="44" y="145.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">play tone (pitch) for 100 ms</text>
<rect x="30" y="160" width="262" height="32" rx="7" fill="#d94fb0"/>
<text x="44" y="180.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">else stop all sounds</text>
</svg>
</div>

```javascript
basic.forever(function () {
    if (input.buttonIsPressed(Button.A)) {
        let pitch = Math.map(input.rotation(Rotation.Pitch), -90, 90, 200, 1000)
        music.playTone(pitch, 100)
    } else {
        music.stopAllSounds()
    }
})
```

## Sessionsplan (60 min + 20 min pause + 30 min)

### Blok 1 — 60 min
- 10 min — hvad gør `map`? (omsætter ét interval til et andet)
- 25 min — byg vippe-thereminen
- 15 min — eksperimentér: ændr intervallet 200–1000, prøv roll i stedet for pitch
- 10 min — minikoncert

### ☕ Pause — 20 min
Snacks og løbe rundt. Boards bliver på bordet.

### Blok 2 — 30 min · Koncert
- 15 min — opgradér dit instrument: lysniveau som lydstyrke, eller lås tonen til en rigtig skala
- 10 min — øv en kort melodi med en makker (én spiller rytme, én spiller melodi)
- 5 min — minikoncert — hvert par optræder i 20 sekunder

## ✅ Færdig når
- At holde A og vippe glider tonehøjden jævnt.
- Slipper man A, stopper lyden.

## Sådan virker det

`map` omregner ét interval til et andet: hældning er −90…90 grader, og vi strækker det ud over 200…1000 Hz. Alle 'smarte' gadgets gør det — tag en sensors interval og omsæt det til noget nyttigt.

## Ekstra udfordringer
- Brug lysniveau som lydstyrke, mens hældning styrer tonehøjden.
- Ram rigtige toner i stedet for en glidende tone (en skala).
- Optag en kort melodi ved at gemme tonerne i en liste.

## Hvis det ikke virker
- Ingen lyd på et V1-board? Sæt en buzzer eller hovedtelefoner på **pin 0** og **GND**.
- Lyden stopper aldrig? Sørg for at `stop all sounds` ligger i `else`-grenen.

## Links & referencer
- Officielle MakeCode-projekter: <https://makecode.microbit.org/projects>
- micro:bit Foundations lektioner & videoer: <https://microbit.org/projects/make-it-code-it/>
- Blok-reference (slå enhver blok op): <https://makecode.microbit.org/reference>

!!! note "Tilføj dit eget link"
    Fundet en god video eller et MakeCode-projekt til denne uge? Indsæt linket her
    (og læg `.hex`-filen eller delelinket i ugens `code/`-mappe).

## Noter
_(plads til sessionsnoter)_
