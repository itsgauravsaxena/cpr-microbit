radio.setGroup(1)
basic.showString("RX")
radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        basic.showArrow(ArrowNames.West)
    } else if (receivedNumber == 2) {
        basic.showArrow(ArrowNames.East)
    } else {
        basic.showIcon(IconNames.Surprised)
    }
})
