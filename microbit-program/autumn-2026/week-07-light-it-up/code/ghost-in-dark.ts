basic.showIcon(IconNames.Happy)
basic.forever(function () {
    if (input.lightLevel() < 50) {
        basic.showIcon(IconNames.Ghost)
        music.playTone(330, 200)
        music.playTone(247, 400)
    } else {
        basic.showIcon(IconNames.Happy)
        basic.pause(200)
    }
})
