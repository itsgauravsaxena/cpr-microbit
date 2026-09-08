input.onGesture(Gesture.Shake, function () {
    if (randint(0, 1) == 0) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
    }
})
