input.onPinPressed(TouchPin.P1, function () {
    pins.digitalWritePin(DigitalPin.P0, 1)
    music.playTone(Note.C5, music.beat(BeatFraction.Half))
    basic.pause(500)
    pins.digitalWritePin(DigitalPin.P0, 0)
})
