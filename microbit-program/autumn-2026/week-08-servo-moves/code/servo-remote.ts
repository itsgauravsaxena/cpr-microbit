radio.onReceivedNumber(function (receivedNumber) {
    servos.P1.setAngle(receivedNumber)
})
radio.setGroup(8)
servos.P1.setAngle(90)
basic.forever(function () {
    if (input.buttonIsPressed(Button.A)) {
        radio.sendNumber(Math.map(input.acceleration(Dimension.X), -1023, 1023, 0, 180))
        led.plot(2, 2)
    } else {
        led.unplot(2, 2)
    }
    basic.pause(100)
})
