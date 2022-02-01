from gettext import translation
from googletrans import Translator

def translate(text):
    translator = Translator()
    #translate text with destination language as German
    translation = translator.translate(text=text,dest='de')
    return translation.text