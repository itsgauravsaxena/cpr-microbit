basic.forever(function () {
    for (let index = 0; index <= 4; index++) {
        servos.P1.setAngle(index * 45)
        music.playTone(Note.C5, music.beat(BeatFraction.Sixteenth))
        basic.pause(500)
    }
})
