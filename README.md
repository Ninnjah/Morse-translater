# Morse Translater

It's python program working with dictionaries and clipboard, and it can encrypt to morse from English, Russian and Custom dict and decrypt.

## Capabilities
1. Encrypt
```python
    morseEnB = ''
    for i in  morseEn.lower():
        if i in dictEnc:
            morseEnB += dictEnc[i]
    print(tui.score('Encrypted word', morseEnB), '\ncopied to clip')
    pyperclip.copy(morseEnB)
```
2. Decrypt
```python
    morseWords = morseDec.split(' ')
    morseWords = list(filter(bool, morseWords))
    morseDecB = ''
    os.system('cls||clear')  
    for i in morseWords:
        if i in dictDec:
            morseDecB += dictDec[i]
    print(tui.score('Decrypted word', morseDecB), '\ncopied to clip')
    pyperclip.copy(morseDecB)
```

# Screenshots


![CMD](https://github.com/Ninnjah/Morse-translater/blob/master/banner.jpg)

![GUI](https://github.com/Ninnjah/Morse-translater/blob/master/GUI.JPG)
