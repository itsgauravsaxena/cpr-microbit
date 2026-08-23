basic.forever(function () {
    let x = Math.map(input.acceleration(Dimension.X), -1000, 1000, 0, 4)
    basic.clearScreen()
    led.plot(Math.round(x), 2)
})
