while True:
    if input.sound_level() >= 150 and input.light_level() > 15: 
        light.show_animation(light.rainbowAnimation, 500) and music.magic_wand.play_until_done()
    else: 
        music.stop_all_sounds() and light.set_all(light.rgb(0,0,0))
