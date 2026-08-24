input.onButtonPressed(Button.A, function () {
    let ticks = randint(5, 12)
    for (let i = 0; i < ticks; i++) {
        basic.showIcon(IconNames.Heart)
        basic.pause(300)
        basic.clearScreen()
        basic.pause(150)
    }
    basic.showIcon(IconNames.Skull)
})
