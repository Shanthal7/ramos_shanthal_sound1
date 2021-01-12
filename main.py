while True:
    if input.sound_level() > 200:
        light.set_all(color.rgb(255, 0, 255))
    else:
        light.clear    