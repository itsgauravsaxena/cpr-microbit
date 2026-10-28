basic.forever(function () {
    if (input.lightLevel() < 50) {
        servos.P1.setAngle(0)
        basic.showIcon(IconNames.Asleep)
    } else {
        servos.P1.setAngle(180)
        basic.showIcon(IconNames.Happy)
    }
    basic.pause(500)
})
