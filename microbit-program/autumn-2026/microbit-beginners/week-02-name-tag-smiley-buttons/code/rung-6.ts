input.onGesture(Gesture.Shake, function () {
    let pick = randint(0, 2)
    if (pick == 0) {
        basic.showIcon(IconNames.Square)
    } else if (pick == 1) {
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
})
