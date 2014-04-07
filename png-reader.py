import os, sys
import Image

def isBlack(rgbPix):
  return rgbPix == (0, 0, 0)

def isRectangleBlack(rgbPix, top, bottom, left, right):
  for row in range(top, bottom):
    for col in range(left, right):
      if isBlack(rgbPix[col, row]):
        return 1

  return 0

if __name__ == '__main__':
  
  pngFile = Image.open("1.png")
  pix = pngFile.load()

  width, heigth = pngFile.size

  top = -1
  bottom = -1
  left = -1
  right = -1

  for row in range(0, heigth):
    for col in range(0, width):
      
      if isBlack(pix[col, row]):

        if top == -1:
          top = row

        if bottom < row:
          bottom = row

        if left == -1 or left > col:
          left = col

        if right == -1 or right < col:
          right = col

  print "top = ", top, "bottom = ", bottom, "left = ", left, "right = ", right

  chiffre = []

  rectangleHeigth = (bottom - top) / 5
  rectangleWidth  = (right - left) / 5

  for i in range(0, 5):
    for j in range(0, 5):
      chiffre.append(isRectangleBlack(pix, 
                                      top + i * rectangleHeigth,
                                      top + (i + 1) * rectangleHeigth,
                                      left + j * rectangleWidth,
                                      left + (j + 1) * rectangleWidth))

  print chiffre

