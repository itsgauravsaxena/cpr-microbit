radio.setGroup(1)
radio.onReceivedNumber(function (receivedNumber) {
    let strength = radio.receivedPacket(RadioPacketProperty.SignalStrength)
    if (strength > -55) {
        basic.showIcon(IconNames.Heart)
    } else if (strength > -75) {
        basic.showIcon(IconNames.Happy)
    } else if (strength > -95) {
        basic.showIcon(IconNames.Confused)
    } else {
        basic.showIcon(IconNames.Sad)
    }
})
