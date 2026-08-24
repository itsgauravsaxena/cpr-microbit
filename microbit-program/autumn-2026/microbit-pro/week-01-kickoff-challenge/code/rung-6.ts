radio.setGroup(2)
let score = 0
input.onButtonPressed(Button.A, function () {
    score += 1
    radio.sendNumber(score)
    basic.showNumber(score)
    if (score >= 10) {
        basic.showIcon(IconNames.Yes)
    }
})
radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber >= 10) {
        basic.showIcon(IconNames.No)
    }
})
