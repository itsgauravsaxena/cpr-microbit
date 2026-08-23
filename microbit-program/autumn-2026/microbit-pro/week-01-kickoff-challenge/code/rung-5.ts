radio.setGroup(1)
input.onButtonPressed(Button.A, function () {
    radio.sendString("ping")
})
radio.onReceivedString(function (receivedString) {
    basic.showIcon(IconNames.Yes)
    basic.pause(300)
    basic.clearScreen()
})
