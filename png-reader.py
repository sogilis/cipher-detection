import os, sys
import Image

def isBlack(rgbPix):
  return rgbPix == (0, 0, 0)

def isRectangleBlack(rgbPix, threshold, top, bottom, left, right):
  rate = 0
  for row in range(top, bottom):
    for col in range(left, right):
      if isBlack(rgbPix[col, row]):
        rate = rate + 1

  rate = rate / float((bottom - top) * (right - left))

  if rate >= 0.25 * threshold:
    return 1
  else:
    return 0

def isOne(chiffre):
  pattern = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

  print pattern
  print chiffre

  percentage = 0
  for i in range(0, len(chiffre)):
    if (pattern[i] == chiffre[i]):
      percentage = percentage + 1

  return (percentage * 100) / len(chiffre)

if __name__ == '__main__':
  
  filename = sys.argv[1]
  pngFile = Image.open(filename)
  pix = pngFile.load()

  width, heigth = pngFile.size

  top = -1
  bottom = -1
  left = -1
  right = -1

  rate = 0
  for row in range(0, heigth):
    for col in range(0, width):
      
      if isBlack(pix[col, row]):
        rate = rate + 1

        if top == -1:
          top = row

        if bottom < row:
          bottom = row

        if left == -1 or left > col:
          left = col

        if right == -1 or right < col:
          right = col

  rate = rate / float((bottom - top) * (right - left))

  #print "top =", top, "bottom =", bottom, "left =", left, "right =", right

  chiffre = []

  rectangleHeigth = (bottom - top) / 10
  rectangleWidth  = (right - left) / 10

  for i in range(0, 10):
    for j in range(0, 10):
      chiffre.append(isRectangleBlack(pix, rate,
                                      top + i * rectangleHeigth,
                                      top + (i + 1) * rectangleHeigth,
                                      left + j * rectangleWidth,
                                      left + (j + 1) * rectangleWidth))

  likelihood = isOne(chiffre)
  print "Confidence that it is a 1:", likelihood, "%"
