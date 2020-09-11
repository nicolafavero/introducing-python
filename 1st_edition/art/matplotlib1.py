import matplotlib.pyplot as plot
import matplotlib.image as image
import os


#strPath = os.getcwd() + "/1st_edition/art/"
strPath = os.path.dirname(__file__)
img = image.imread(strPath + "/oreilly.png")
plot.imshow(img)
plot.show()
