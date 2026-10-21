input.onButtonPressed(Button.A, function () {
    level = Math.max(level - 1, 0)
    pins.analogWritePin(AnalogPin.P0, level * 100)
    basic.showNumber(level)
})
input.onButtonPressed(Button.B, function () {
    level = Math.min(level + 1, 10)
    pins.analogWritePin(AnalogPin.P0, level * 100)
    basic.showNumber(level)
})
let level = 5
pins.analogWritePin(AnalogPin.P0, level * 100)
basic.showNumber(level)
