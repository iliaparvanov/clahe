from PIL import image
import numpy as np

def main:
    before_filename = 'sample.jpg'
    after_filename = 'sample_after.jpg'
    img = Image.open(filename)
    np_img = numpy.array(img)
    improved_img = Image.fromarray(equalize_histogram(np_img))
    improved_img.save(after_filename)


def equalize_histogram(np_img):
    return np_img