from PIL import Image
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

plt.ion()

def main():
    before_filename = 'rose.jpg'
    after_filename = 'rose_after.jpg'
    
    img = Image.open(before_filename).convert('L')
    np_img = np.array(img)
    
    plot_and_save_hist(np_img, 'histogram_before.png', 'histogram before')
    improved_img_np = equalize_histogram(np_img)
    plot_and_save_hist(improved_img_np, 'histogram_after.png', 'histogram after')

    improved_img = Image.fromarray(improved_img_np)
    improved_img.save(after_filename)


def equalize_histogram(np_img):
    improved_np_img = np.copy(np_img)
    improved_np_img_raveled = improved_np_img.ravel()

    hist, bin_edges = np.histogram(np_img, bins=256, range=(0, 255))
    h_cum, r, h_m = 0, 0, (len(improved_np_img_raveled)/bin_edges[-1])
    c_n = []

    for idx, c in enumerate(hist):
        l_c = r 
        h_cum = h_cum + hist[idx]
        while h_cum > h_m:
            r += 1
            h_cum = h_cum - h_m
        r_c = r
        #calculate c_n
        c_n.append(int((l_c + r_c) / 2))

    for i in range(0, improved_np_img.shape[0]):
        for z in range(0, improved_np_img.shape[1]):
            improved_np_img[i, z] = c_n[improved_np_img[i,z]]

    return improved_np_img

def plot_and_save_hist(np_img, filename, histname):
    plt.clf()
    plt.hist(np_img.ravel(), bins = 255) 
    plt.title(histname) 
    plt.savefig(filename)

main()