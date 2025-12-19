from PIL import Image


def save_image(img):
    Image.fromarray(img).save("note.png")
