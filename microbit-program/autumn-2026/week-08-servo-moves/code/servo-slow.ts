basic.forever(function () {
    for (let index = 0; index <= 36; index++) {
        servos.P1.setAngle(index * 5)
        basic.pause(30)
    }
    for (let index2 = 0; index2 <= 36; index2++) {
        servos.P1.setAngle(180 - index2 * 5)
        basic.pause(30)
    }
})
