import os


# check for mising images in gt.txt
def cheack_misiing_image_in_image_folder():
    hi = 0
    for filename in os.listdir('E:/programs/lab/convert_image_gp/FullIJCNN2013'):
        num = int(filename.split('.')[0])
        if hi != num:
            print(hi)
            hi = num
            hi += 1
        else:
            hi += 1


def cheack_misiing_images_in_gt_txt():
    annotation_file = open("../gt.txt", "r")
    num = []
    missing = []
    for filename in annotation_file:
        if int(filename.split('.')[0]) not in num:
            num.append(int(filename.split('.')[0]))
    for missing_image_name in range(900):
        if missing_image_name not in num:
            missing.append(missing_image_name)
    print("images without labels: {}".format(missing))
    print("images without labels count: {}".format(len(missing)))
    return missing

