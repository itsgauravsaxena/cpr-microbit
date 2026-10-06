basic.showIcon(IconNames.Happy)
basic.forever(function () {
    if (input.lightLevel() < 50) {
        basic.showIcon(IconNames.Ghost)
        pins.digitalWritePin(DigitalPin.P0, 1)
        basic.pause(randint(40, 180))
        pins.digitalWritePin(DigitalPin.P0, 0)
        basic.pause(randint(40, 180))
    } else {
        basic.showIcon(IconNames.Happy)
        pins.digitalWritePin(DigitalPin.P0, 0)
        basic.pause(200)
    }
})
