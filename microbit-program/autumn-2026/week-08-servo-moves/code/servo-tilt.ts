basic.forever(function () {
    servos.P1.setAngle(Math.map(input.acceleration(Dimension.X), -1023, 1023, 0, 180))
    basic.pause(20)
})
