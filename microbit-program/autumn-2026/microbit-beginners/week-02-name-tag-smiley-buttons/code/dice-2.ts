input.onGesture(Gesture.Shake, function () {
    let roll = randint(1, 6)
    if (roll == 6) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showNumber(roll)
    }
})
