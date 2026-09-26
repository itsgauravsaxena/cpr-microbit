basic.showIcon(IconNames.Heart)
basic.forever(function () {
    led.setBrightness(255)
    basic.pause(400)
    led.setBrightness(40)
    basic.pause(400)
})
