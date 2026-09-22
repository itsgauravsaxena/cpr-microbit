radio.setGroup(1)
basic.showString("TX")
basic.forever(function () {
    radio.sendNumber(input.acceleration(Dimension.X))
    basic.pause(100)
})
