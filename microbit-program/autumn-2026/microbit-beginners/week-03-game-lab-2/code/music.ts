input.onButtonPressed(Button.A, function () {
    music.startMelody(music.builtInMelody(Melodies.BaDing), MelodyOptions.Once)
})
input.onButtonPressed(Button.B, function () {
    music.startMelody(music.builtInMelody(Melodies.JumpUp), MelodyOptions.Once)
})
input.onGesture(Gesture.Shake, function () {
    basic.showIcon(IconNames.EighthNote)
    music.startMelody(music.builtInMelody(Melodies.Nyan), MelodyOptions.Once)
})
