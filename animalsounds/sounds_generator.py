# -*- coding: utf-8 -*-
sounds_dict = {"cat": "meow", "dog": "woof", "fish": "..."}


def generator(animal):
    """
       Summary:
            Translates what the sound different animals make
        Args:
            animal (str) – A string of the animal you want to hear, valid options include ‘cat’, ‘dog, ’ and ‘fish’
        Returns:
            A string of the appropriate sound.
    """
    sound = ""
    try:
        sound = sounds_dict[animal.lower()]
    except:
        raise Exception(f"We don’t know what a {animal} sounds like! You could be on to something!")
    return(sound)
