basic.forever(function () {
    servos.P1.setAngle(0)
    basic.pause(1000)
    servos.P1.setAngle(180)
    basic.pause(1000)
})
