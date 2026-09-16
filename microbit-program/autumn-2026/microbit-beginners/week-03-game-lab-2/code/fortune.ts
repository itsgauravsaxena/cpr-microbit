input.onGesture(Gesture.Shake, function () {
    basic.showIcon(IconNames.Asleep)
    basic.pause(500)
    let pick = randint(0, 3)
    if (pick == 0) {
        basic.showIcon(IconNames.Yes)
    } else if (pick == 1) {
        basic.showIcon(IconNames.No)
    } else if (pick == 2) {
        basic.showIcon(IconNames.Confused)
    } else {
        basic.showIcon(IconNames.Happy)
    }
})
