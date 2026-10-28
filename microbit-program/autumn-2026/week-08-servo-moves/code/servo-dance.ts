input.onButtonPressed(Button.A, function () {
    music.startMelody(music.builtInMelody(Melodies.Entertainer), MelodyOptions.Once)
    for (let index = 0; index < 4; index++) {
        servos.P1.setAngle(180)
        servos.P2.setAngle(0)
        basic.pause(400)
        servos.P1.setAngle(0)
        servos.P2.setAngle(180)
        basic.pause(400)
    }
    for (let index2 = 0; index2 < 4; index2++) {
        servos.P1.setAngle(180)
        servos.P2.setAngle(180)
        basic.pause(300)
        servos.P1.setAngle(90)
        servos.P2.setAngle(90)
        basic.pause(300)
    }
})
servos.P1.setAngle(90)
servos.P2.setAngle(90)
