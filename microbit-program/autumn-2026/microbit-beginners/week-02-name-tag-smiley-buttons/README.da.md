# Uge 2 — Name Tag + Smiley Buttons

Tryk på en knap, skift humør! 😀 Knap **A** viser et glad ansigt, knap **B** et surt. Din micro:bit har følelser — og *du* bestemmer dem.

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="230" height="230" viewBox="0 0 196 196" role="img" aria-label="en micro:bit der skifter mellem glad og sur" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="196" height="196" rx="22" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<g fill="#2b3038"><rect x="17" y="17" width="26" height="26" rx="6"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="153" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="17" y="153" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/><rect x="153" y="153" width="26" height="26" rx="6"/></g>
<g fill="#ff4d4d"><g><animate attributeName="opacity" calcMode="discrete" dur="1.0s" repeatCount="indefinite" keyTimes="0.0000;0.5000" values="1;0"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/></g><g><animate attributeName="opacity" calcMode="discrete" dur="1.0s" repeatCount="indefinite" keyTimes="0.0000;0.5000" values="0;1"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="17" y="153" width="26" height="26" rx="6"/><rect x="153" y="153" width="26" height="26" rx="6"/></g></g>
</svg>
</div>

**Mål:** grundlæggende om knapper og display, to hurtige tutorials i træk.

**Officielle tutorials:**
- https://makecode.microbit.org/projects/name-tag
- https://makecode.microbit.org/projects/smiley-buttons

## Sessionsplan (60 min + 20 min pause + 30 min)

### Blok 1 — 60 min
- 5 min opsummering af uge 1
- 25 min — Name Tag-tutorial
- 25 min — Smiley Buttons-tutorial
- 5 min — del/test

### ☕ Pause — 20 min
Snacks og løbe rundt. Boards bliver på bordet.

### Blok 2 — 30 min · Bland de to sammen
- 10 min — læg begge programmer på ét board: dit navn ruller, **A** = glad, **B** = sur
- 10 min — tilføj et tredje ansigt på **A+B** (begge knapper på én gang) — vælg et fjollet et
- 5 min — byt board med en makker og prøv hinandens ansigter
- 5 min — 🎉 **Kahoot-quiz** — hele holdet sammen

## Eksempelkode

Kør det her, og klik på **Open & edit in MakeCode** for at lave din egen version:

<!-- Indsæt ugens MakeCode-del-id nedenfor (Share -> Publish giver et link
     som https://makecode.microbit.org/_abc123 -- indsæt id'et eller hele
     linket). Indtil et id er tilføjet, vises en "kommer snart"-note. -->
```makecode
auto
```

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 580 113" width="100%" style="max-width:580px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="250" height="32" rx="14" fill="#9857c9"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button A pressed</text>
<rect x="30" y="55" width="250" height="32" rx="7" fill="#2a7fff"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show icon (happy)</text>
<rect x="310" y="20" width="250" height="32" rx="14" fill="#9857c9"/>
<rect x="320" y="15" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="324" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button B pressed</text>
<rect x="310" y="55" width="250" height="32" rx="7" fill="#2a7fff"/>
<text x="324" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show icon (sad)</text>
</svg>
</div>

```javascript
input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Happy)
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.Sad)
})
```

**Name Tag** (ruller dit navn):

```javascript
basic.forever(function () {
    basic.showString("ALEX")
})
```

!!! tip "▶️ Prøv den i MakeCode (30 sekunder)"
    1. Åbn <https://makecode.microbit.org> → **New Project**
    2. Klik på **`{ } JavaScript`**-knappen øverst
    3. Markér alt i editoren og **slet det**, indsæt derefter **koden ovenfor**
    4. Klik på **Blocks** for at skifte tilbage — de rigtige blokke dukker op, klar til at udforske
    5. **Download** for at lægge den på et board, eller tryk ▶️ for at køre den i simulatoren

    Børnene kan gøre præcis det samme for at komme i gang og derefter ændre tingene, så det bliver deres eget.


## ✅ Færdig når
- Knap **A** viser et glad ansigt, **B** et surt ansigt.
- Name Tag-programmet ruller dit navn hen over LED'erne.

## Noter
_(plads til sessionsnoter)_

## Reference
- Begge tutorials ligger under makecode.microbit.org/projects — samme tutorial-brugerflade som i uge 1
