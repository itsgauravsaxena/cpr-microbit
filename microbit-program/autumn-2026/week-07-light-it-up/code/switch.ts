input.onPinPressed(TouchPin.P1, function () {
    basic.showIcon(IconNames.Yes)
    music.playTone(Note.C5, music.beat(BeatFraction.Half))
})
