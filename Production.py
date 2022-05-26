import pytesseract
import cv2 as cv
import scrython
import re
import glob, os
import FinalVersion

location = FinalVersion.GetCardLocation()
print (location)
for Card in location:
    printcard = FinalVersion.GetCardInfo(Card)
    FinalVersion.PrintCardInfo(printcard)
print("Finished!")

