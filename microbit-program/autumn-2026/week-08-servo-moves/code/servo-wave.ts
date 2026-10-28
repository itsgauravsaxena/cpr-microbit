input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Happy)
    for (let index = 0; index < 3; index++) {
        servos.P1.setAngle(45)
        basic.pause(300)
        servos.P1.setAngle(135)
        basic.pause(300)
    }
    servos.P1.setAngle(90)
    basic.clearScreen()
})
servos.P1.setAngle(90)
