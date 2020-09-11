import matplotlib.pyplot as plot
import matplotlib.image as image
import os


strPath = os.getcwd() + "/1st_edition/art/"
img = image.imread(strPath + "oreilly.png")
plot.imshow(img)
plot.show()
