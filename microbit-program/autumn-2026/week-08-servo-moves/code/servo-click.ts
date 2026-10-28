input.onButtonPressed(Button.A, function () {
    angle = Math.min(angle + 30, 180)
    servos.P1.setAngle(angle)
})
input.onButtonPressed(Button.B, function () {
    angle = Math.max(angle - 30, 0)
    servos.P1.setAngle(angle)
})
let angle = 0
servos.P1.setAngle(angle)
