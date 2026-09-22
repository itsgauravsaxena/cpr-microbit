let light = 0
radio.setGroup(3)
radio.onReceivedNumber(function (receivedNumber) {
    light = receivedNumber
    if (light == 1) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
    }
})
input.onGesture(Gesture.Shake, function () {
    if (light == 2) {
        basic.showIcon(IconNames.Skull)
        game.gameOver()
    }
})
