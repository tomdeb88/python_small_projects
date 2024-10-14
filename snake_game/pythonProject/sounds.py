from pygame import mixer
mixer.init()


class Sound:
    def game_over(self):
        sound_effect=mixer.Sound("sounds/game_over.wav")
        sound_effect.play()

    def eating_sound(self):
        sound_effect=mixer.Sound("sounds/eating.wav")
        sound_effect.play()
