input.onGesture(Gesture.Shake, function () {
    if (randint(0, 1) == 0) {
        basic.showString("H")
    } else {
        basic.showString("T")
    }
})
