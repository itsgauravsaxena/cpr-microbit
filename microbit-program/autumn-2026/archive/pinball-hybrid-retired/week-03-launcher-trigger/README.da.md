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

## Sådan affyres bolden

Affyreren skyder bolden op ad **affyringsbanen**; fordi pladen er **vippet**, ruller tyngdekraften den ned igen gennem spillepladen.

**Vip pladen først:** stil bagenden af kabinettet et par centimeter op, så spillepladen hælder ned mod flipperne.

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 360 340" width="100%" style="max-width:340px;height:auto;" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,Segoe UI,sans-serif" role="img" aria-label="Animated diagram of a plunger launching the ball up the lane">
  <!-- launch lane -->
  <rect x="60" y="26" width="44" height="290" rx="16" fill="#123a24" stroke="#1d5637" stroke-width="2"/>
  <!-- launch direction arrow -->
  <g stroke="#6fe0a0" stroke-width="4" fill="none" opacity="0.85" stroke-linecap="round" stroke-linejoin="round">
    <line x1="82" y1="250" x2="82" y2="74"/>
    <polyline points="70,90 82,66 94,90"/>
  </g>
  <!-- ball -->
  <circle cx="82" r="13" fill="#eef3f7" stroke="#9fb0bd" stroke-width="2">
    <animate attributeName="cy" values="256;290;256;58;58;256" keyTimes="0;0.28;0.4;0.62;0.9;1" dur="3s" repeatCount="indefinite"/>
  </circle>
  <!-- plunger (rod + knob) -->
  <g>
    <animateTransform attributeName="transform" type="translate" values="0 0;0 34;0 0;0 0" keyTimes="0;0.28;0.4;1" dur="3s" repeatCount="indefinite"/>
    <rect x="77" y="272" width="10" height="46" fill="#9aa4b2"/>
    <rect x="64" y="314" width="36" height="18" rx="5" fill="#c8a24a"/>
  </g>
  <!-- labels + leaders -->
  <g stroke="#8a94a6" stroke-width="1.5" fill="none">
    <line x1="106" y1="120" x2="150" y2="120"/>
    <line x1="98" y1="256" x2="150" y2="256"/>
    <line x1="102" y1="322" x2="150" y2="322"/>
  </g>
  <g fill="#8a94a6"><circle cx="106" cy="120" r="3"/><circle cx="98" cy="256" r="3"/><circle cx="102" cy="322" r="3"/></g>
  <g font-size="16" font-weight="600" fill="currentColor">
    <text x="158" y="90" fill="#2e9e63">Ball launches up ↑</text>
    <text x="158" y="125">Launch lane</text>
    <text x="158" y="261">Ball (resting)</text>
    <text x="158" y="315">Plunger</text>
    <text x="158" y="335" font-size="13" font-weight="400">pull back &amp; let go</text>
  </g>
</svg>
</div>

**Vælg så en affyrer (simpel → avanceret):**

1. **Gummibånds-plunger** (nemmest, ingen kode) — en lille skubber (en pind, ispind eller 3D-printet tap) i banen med et **gummibånd** bagved. Træk tilbage, slip — *twang!*
2. **Fjeder-plunger** (mest "ægte" flipperfølelse) — en stang + en lille **fjeder** i banen. Børnene kan 3D-designe knoppen i designugerne.
3. **Servo-affyrer** (den *kodede* 🎮) — en **servo**-arm i bunden af banen. Tryk på **knap A**, og den slår bolden op — samme `servoWritePin`-kode som flipperen ovenfor.

!!! tip "Anbefaling"
    Start med **gummibånds-plungeren**, så hver maskine affyrer pålideligt uden kode, og tilbyd så **servo-affyreren** som en "kod det"-opgradering til grupper, der vil have micro:bitten til at affyre.

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
