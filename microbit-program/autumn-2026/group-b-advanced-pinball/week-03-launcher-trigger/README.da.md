# Uge 3 — Programmér udløseren til affyring/flipper

**Mål:** et knaptryk (eller et tap på accelerometeret) affyrer en **"flip"/"affyring"**-hændelse med lyd + LED-feedback.

## Hvad I bygger
Tryk på knap **B**, og micro:bitten blinker en flipper-figur og spiller en zap-lyd. Har I en servo, så få en rigtig flipper til at svinge.

## Eksempelkode
<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 300 203" width="100%" style="max-width:300px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="250" height="32" rx="14" fill="#9857c9" />
<rect x="40" y="15" width="34" height="12" rx="6" fill="#9857c9" />
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button B pressed</text>
<rect x="30" y="55" width="250" height="32" rx="7" fill="#2a7fff" />
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show leds</text>
<rect x="248" y="61" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="253" y="61" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="258" y="61" width="4" height="4" rx="1" fill="#ffffff" />
<rect x="263" y="61" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="268" y="61" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="248" y="66" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="253" y="66" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="258" y="66" width="4" height="4" rx="1" fill="#ffffff" />
<rect x="263" y="66" width="4" height="4" rx="1" fill="#ffffff" />
<rect x="268" y="66" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="248" y="71" width="4" height="4" rx="1" fill="#ffffff" />
<rect x="253" y="71" width="4" height="4" rx="1" fill="#ffffff" />
<rect x="258" y="71" width="4" height="4" rx="1" fill="#ffffff" />
<rect x="263" y="71" width="4" height="4" rx="1" fill="#ffffff" />
<rect x="268" y="71" width="4" height="4" rx="1" fill="#ffffff" />
<rect x="248" y="76" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="253" y="76" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="258" y="76" width="4" height="4" rx="1" fill="#ffffff" />
<rect x="263" y="76" width="4" height="4" rx="1" fill="#ffffff" />
<rect x="268" y="76" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="248" y="81" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="253" y="81" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="258" y="81" width="4" height="4" rx="1" fill="#ffffff" />
<rect x="263" y="81" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="268" y="81" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="30" y="90" width="250" height="32" rx="7" fill="#d94fb0" />
<text x="44" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">play tone High C</text>
<rect x="30" y="125" width="250" height="32" rx="7" fill="#2a7fff" />
<text x="44" y="145.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">pause 200 ms</text>
<rect x="30" y="160" width="250" height="32" rx="7" fill="#2a7fff" />
<text x="44" y="180.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">clear screen</text>
</svg>
</div>

```javascript
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        . . # . .
        . . # # .
        # # # # #
        . . # # .
        . . # . .
        `)
    music.playTone(Note.C5, music.beat(BeatFraction.Quarter))
    basic.pause(200)
    basic.clearScreen()
})
```

Got a servo? Make a real flipper move:

```javascript
input.onButtonPressed(Button.B, function () {
    pins.servoWritePin(AnalogPin.P0, 90)
    basic.pause(300)
    pins.servoWritePin(AnalogPin.P0, 0)
})
```

## Sessionsforløb (60 min)
- 10 min — opsummering
- 40 min — programmér udløserhændelsen; er der servoer, så forbind en til pin P0 og få en flipper til at bevæge sig (søg "servo" under makecode.microbit.org/projects for referenceblokke)
- 10 min — test

## ✅ Færdig når
- Et tryk på **B** blinker en flipper-figur og spiller en lyd.
- Skærmen ryddes bagefter, klar til næste flip.
- *(Med en servo)* svinger flipperen fysisk ud og tilbage igen.

## Noter
Er der ingen servo, kan flippere være simple manuelle/fjedermekanismer — micro:bitten giver blot lyd-/lysfeedback ved udløsning.
