__author__ = 'Lina Andersson'
import pygame

class Sound:
    def __init__(self, userAnswer):
        self.userAnswer = userAnswer

    #play the sound
    def playSound(self):
        pygame.mixer.init()
        soundEffects = pygame.mixer.Sound(self.userAnswer)
        soundEffects.play()