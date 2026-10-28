input.onPinPressed(TouchPin.P2, function () {
    basic.showIcon(IconNames.Happy)
    music.startMelody(music.builtInMelody(Melodies.JumpUp), MelodyOptions.Once)
    for (let index = 0; index < 4; index++) {
        servos.P1.setAngle(30)
        basic.pause(150)
        servos.P1.setAngle(150)
        basic.pause(150)
    }
    servos.P1.setAngle(90)
    basic.clearScreen()
})
servos.P1.setAngle(90)
