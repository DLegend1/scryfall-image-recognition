import pytesseract
import cv2 as cv
import scrython
import re
img = cv.imread('img15.jpg',0)
'''scan = cv.medianBlur(img,5)'''
"""
adaptive gaussian treshold
"""
img = img[55:100,55:480]
cv.imshow("end result",img)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

CardName = pytesseract.image_to_string(img)

splitnames= CardName.splitlines()
card = scrython.cards.Named(fuzzy=splitnames[0])
print(card.type_line())
print(card.name())
print(card.colors())
print(card.mana_cost())
print(card.oracle_text())
print(card.cmc())
try:
    flavortext=card.flavor_text()
except KeyError:
    flavortext= ""
if re.findall('Creature',card.type_line()) >= ['Creature']:
    print(card.power()+"/"+card.toughness())
    f = open(card.name()+".txt", "w")
    f.write('Card name: '+str(card.name())+'   '+str(card.mana_cost())+'\n'+'Card color: '+str(card.colors())+'\n'+'Card Type: '+str(card.type_line())+'\n'+'Description text: '+str(card.oracle_text())+'\n'+'Card flavor text: '+str(flavortext)+'\n'+'Power/Toughness: '+str(card.power())+'/'+str(card.toughness())+'\n'+'Card Link: '+str(card.scryfall_uri()))
    f.close()
else:
    f = open(card.name()+".txt", "w")
    f.write('Card name: '+str(card.name())+'   '+str(card.mana_cost())+'\n'+'Card color: '+str(card.colors())+'\n'+'Card Type: '+str(card.type_line())+'\n'+'Description text: '+str(card.oracle_text())+'\n'+'Card flavor text: '+str(flavortext)+'\n'+'Card Link: '+str(card.scryfall_uri()))
    f.close()
    





"""
# adds image processing capabilities
from PIL import Image
# will convert the image to text string
import pytesseract
# assigning an image from the source path
"""
#pytesseract.pytesseract.tesseract_cmd = r"C:\Users\DLegend\AppData\Local\Programs\Python\Python39\Lib\site-packages\tesseract\__init__.py"
"""
img = Image.open('IMGS/img1.jpg')
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)

with open('text_result.txt', mode ='w') as file:
 file.write(result)
 print('ready!')
"""


"""
# adds more image processing capabilities
from PIL import Image, ImageEnhance
import pytesseract
# assigning an image from the source path
img = Image.open("IMGS/img1.jpg")
# adding some sharpness and contrast to the image 
enhancer1 = ImageEnhance.Sharpness(img)
enhancer2 = ImageEnhance.Contrast(img)
img_edit = enhancer1.enhance(20.0)
img_edit = enhancer2.enhance(1.5)
# save the new image
img_edit.save("edited_image.png")
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img_edit)
file = open('text_result2.txt', 'w+')
file.writelines(result)
print(result)
"""
