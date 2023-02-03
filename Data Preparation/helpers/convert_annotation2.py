import cv2
import os
from tqdm import tqdm
import numpy as np
from convert_image_gp.helpers.check_mising_images import *

annotation_file = open("../gt.txt", "r")
ids = list()
img_count = 0

missing_img = cheack_misiing_images_in_gt_txt()

if not os.path.exists('../annotation'):
    os.makedirs('../annotation')


for line in tqdm(annotation_file):
    img_count += 1
    data = line.split(';')
    if int(data[0].split('.')[0]) not in missing_img:
        coords = np.asarray([float(data[1]), float(data[2]), float(data[3]), float(data[4])])
        class_id = int(data[-1].split('\n')[0])
        ids.append(class_id)
        img_name = data[0].split('.')[0]

        image = cv2.imread("../FullIJCNN2013" + "\\" + img_name + ".jpg")

        coords[2] -= coords[0]
        coords[3] -= coords[1]
        x_diff = int(coords[2] / 2)
        y_diff = int(coords[3] / 2)
        coords[0] = coords[0] + x_diff
        coords[1] = coords[1] + y_diff
        coords[0] /= int(image.shape[1])
        coords[1] /= int(image.shape[0])
        coords[2] /= int(image.shape[1])
        coords[3] /= int(image.shape[0])

        add_line = str(data[5].split()[0]) + ' ' + str(coords[0]) + ' ' + str(coords[1]) + ' ' + str(coords[2]) + ' ' + str(
            coords[3])
        with open("../annotation" + "\\" + img_name + ".txt", "a+") as outfile:
            outfile.write(add_line)
            outfile.write("\n")
            outfile.close()

print(img_count)
print("success")
