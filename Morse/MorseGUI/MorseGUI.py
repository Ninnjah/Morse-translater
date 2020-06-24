from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import json
#Dictionaries // Словари
dictEnEnc = {'a':'.- ' ,'b':'-... ','c':'-.-. ','d':'-.. ','e':'. ','f':'..-. ','g':'--. ','h':'.... ','i':'.. ','j':'.--- ','k':'-.- ','l':'.-.. ','m':'-- ','n':'-. ','o':'--- ','p':'.--. ','q':'--.- ','r':'.-. ','s':'... ','t':'- ','u':'..- ','v':'...- ','w':'.-- ','x':'-..- ','y':'-.-- ','z':'--.. ','0':'----- ','9':'----. ','8':'---.. ','7':'--... ','6':'-.... ','5':'..... ','4':'....- ','3':'...-- ','2':'..--- ','1':'.---- ',' ':'_ '}
dictRuEnc = {'а':'.- ','б':'-... ','в':'.-- ','г':'--. ','д':'-.. ','е':'. ','ё':'. ','ж':'...- ','з':'--.. ','и':'.. ','й':'.--- ','к':'-.- ','л':'.-.. ','м':'-- ','н':'-. ','о':'--- ','п':'.--. ','р':'.-. ','с':'... ','т':'- ','у':'..- ','ф':'..-. ','х':'.... ','ц':'-.-. ','ч':'---. ','ш':'---- ','щ':'--.- ','ъ':'.--.-. ','ы':'-.-- ','ь':'-..- ','э':'...-... ','ю':'..-- ','я':'.-.- ','0':'----- ','9':'----. ','8':'---.. ','7':'--... ','6':'-.... ','5':'..... ','4':'....- ','3':'...-- ','2':'..--- ','1':'.---- ',' ':'_ '}
#Download custom Dictionary // Загрузка настраеваемого словаря
with open('dict.json', 'r') as read_file:
    dictCustomEnc = json.load(read_file)

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
# Custom dictionary // Настраеваемый словарь
dictCustomEncC = dictCustomEnc.copy()
for k, v in dictCustomEncC.items():
    dictCustomEncC[k] = v.rstrip()
dictCustomDec = dict(zip(dictCustomEncC.values(), dictCustomEncC.keys()))

#*Code // Код
#Encrypting to Morse // Шифровка в морзе
def Encrypt():
    if comboLang.get() == 'English':
        dictEnc=dictEnEnc
    elif comboLang.get() == 'Russian':
        dictEnc=dictRuEnc
    elif comboLang.get() == 'Custom':
        dictEnc=dictCustomEnc
    morseEn = eTo.get()
    print(morseEn)
    morseEnlow = morseEn.lower()
    morseEnB = ''
    for i in morseEnlow:
        morseEnB += dictEnc[i]
    tFrom.delete(1.0, END)
    tFrom.insert(1.0, morseEnB)
    root.clipboard_clear()
    root.clipboard_append(morseEnB)

#Decrypting from Morse // Расшифровка из морзе
def Decrypt():
    if comboLang.get() == 'English':
        dictDec=dictEnDec
    elif comboLang.get() == 'Russian':
        dictDec=dictRuDec
    elif comboLang.get() == 'Custom':
        dictDec=dictCustomDec
    morseDec = eFrom.get()
    morseWords = morseDec.split(' ')
    morseWords = list(filter(bool, morseWords))
    morseDecB = ''
    for i in morseWords:
            morseDecB += dictDec[i]
    tTo.delete(1.0, END)
    tTo.insert(1.0, morseDecB)
    root.clipboard_clear()
    root.clipboard_append(morseDecB)

#*Interface // Интерфейс
#Creating root window // Создание главного окна
root = Tk()
root.title("Морзе переводчик")
root.geometry('400x210')
root.resizable(width=False, height=False)

#Encrypting Row // Ряд зашифровки
lTo = Label(root, font=('Arial Bold', 8), text='Шифровка в азбуку морзе')
lTo.grid(column=0, row=0)
eTo = Entry(root, width=48)
eTo.grid(column=0, row=1)
tTo = scrolledtext.ScrolledText(root, width=36, height=3)
tTo.grid(column=0, row=2)
bTo = Button(root, text='Зашифровать', height=3, command=Encrypt)
bTo.grid(column=1, row=2)

#Decrupting Row // Ряд расшифровки
lFrom = Label(root, font=('Arial Bold', 8), text='Расшифровка из азбуки морзе')
lFrom.grid(column=0, row=3)
eFrom = Entry(root, width=48)
eFrom.grid(column=0, row=4)
tFrom = scrolledtext.ScrolledText(root, width=36, height=3)
tFrom.grid(column=0, row=5)
bFrom = Button(root, text='Расшифровать', height=3, command=Decrypt)
bFrom.grid(column=1, row=5)

#Language set // Выбор языка
comboLang = ttk.Combobox(root, values=['English','Russian','Custom'])
comboLang.grid(column=0, row=6)

eTo.focus()
root.mainloop()
