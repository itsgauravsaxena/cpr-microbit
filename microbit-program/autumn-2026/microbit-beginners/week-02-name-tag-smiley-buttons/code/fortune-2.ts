input.onGesture(Gesture.Shake, function () {
    let pick = randint(0, 2)
    if (pick == 0) {
        basic.showIcon(IconNames.Yes)
    } else if (pick == 1) {
        basic.showIcon(IconNames.No)
    } else {
        basic.showIcon(IconNames.Confused)
    }
})
