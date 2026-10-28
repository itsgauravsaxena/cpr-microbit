input.onButtonPressed(Button.A, function () {
    for (let index = 0; index < 6; index++) {
        servos.P1.setAngle(randint(0, 180))
        music.playTone(Note.C5, music.beat(BeatFraction.Sixteenth))
        basic.pause(200)
    }
    servos.P1.setAngle(randint(0, 180))
    music.startMelody(music.builtInMelody(Melodies.BaDing), MelodyOptions.Once)
})
servos.P1.setAngle(90)
