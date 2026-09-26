basic.forever(function () {
    led.plot(randint(0, 4), randint(0, 4))
    basic.pause(120)
    led.unplot(randint(0, 4), randint(0, 4))
})
