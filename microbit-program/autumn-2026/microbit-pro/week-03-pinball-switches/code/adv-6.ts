let wasP9 = false
let wasP8 = false
let score = 0
let balls = 3
function addPoints (points: number) {
    score += points
    music.playTone(988, 100)
    basic.showNumber(score)
}
function loseBall () {
    balls += -1
    if (balls <= 0) {
        basic.showString("OVER")
        basic.showNumber(score)
    } else {
        basic.showString("BALL")
        basic.showNumber(balls)
    }
}
input.onPinPressed(TouchPin.P0, function () {
    addPoints(10)
})
input.onPinPressed(TouchPin.P1, function () {
    addPoints(50)
})
input.onPinPressed(TouchPin.P2, function () {
    loseBall()
})
input.onGesture(Gesture.Shake, function () {
    basic.showString("TILT")
    loseBall()
})
input.onButtonPressed(Button.A, function () {
    score = 0
    basic.showNumber(0)
})
input.onButtonPressed(Button.B, function () {
    score = 0
    balls = 3
    basic.showString("GO")
})
pins.setPull(DigitalPin.P8, PinPullMode.PullUp)
pins.setPull(DigitalPin.P9, PinPullMode.PullUp)
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P8) == 0) {
        if (!(wasP8)) {
            wasP8 = true
            addPoints(100)
        }
    } else {
        wasP8 = false
    }
    if (pins.digitalReadPin(DigitalPin.P9) == 0) {
        if (!(wasP9)) {
            wasP9 = true
            addPoints(500)
        }
    } else {
        wasP9 = false
    }
})
