let score = 0
let catcher = 2
input.onButtonPressed(Button.A, function () {
    catcher = Math.constrain(catcher - 1, 0, 4)
})
input.onButtonPressed(Button.B, function () {
    catcher = Math.constrain(catcher + 1, 0, 4)
})
input.onButtonPressed(Button.AB, function () {
    basic.showNumber(score)
})
basic.forever(function () {
    let star = randint(0, 4)
    for (let row = 0; row <= 4; row++) {
        basic.clearScreen()
        led.plot(catcher, 4)
        led.plot(star, row)
        basic.pause(350)
    }
    if (catcher == star) {
        score += 1
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
    }
    basic.pause(300)
})
