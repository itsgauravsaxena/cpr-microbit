input.onButtonPressed(Button.B, function () {
    dark = input.lightLevel() / 2
    basic.showIcon(IconNames.Yes)
})
let dark = 0
basic.showIcon(IconNames.Happy)
dark = input.lightLevel()
basic.pause(1000)
dark = input.lightLevel() / 2
basic.forever(function () {
    if (input.buttonIsPressed(Button.A)) {
        basic.showNumber(input.lightLevel())
    } else if (input.lightLevel() < dark) {
        basic.showIcon(IconNames.Ghost)
        pins.digitalWritePin(DigitalPin.P0, 1)
        basic.pause(randint(40, 180))
        pins.digitalWritePin(DigitalPin.P0, 0)
        basic.pause(randint(40, 180))
    } else {
        basic.showIcon(IconNames.Happy)
        pins.digitalWritePin(DigitalPin.P0, 0)
        basic.pause(200)
    }
})
