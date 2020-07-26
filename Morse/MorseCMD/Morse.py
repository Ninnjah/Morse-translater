import os
import time
import json
import pyperclip
import easyTui as tui

# Main menu // Главное меню
def main():
    # Select Mode // Выбор режима
    def selectMode():
        # Clear the console // Очистка консоли
        os.system('cls||clear')  
        # Title // Заголовок                           
        print(tui.title('Morse Translater'))
        # Print modes list // Вывод списка режимов
        print(tui.label('Select mode...'))
        print(tui.ol(['Encryption to morse', 'Decryption from morse']))
        print('to exit enter "exit"')
        # request for input // Запрос ввода
        cmd = input()
        # Check input // Проверка ввода
        if cmd in '012':
            return cmd
        elif cmd.lower() == 'exit':
            quit()
        else:
            print('Enter number from 0 to 2', end='\r')
            time.sleep(1)
            print(' '*24, end='\r')
            selectMode()
    # Select lang // Выбор языка
    def selectLang():
        # Clear the console // Очистка консоли
        os.system('cls||clear')  
        # Print modes list // Вывод списка режимов
        print(tui.label('Select dict...'))
        print(tui.ol(['English', 'Russian', 'Custom']))
        # request for input // Запрос ввода
        lang = input()
        # Check input // Проверка ввода
        if lang in '012':
            return lang
        else:
            print('Enter number from 0 to 2', end='\r')
            time.sleep(1)
            print(' '*24, end='\r')
            selectLang()
    cmd = selectMode()
    lang = selectLang()
    if cmd == '0':
        Encrypt(lang)
    elif cmd == '1':
        Decrypt(lang)
    else:
        print('Incorrect input!')
        time.sleep(1)
        main()
      # Select using paperclip // Выбор использования буфера обмена

# Select using clip // Выбор использования буфера
def selectCopy():
    # Clear the console // Очистка консоли
    os.system('cls||clear')  
    print(tui.label('Do you want to paste text from clip? y/n'))
    cmd = input()
    if cmd.lower() == 'y':
        clip = pyperclip.paste()
    elif cmd.lower() == 'n':
        clip = input('Enter phrase to encrypt: ')
    else:
        print('Enter y/n..')
        time.sleep(1)
        selectCopy()
    return clip
  
# Encrypting to Morse // Шифровка в морзе
def Encrypt(lang):
    if lang == '0':
        dictEnc=dictEnEnc
    elif lang == '1':
        dictEnc=dictRuEnc
    elif lang == '2':
        dictEnc=dictCustomEnc
    morseEn = selectCopy()
    morseEnB = ''
    # Clear the console // Очистка консоли
    os.system('cls||clear')  
    for i in  morseEn.lower():
        if i in dictEnc:
            morseEnB += dictEnc[i]
    print(tui.score('Encrypted word', morseEnB), '\ncopied to clip')
    pyperclip.copy(morseEnB)
    input('Press Enter...')
    main()
    
# Decrypting from Morse // Расшифровка из морзе
def Decrypt(lang):
    if lang == '0':
        dictDec=dictEnDec
    elif lang == '1':
        dictDec=dictRuDec
    elif lang == '2':
        dictDec=dictCustomDec
    morseDec = selectCopy()
    morseWords = morseDec.split(' ')
    morseWords = list(filter(bool, morseWords))
    morseDecB = ''
    # Clear the console // Очистка консоли
    os.system('cls||clear')  
    for i in morseWords:
        if i in dictDec:
            morseDecB += dictDec[i]
    print(tui.score('Decrypted word', morseDecB), '\ncopied to clip')
    pyperclip.copy(morseDecB)
    input('\n\nPress Enter...')
    main()

# Init program, generating dicts // Запуск программы и генерация словарей
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
    
    main()
