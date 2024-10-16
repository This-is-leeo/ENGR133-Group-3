import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import numpy as np

current_folder = os.path.dirname(os.path.abspath(__file__))

def to_binary(str):
    binary_value = []
    for i in str:
        binary_value.append(format(ord(i) , '08b'))
    return binary_value

def importImageToDict(all_images = {}, image_name = None):
    if image_name == None: image_name = input("Enter the path of the image you want to load: ")
    #Replace This Later while submitting!!!
    image_folder = 'images'
    image_path = os.path.join(current_folder, image_folder, image_name)
    #image_path = os.path.join(current_folder, image_name)
    all_images[image_name.strip()] = np.array(mpimg.imread(image_path) * 255)
    return all_images

def importImage(image_name = None):
    
    if image_name == None: image_name = input("Enter the path of the image you want to load: ")
    #Replace This Later while submitting!!!
    image_folder = 'images'
    image_path = os.path.join(current_folder, image_folder, image_name)
    #image_path = os.path.join(current_folder, image_name)
    return np.array(mpimg.imread(image_path) * 255)

def checkGrayscale(image: np.array):
    if len(image.shape) == 2:
        return True
    elif len(image.shape) == 3 and image.shape[2] == 1:
        return True
    else:
        return False
    

def visualize_image(img,image_name = None, save_path = None):
    if image_name != None: print(f'Below is the img_array output of {image_name}:')
    if checkGrayscale(img):
        plt.imshow(img.astype(np.uint8), cmap='gray')
    else:
        plt.imshow(img.astype(np.uint8))  # Convert to uint8
    #plt.axis('off')
    if save_path != None:
        #Replace This Later while submitting!!!
        image_folder = 'images'
        image_path = os.path.join(current_folder, image_folder, save_path)
        #image_path = os.path.join(current_folder, image_name)
        plt.savefig(image_path, format='png')

    plt.show()