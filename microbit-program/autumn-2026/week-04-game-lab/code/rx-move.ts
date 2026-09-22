radio.setGroup(1)
let dot = game.createSprite(2, 2)
radio.onReceivedNumber(function (receivedNumber) {
    dot.set(LedSpriteProperty.X, Math.map(receivedNumber, -1023, 1023, 0, 4))
})
