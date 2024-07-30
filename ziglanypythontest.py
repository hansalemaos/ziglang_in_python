import numpy as np
import cv2
from ziglanypython import search_colors
import time

# 4525 x 6623 x 3 picture https://www.pexels.com/pt-br/foto/foto-da-raposa-sentada-no-chao-2295744/
picx = r"C:\Users\hansc\Downloads\pexels-alex-andrews-2295744.jpg"
pic = cv2.imread(picx)
if not pic.flags["C_CONTIGUOUS"]:
    pic = np.ascontiguousarray(pic)
colors0 = np.array([[255, 255, 255]], dtype=np.uint8)
start = time.perf_counter()
resus0 = search_colors(pic=pic, colors=colors0)
print(time.perf_counter() - start)
colors1 = np.array(
    [
        (66, 71, 69),
        (62, 67, 65),
        (144, 155, 153),
        (52, 57, 55),
        (127, 138, 136),
        (53, 58, 56),
        (51, 56, 54),
        (32, 27, 18),
        (24, 17, 8),
    ],
    dtype=np.uint8,
)
start = time.perf_counter()
resus1 = search_colors(pic=pic, colors=colors1)
print(time.perf_counter() - start)
####################################################################
# search_colors(pic=pic, colors=colors0)
# resus1 =  search_colors(pic=pic, colors=colors1)
