let wasClosed = false
let score = 0
pins.setPull(DigitalPin.P0, PinPullMode.PullUp)
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P0) == 0) {
        if (!(wasClosed)) {
            wasClosed = true
            score += 100
            basic.showNumber(score)
        }
    } else {
        wasClosed = false
    }
})
