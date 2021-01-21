while True:
    print("sound level" + input.sound_level()) and print("light level:" + input.light_level())
    if input.sound_level() > 100:
        light.show_animation(light.rainbowAnimation, 500)
    if input.light_level() > 15:
        music.magic_wand.play_until_done()
else: 
    music.stop_all_sounds() and light.set_all(light.rgb(0,0,0))
