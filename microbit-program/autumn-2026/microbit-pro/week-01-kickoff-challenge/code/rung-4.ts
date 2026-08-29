let score = 0
function addPoints (points: number) {
    score += points
    music.playTone(988, 100)
    basic.showNumber(score)
}
input.onPinPressed(TouchPin.P0, function () {
    addPoints(10)
})
input.onPinPressed(TouchPin.P1, function () {
    addPoints(50)
})
input.onButtonPressed(Button.A, function () {
    score = 0
    basic.showNumber(0)
})
input.onButtonPressed(Button.B, function () {
    score = 0
    basic.showString("GO")
})
