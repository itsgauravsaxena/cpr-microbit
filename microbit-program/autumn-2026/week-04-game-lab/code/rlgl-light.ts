radio.setGroup(3)
input.onButtonPressed(Button.A, function () {
    radio.sendNumber(1)
    basic.showIcon(IconNames.Yes)
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(2)
    basic.showIcon(IconNames.No)
})
