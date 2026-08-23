input.onGesture(Gesture.Shake, function () {
    let n = randint(0, 3)
    if (n == 0) {
        basic.showIcon(IconNames.Heart)
    } else if (n == 1) {
        basic.showIcon(IconNames.Ghost)
    } else if (n == 2) {
        basic.showIcon(IconNames.Duck)
    } else {
        basic.showIcon(IconNames.Yes)
    }
})
