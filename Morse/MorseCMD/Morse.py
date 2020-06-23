from tkinter import Tk
c = Tk()
print('-.. . -.-. --- .-. .- - .. --- -.\n..-. Translater to morse .-..\n-.. . -.-. --- .-. .- - .. --- -.')
dictA = {'a':'.- ' ,'b':'-... ','c':'-.-. ','d':'-.. ','e':'. ','f':'..-. ','g':'--. ','h':'.... ','i':'.. ','j':'.--- ','k':'-.- ','l':'.-.. ','m':'-- ','n':'-. ','o':'--- ','p':'.--. ','q':'--.- ','r':'.-. ','s':'... ','t':'- ','u':'..- ','v':'...- ','w':'.-- ','x':'-..- ','y':'-.-- ','z':'--.. ','0':'----- ','9':'----. ','8':'---.. ','7':'--... ','6':'-.... ','5':'..... ','4':'....- ','3':'...-- ','2':'..--- ','1':'.---- ',' ':'_ '}
dictB = {'.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f','--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l','--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r','...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x','-.--':'y','--..':'z','-----':'0','----.':'9','---..':'8','--...':'7','-....':'6','.....':'5','....-':'4','...--':'3','..---':'2','.----':'1','_':' '}

while True:
    cmdRaw=input('TO morse or FROM morse?  to/from: ')
    cmd = cmdRaw.lower()
    if cmd == 'to':
        morseA = input('Enter phrase to morse: ')
        morse = morseA.lower()
        morseB = ''
        for i in morse:
            morseB += dictA[i]
        print('Morse: ', morseB)
        c.withdraw()
        c.clipboard_clear()
        c.clipboard_append(morseB)
        c.update
        c.destroy
        
    elif cmd == 'from':
        cmdRaw=input('Paste copied morse? y/n: ')
        morseB = ''
        cmd = cmdRaw.lower()
        if cmd == 'y':
            c.withdraw()
            morseA = c.clipboard_get()
            c.update
            c.destroy
        else:
            morseA = input('Enter phrase from morse: ')
        morseWords = morseA.split(' ')
        for i in morseWords:
            if i == '':
                morseWords.remove('')
            else:
                morseB += dictB[i]
        print(morseB)
    elif cmd == 'exit':
        break
    else:
        print('!------------------------------!\nUnknown command. Print to/for\n!------------------------------!')