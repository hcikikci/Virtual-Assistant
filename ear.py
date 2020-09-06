# -*- coding: utf-8 -*-
"""
This module listen audio from microphone and convert to the string.
"""

from speech_recognition import Recognizer, Microphone, UnknownValueError, RequestError


class Ear: # pylint: disable=too-few-public-methods
    """
    listen() -- take audio from microphone, recognize it and return as string
    """

    def __init__(self):
        self.recognizer = Recognizer()

    def listen(self):
        """
        listen audio from microphone and convert to the string.
        :return:data
        """
        self.recognizer = Recognizer()
        with Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("I am listening you...")
            audio = self.recognizer.listen(source, phrase_time_limit=6)

        data = ""
        try:
            # Uses the default API key
            # To use another API key:
            # `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            data = self.recognizer.recognize_google(audio, language="tr")
            print("You said : " + data)
        except UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return self.listen()
        except RequestError as exception:
            print("Could not request results from "
                  "Google Speech Recognition service; {0}".format(exception))
            return self.listen()

        return data.lower()
