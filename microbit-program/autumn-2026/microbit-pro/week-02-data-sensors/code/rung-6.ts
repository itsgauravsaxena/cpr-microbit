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
