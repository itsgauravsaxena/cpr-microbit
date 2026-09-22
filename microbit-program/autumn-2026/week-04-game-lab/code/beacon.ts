radio.setGroup(1)
basic.showIcon(IconNames.Diamond)
basic.forever(function () {
    radio.sendNumber(1)
    basic.pause(300)
})
