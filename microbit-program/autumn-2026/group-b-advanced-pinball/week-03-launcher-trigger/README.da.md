# Uge 3 — Programmér udløseren til affyring/flipper

**Mål:** et knaptryk (eller et tap på accelerometeret) affyrer en **"flip"/"affyring"**-hændelse med lyd + LED-feedback.

## Hvad I bygger
Tryk på knap **B**, og micro:bitten blinker en flipper-figur og spiller en zap-lyd. Har I en servo, så få en rigtig flipper til at svinge.

## Eksempelkode
```blocks
on button B pressed:          // the flipper / launcher
    show leds:
        . . # . .
        . . # # .
        # # # # #
        . . # # .
        . . # . .
    play tone (High C) for (1/4 beat)
    pause (200) ms
    clear screen
```

Got a servo? Make a real flipper move:

```blocks
on button B pressed:
    servo write pin (P0) to (90)
    pause (300) ms
    servo write pin (P0) to (0)
```

## Sessionsforløb (60 min)
- 10 min — opsummering
- 40 min — programmér udløserhændelsen; er der servoer, så forbind en til pin P0 og få en flipper til at bevæge sig (søg "servo" under makecode.microbit.org/projects for referenceblokke)
- 10 min — test

## Noter
Er der ingen servo, kan flippere være simple manuelle/fjedermekanismer — micro:bitten giver blot lyd-/lysfeedback ved udløsning.
