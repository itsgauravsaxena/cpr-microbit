basic.showString("HEJ!")
input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Happy)
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.Sad)
})
input.onButtonPressed(Button.AB, function () {
    basic.showIcon(IconNames.Heart)
})
input.onGesture(Gesture.Shake, function () {
    let n = randint(0, 3)
    if (n == 0) {
        basic.showIcon(IconNames.Happy)
    } else if (n == 1) {
        basic.showIcon(IconNames.Sad)
    } else if (n == 2) {
        basic.showIcon(IconNames.Surprised)
    } else {
        basic.showIcon(IconNames.Silly)
    }
})
