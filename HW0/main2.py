import cv2
import numpy as np

img1 = cv2.imread("./data/lena.png")
img2 = cv2.imread("./data/lena_modified.png")

# 使用後者異於前者的部分產生相同格式的新圖檔 ans_two.png

new_img = img2.copy()

for old in np.nditer(img1):
    for new in np.nditer(new_img):
        # TODO opencv 将相同的像素设置为透明
        pass
