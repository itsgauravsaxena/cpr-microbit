let score = 0
function addPoints (points: number) {
    score += points
    basic.showNumber(score)
    if (score >= 100) {
        basic.showIcon(IconNames.Yes)
    }
}
input.onPinPressed(TouchPin.P0, function () {
    addPoints(10)
})
input.onPinPressed(TouchPin.P1, function () {
    addPoints(50)
})
input.onPinPressed(TouchPin.P2, function () {
    addPoints(100)
})
input.onButtonPressed(Button.A, function () {
    score = 0
    basic.showNumber(0)
})
input.onButtonPressed(Button.B, function () {
    score = 0
    basic.showString("GO")
})
input.onGesture(Gesture.Shake, function () {
    basic.showString("TILT")
    score = 0
    basic.showNumber(0)
})
