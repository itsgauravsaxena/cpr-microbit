let wasP1 = false
let wasP0 = false
let score = 0
pins.setPull(DigitalPin.P0, PinPullMode.PullUp)
pins.setPull(DigitalPin.P1, PinPullMode.PullUp)
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P0) == 0) {
        if (!(wasP0)) {
            wasP0 = true
            score += 100
            basic.showNumber(score)
        }
    } else {
        wasP0 = false
    }
    if (pins.digitalReadPin(DigitalPin.P1) == 0) {
        if (!(wasP1)) {
            wasP1 = true
            score += 500
            basic.showNumber(score)
        }
    } else {
        wasP1 = false
    }
})
