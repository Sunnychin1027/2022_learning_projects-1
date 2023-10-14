"""
File: blur.py
Name: Sunny
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    First create a blank image, then we will get all neighbor pixel from
    old image, get total pixel and number or neighbor, get the average color
    and put the color back to the blank image to get blur image.
    :param img: SimpleImage, original picture
    :return: SimpleImage, blurred picture
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            new_img_pixel = new_img.get_pixel(x,y)
            total_red = 0
            total_green = 0
            total_blue = 0
            total_num = 0
            for j in range(-1, 2, 1):       # nearest neighbor algo
                for k in range(-1, 2, 1):
                    x1 = x + j
                    y1 = y + k
                    if 0 <= x1 < img.width:
                        if 0 <= y1 < img.height:
                            pixel = img.get_pixel(x1, y1)
                            total_red += pixel.red
                            total_green += pixel.green
                            total_blue += pixel.blue
                            total_num += 1
            new_img_pixel.red = total_red / total_num
            new_img_pixel.green = total_green / total_num
            new_img_pixel.blue = total_blue / total_num
    return new_img
    

def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
