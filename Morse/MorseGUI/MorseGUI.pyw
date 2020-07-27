import sys
import json
import pyperclip
from PyQt5 import QtWidgets, uic, QtGui, QtCore

def main():
    win.buttonEnc.clicked.connect(Encrypt)
    win.buttonDec.clicked.connect(Decrypt)

#Encrypting to Morse // Шифровка в морзе
def Encrypt():
    if win.comboLang.currentText() == 'English':
        dictEnc=dictEnEnc
    elif win.comboLang.currentText() == 'Russian':
        dictEnc=dictRuEnc
    elif win.comboLang.currentText() == 'Custom':
        dictEnc=dictCustomEnc
    morseEn = win.textEnc.toPlainText()
    morseEnlow = morseEn.lower()
    morseEnB = ''
    for i in morseEnlow:
        morseEnB += dictEnc[i]
    win.textDec.setPlainText(morseEnB)
    pyperclip.copy(morseEnB)

#Decrypting from Morse // Расшифровка из морзе
def Decrypt():
    if win.comboLang.currentText() == 'English':
        dictDec=dictEnDec
    elif win.comboLang.currentText() == 'Russian':
        dictDec=dictRuDec
    elif win.comboLang.currentText() == 'Custom':
        dictDec=dictCustomDec
    morseDec = win.textDec.toPlainText()
    morseWords = morseDec.split(' ')
    morseWords = list(filter(bool, morseWords))
    morseDecB = ''
    for i in morseWords:
            morseDecB += dictDec[i]
    win.textEnc.setPlainText(morseDecB)
    pyperclip.copy(morseDecB)

if __name__ == '__main__':
    #Dictionaries // Словари
    dictEnEnc = {'a':'.- ' ,'b':'-... ','c':'-.-. ','d':'-.. ','e':'. ','f':'..-. ','g':'--. ','h':'.... ','i':'.. ','j':'.--- ','k':'-.- ','l':'.-.. ','m':'-- ','n':'-. ','o':'--- ','p':'.--. ','q':'--.- ','r':'.-. ','s':'... ','t':'- ','u':'..- ','v':'...- ','w':'.-- ','x':'-..- ','y':'-.-- ','z':'--.. ','0':'----- ','9':'----. ','8':'---.. ','7':'--... ','6':'-.... ','5':'..... ','4':'....- ','3':'...-- ','2':'..--- ','1':'.---- ',' ':'_ '}
    dictRuEnc = {'а':'.- ','б':'-... ','в':'.-- ','г':'--. ','д':'-.. ','е':'. ','ж':'...- ','з':'--.. ','и':'.. ','й':'.--- ','к':'-.- ','л':'.-.. ','м':'-- ','н':'-. ','о':'--- ','п':'.--. ','р':'.-. ','с':'... ','т':'- ','у':'..- ','ф':'..-. ','х':'.... ','ц':'-.-. ','ч':'---. ','ш':'---- ','щ':'--.- ','ъ':'.--.-. ','ы':'-.-- ','ь':'-..- ','э':'...-... ','ю':'..-- ','я':'.-.- ','0':'----- ','9':'----. ','8':'---.. ','7':'--... ','6':'-.... ','5':'..... ','4':'....- ','3':'...-- ','2':'..--- ','1':'.---- ',' ':'_ '}
    #Download custom Dictionary // Загрузка настраиваемого словаря
    try:
        with open('dict.json', 'r') as read_file:
            dictCustomEnc = json.load(read_file)
    except:
        dictCustomEnc = {'a':'.- ' ,'b':'-... ','c':'-.-. ','d':'-.. ','e':'. ','f':'..-. ','g':'--. ','h':'.... ','i':'.. ','j':'.--- ','k':'-.- ','l':'.-.. ','m':'-- ','n':'-. ','o':'--- ','p':'.--. ','q':'--.- ','r':'.-. ','s':'... ','t':'- ','u':'..- ','v':'...- ','w':'.-- ','x':'-..- ','y':'-.-- ','z':'--.. ','0':'----- ','9':'----. ','8':'---.. ','7':'--... ','6':'-.... ','5':'..... ','4':'....- ','3':'...-- ','2':'..--- ','1':'.---- ',' ':'_ '}
    
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
    
    app = QtWidgets.QApplication([])
    win = uic.loadUi("morse.ui")
    win.show()
    win.textEnc.setFocus()

    main()

    sys.exit(app.exec())