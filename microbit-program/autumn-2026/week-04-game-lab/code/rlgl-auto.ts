radio.setGroup(3)
basic.forever(function () {
    radio.sendNumber(1)
    basic.showIcon(IconNames.Yes)
    basic.pause(randint(1000, 4000))
    radio.sendNumber(2)
    basic.showIcon(IconNames.No)
    basic.pause(randint(1000, 3000))
})
