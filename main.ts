while (true) {
    if (input.soundLevel() >= 150 && input.lightLevel() > 15) {
        light.showAnimation(light.rainbowAnimation, 500) && music.magicWand.playUntilDone()
    } else {
        music.stopAllSounds() && light.setAll(light.rgb(0, 0, 0))
    }
    
}
