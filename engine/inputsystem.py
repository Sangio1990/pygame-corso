import pygame


class InputSystem:
    def __init__(self):
        self.observers = {}

    def bindToKeyboard(self, key, function):
        if function is not None:
            # bind a single function to multiple keys
            self.observers[key] = function

    def process(self):
        keyboardEvents = pygame.key.get_pressed()

        # every single key is mapped here, with a boolean set to True for those keys that were pressed
        for key, function in self.observers.items():
            if keyboardEvents[key]:
                function(key)
