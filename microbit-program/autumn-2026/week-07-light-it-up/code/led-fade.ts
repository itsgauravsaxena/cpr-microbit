basic.forever(function () {
    for (let index = 0; index <= 20; index++) {
        pins.analogWritePin(AnalogPin.P0, index * 50)
        basic.pause(40)
    }
    for (let index2 = 0; index2 <= 20; index2++) {
        pins.analogWritePin(AnalogPin.P0, 1000 - index2 * 50)
        basic.pause(40)
    }
})
