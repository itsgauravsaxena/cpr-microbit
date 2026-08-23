input.onGesture(Gesture.Shake, function () {
    let choice = randint(0, 2)
    if (choice == 0) {
        basic.showIcon(IconNames.Square)
    } else if (choice == 1) {
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
