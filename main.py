from PIL import Image
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

plt.ion()

def main():
    before_filename = 'sample_xray.png'
    after_filename = 'sample_after.jpg'
    
    img = Image.open(before_filename).convert('L')
    np_img = np.array(img)
    
    plot_and_save_hist(np_img)
    improved_img_np = equalize_histogram(np_img)
    plot_and_save_hist(improved_img_np)

    improved_img = Image.fromarray(improved_img_np)
    improved_img.save(after_filename)


def equalize_histogram(np_img):
    hist, bin_edges = np.histogram(np_img, bins=10)
    # print(hist)
    # print(np_img)

    
    return np_img

def plot_and_save_hist(np_img):
    plt.hist(np_img.ravel(), bins = 255) 
    plt.title("histogram before") 
    plt.savefig('histogram.png')

main()