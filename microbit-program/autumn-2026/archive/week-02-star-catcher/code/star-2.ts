let catcher = 2
input.onButtonPressed(Button.A, function () {
    catcher = Math.constrain(catcher - 1, 0, 4)
})
input.onButtonPressed(Button.B, function () {
    catcher = Math.constrain(catcher + 1, 0, 4)
})
basic.forever(function () {
    basic.clearScreen()
    led.plot(catcher, 4)
    basic.pause(100)
})
