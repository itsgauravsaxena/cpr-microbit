let mine = 0
radio.setGroup(2)
function showThrow (t: number) {
    if (t == 0) {
        basic.showIcon(IconNames.Square)
    } else if (t == 1) {
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
}
input.onGesture(Gesture.Shake, function () {
    mine = randint(0, 2)
    showThrow(mine)
    radio.sendNumber(mine)
})
radio.onReceivedNumber(function (receivedNumber) {
    if (mine == receivedNumber) {
        basic.showString("=")
    } else if (mine == 0 && receivedNumber == 2 || mine == 1 && receivedNumber == 0 || mine == 2 && receivedNumber == 1) {
        basic.showIcon(IconNames.Happy)
    } else {
        basic.showIcon(IconNames.Sad)
    }
})
