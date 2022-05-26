import pytesseract
import cv2 as cv
import scrython
import re
import glob, os

CardImage = []
def GetCardLocation():
    os.chdir("F:\Damien Faculty\scryfall-image-recognition\scryfall-image-recognition\Images")
    for file in glob.glob("*.jpg"):
        CardImage.append(file)
    return CardImage

def GetCardInfo(CardImage):
    img = cv.imread(CardImage,0)
    img = img[55:100,55:480]
    #cv.imshow("end result",img)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    CardName = pytesseract.image_to_string(img)
    splitnames= CardName.splitlines()
    card = scrython.cards.Named(fuzzy=splitnames[0])
    return card

def PrintCardInfo(card):
    try:
        flavortext=card.flavor_text()
    except KeyError:
        flavortext= ""
    if re.findall('Creature',card.type_line()) >= ['Creature']:
        #print(card.power()+"/"+card.toughness())
        f = open("./text/"+card.name()+".txt", "w")
        f.write('Card name: '+str(card.name())+'   '+str(card.mana_cost())+'\n'+'Card color: '+str(card.colors())+'\n'+'Card Type: '+str(card.type_line())+'\n'+'Description text: '+str(card.oracle_text())+'\n'+'Card flavor text: '+str(flavortext)+'\n'+'Power/Toughness: '+str(card.power())+'/'+str(card.toughness())+'\n'+'Card Link: '+str(card.scryfall_uri()))
        f.close()
    else:
        f = open("./text/"+card.name()+".txt", "w")
        f.write('Card name: '+str(card.name())+'   '+str(card.mana_cost())+'\n'+'Card color: '+str(card.colors())+'\n'+'Card Type: '+str(card.type_line())+'\n'+'Description text: '+str(card.oracle_text())+'\n'+'Card flavor text: '+str(flavortext)+'\n'+'Card Link: '+str(card.scryfall_uri()))
        f.close()

def TestCardInfo(card):
    print(card.type_line())
    print(card.name())
    print(card.colors())
    print(card.mana_cost())
    print(card.oracle_text())
    print(card.cmc())
