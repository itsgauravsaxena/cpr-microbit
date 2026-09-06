let score = 0
input.onPinPressed(TouchPin.P0, function () {
    score += 10
    basic.showNumber(score)
})
input.onButtonPressed(Button.A, function () {
    score = 0
    basic.showNumber(0)
})
