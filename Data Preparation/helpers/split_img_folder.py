# Copyright 2014-2017 Bert Carremans
# Author: Bert Carremans <bertcarremans.be>
#
# License: BSD 3 clause

import os
import random
from shutil import copyfile
from convert_image_gp.helpers.check_mising_images import *


def img_train_test_split(img_source_dir, train_size):
    """
    Randomly splits images over a train and split_img_folder folder, while preserving the folder structure

    Parameters
    ----------
    img_source_dir : string
        Path to the folder with the images to be split. Can be absolute or relative path

    train_size : float
        Proportion of the original images that need to be copied in the subdirectory in the train folder
    """
    if not (isinstance(img_source_dir, str)):
        raise AttributeError('img_source_dir must be a string')

    if not os.path.exists(img_source_dir):
        raise OSError('img_source_dir does not exist')

    if not (isinstance(train_size, float)):
        raise AttributeError('train_size must be a float')

    # Set up empty folder structure if not exists
    if not os.path.exists('../data'):
        os.makedirs('../data')

    else:
        if not os.path.exists('../data/train'):
            os.makedirs('../data/train')
        if not os.path.exists('../data/test'):
            os.makedirs('../data/test')

    train_subdir = os.path.join('../data', 'train')
    test_subdir = os.path.join('../data', 'test')

    train_counter = 0
    test_counter = 0

    missing_img = cheack_misiing_images_in_gt_txt()
    # Randomly assign an image to train or test folder
    for filename in os.listdir(img_source_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            fileparts = filename.split('.')
            if int(fileparts[0]) not in missing_img:
                if random.uniform(0, 1) <= train_size:
                    copyfile(os.path.join(img_source_dir, filename),
                             os.path.join(train_subdir, str(fileparts[0]) + '.' + fileparts[1]))
                    train_counter += 1
                else:
                    copyfile(os.path.join(img_source_dir, filename),
                             os.path.join(test_subdir, str(fileparts[0]) + '.' + fileparts[1]))
                    test_counter += 1

    print("training images count: {}".format(train_counter))
    print("testing images count: {}".format(test_counter))


img_train_test_split("E:/programs/lab/convert_image_gp/FullIJCNN2013", 0.85)
