basic.forever(function () {
    pins.digitalWritePin(DigitalPin.P0, randint(0, 1))
    pins.digitalWritePin(DigitalPin.P1, randint(0, 1))
    pins.digitalWritePin(DigitalPin.P2, randint(0, 1))
    basic.pause(150)
})
