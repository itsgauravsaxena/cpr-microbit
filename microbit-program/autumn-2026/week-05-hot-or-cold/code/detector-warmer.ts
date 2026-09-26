let last = -128
let strength = -128
radio.setGroup(1)
radio.onReceivedNumber(function (receivedNumber) {
    strength = radio.receivedPacket(RadioPacketProperty.SignalStrength)
})
basic.forever(function () {
    if (strength > last + 3) {
        basic.showArrow(ArrowNames.North)
    } else if (strength < last - 3) {
        basic.showArrow(ArrowNames.South)
    } else {
        basic.showIcon(IconNames.Confused)
    }
    last = strength
    basic.pause(700)
})
