import easyocr
import PIL
from PIL import Image, ImageDraw
def readText(filePath:str)->None:
    reader = easyocr.Reader(['en','ru'], gpu = True)


    bounds = reader.readtext(filePath)
    im = PIL.Image.open(filePath)

    def draw_boxes(image,bounds,color='red',width=2):
        count=0
        draw = ImageDraw.Draw(image)
        for bound in bounds:
            print(bounds[count][1])
            count=count + 1
        return bounds

    return draw_boxes(im, bounds)  