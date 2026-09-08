let catcher = 2
input.onButtonPressed(Button.A, function () {
    catcher += -1
})
input.onButtonPressed(Button.B, function () {
    catcher += 1
})
basic.forever(function () {
    basic.clearScreen()
    led.plot(catcher, 4)
    basic.pause(100)
})
