import os
import pyperclip
import json
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

class Container(BoxLayout):
    # Encrypting to Morse // Шифровка в морзе
    def Encrypt(self):
        lang = self.langSpin.text
        if lang == 'English':
            dictEnc=dictEnEnc
        elif lang == 'Russian':
            dictEnc=dictRuEnc
        elif lang == 'Custom':
            dictEnc=dictCustomEnc
        morseEn = self.morseEn.text
        morseEnB = ''
        # Clear the console // Очистка консоли
        os.system('cls||clear')  
        for i in  morseEn.lower():
            if i in dictEnc:
                morseEnB += dictEnc[i]
        self.morseDec.text = morseEnB
        pyperclip.copy(morseEnB)

        # Decrypting from Morse // Расшифровка из морзе
    def Decrypt(self):
        lang = self.langSpin.text
        if lang == 'English':
            dictDec=dictEnDec
        elif lang == 'Russian':
            dictDec=dictRuDec
        elif lang == 'Custom':
            dictDec=dictCustomDec
        morseDec = self.morseDec.text
        morseWords = morseDec.split(' ')
        morseWords = list(filter(bool, morseWords))
        morseDecB = ''
        # Clear the console // Очистка консоли
        os.system('cls||clear')  
        for i in morseWords:
            if i in dictDec:
                morseDecB += dictDec[i]
        self.morseEn.text = morseDecB
        pyperclip.copy(morseDecB)

class MorseTranslaterApp(App):
    def build(self):
        return Container()

if __name__ == '__main__':
    #Dictionaries // Словари
    dictEnEnc = {'a':'.- ' ,'b':'-... ',
                'c':'-.-. ','d':'-.. ',
                'e':'. ','f':'..-. ',
                'g':'--. ','h':'.... ',
                'i':'.. ','j':'.--- ',
                'k':'-.- ','l':'.-.. ',
                'm':'-- ','n':'-. ',
                'o':'--- ','p':'.--. ',
                'q':'--.- ','r':'.-. ',
                's':'... ','t':'- ',
                'u':'..- ','v':'...- ',
                'w':'.-- ','x':'-..- ',
                'y':'-.-- ','z':'--.. ',
                '0':'----- ','9':'----. ',
                '8':'---.. ','7':'--... ',
                '6':'-.... ','5':'..... ',
                '4':'....- ','3':'...-- ',
                '2':'..--- ','1':'.---- ',
                ' ':'_ '}
    dictRuEnc = {'а':'.- ','б':'-... ',
                'в':'.-- ','г':'--. ',
                'д':'-.. ','е':'. ',
                'ж':'...- ','з':'--.. ',
                'и':'.. ','й':'.--- ',
                'к':'-.- ','л':'.-.. ',
                'м':'-- ','н':'-. ',
                'о':'--- ','п':'.--. ',
                'р':'.-. ','с':'... ',
                'т':'- ','у':'..- ',
                'ф':'..-. ','х':'.... ',
                'ц':'-.-. ','ч':'---. ',
                'ш':'---- ','щ':'--.- ',
                'ъ':'.--.-. ','ы':'-.-- ',
                'ь':'-..- ','э':'...-... ',
                'ю':'..-- ','я':'.-.- ',
                '0':'----- ','9':'----. ',
                '8':'---.. ','7':'--... ',
                '6':'-.... ','5':'..... ',
                '4':'....- ','3':'...-- ',
                '2':'..--- ','1':'.---- ',
                ' ':'_ '}
    #Download custom Dictionary // Загрузка настраиваемого словаря
    if os.path.exists('dict.json'):
        with open('dict.json', 'r') as read_file:
            dictCustomEnc = json.load(read_file)
    else:
        dictCustomEnc = dictEnEnc
    #Generating decrypting dictionaries // Генерация словарей расшифровки
    # English dictionary // Английский словарь
    dictEnEncC = dictEnEnc.copy()
    for k, v in dictEnEncC.items():
        dictEnEncC[k] = v.rstrip()
    dictEnDec = dict(zip(dictEnEncC.values(), dictEnEncC.keys()))
    # Russian dictionary // Русский словарь
    dictRuEncC = dictRuEnc.copy()
    for k, v in dictRuEncC.items():
        dictRuEncC[k] = v.rstrip()
    dictRuDec = dict(zip(dictRuEncC.values(), dictRuEncC.keys()))
    # Custom dictionary // Настраиваемый словарь
    dictCustomEncC = dictCustomEnc.copy()
    for k, v in dictCustomEncC.items():
        dictCustomEncC[k] = v.rstrip()
    dictCustomDec = dict(zip(dictCustomEncC.values(), dictCustomEncC.keys()))
    
    MorseTranslaterApp().run()