let on = false
input.onButtonPressed(Button.A, function () {
    on = !(on)
    if (on) {
        pins.digitalWritePin(DigitalPin.P0, 1)
        basic.showIcon(IconNames.Yes)
    } else {
        pins.digitalWritePin(DigitalPin.P0, 0)
        basic.clearScreen()
    }
})
