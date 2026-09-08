let score = 0
pins.setPull(DigitalPin.P0, PinPullMode.PullUp)
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P0) == 0) {
        score += 1
        basic.showNumber(score)
    }
})
