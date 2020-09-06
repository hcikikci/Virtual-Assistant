# -*- coding: utf-8 -*-
"""
This module takes string, convert it to human voice and play.
"""
from uuid import uuid4
from pygame import mixer
from gtts import gTTS



class Tongue: # pylint: disable=too-few-public-methods
    """
    This class takes string, convert it to human voice and play.
    """

    def __init__(self):
        mixer.init()

    @classmethod
    def speak(cls, string):
        """
        take the data from another object after that convert it to the audio and play.
        :param string:
        """
        try:
            mixer.music.load(r"Audio/" + string)
            mixer.music.play()
        except: # pylint: disable=bare-except
            filename = str(uuid4()) + ".mp3"
            tts = gTTS(text=string, lang='tr')
            tts.save(r"./delete/" + filename)
            mixer.music.load(r"./delete/" + filename)
            mixer.music.play()
