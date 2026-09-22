let score = 0
input.onPinPressed(TouchPin.P1, function () {
    score += 1
    basic.showIcon(IconNames.Happy)
    music.startMelody(music.builtInMelody(Melodies.JumpUp), MelodyOptions.Once)
    basic.showNumber(score)
})
