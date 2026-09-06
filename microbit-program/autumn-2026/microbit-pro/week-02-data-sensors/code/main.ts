let score = 0
input.onPinPressed(TouchPin.P0, function () {
    score += 10
    basic.showNumber(score)
})
