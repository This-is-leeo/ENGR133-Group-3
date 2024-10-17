import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import numpy as np

current_folder = os.path.dirname(os.path.abspath(__file__))

def toBinary(str):
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
    

def visualizeImage(img,image_name = None, save_path = None):
    if image_name != None: print(f'Below is the img_array output of {image_name}:')
    if checkGrayscale(img):
        plt.imshow(img.astype(np.uint8), cmap='gray')
        if save_path != None:
            image_path = os.path.join(current_folder, 'images', image_name)
            plt.savefig(image_path, format='png')
    else:
        plt.imshow(img.astype(np.uint8))  # Convert to uint8
        if save_path != None:
            image_path = os.path.join(current_folder, 'images', image_name)
            plt.savefig(image_path, format='png')
    #plt.axis('off')

    plt.show()

def compare_image(input_file_name_1 = None, input_file_name_2 = None, output_file_name = 'diff.png', printout = False):
    image1 = importImage(input_file_name_1)
    image2 = importImage(input_file_name_2)
    if  not checkGrayscale(image1): image1 = image1[:,:,:3]
    if  not checkGrayscale(image2): image2 = image2[:,:,:3]
    
    if checkGrayscale(image1) != checkGrayscale(image2):
        print('Cannot compare images in different modes (RGBA and L).')
        return False
    if image1.shape[0] != image2.shape[0] or image1.shape[1] != image2.shape[1]:
        #print('The images are different.')
        return False
    
    identical = True
    #when it is not a grayscale image
    if not checkGrayscale(image1) and not checkGrayscale(image2):
        difference_image = np.zeros(image1.shape)
        for row in range(difference_image.shape[0]):
            for pixel in range(difference_image.shape[1]):
                for bit in range(difference_image.shape[2]):
                    if image1[row,pixel,bit] != image2[row,pixel,bit]:
                        difference_image[row,pixel,bit] = 255
                        identical = False
                    if bit == 3: difference_image[row,pixel,bit] = 255
                    #for some image there is a 4th pixel for brightness, lowkey dumb af

    elif len(image1.shape) == 3:
        difference_image = np.zeros(image1.shape)
        for row in range(difference_image.shape[0]):
            for pixel in range(difference_image.shape[1]):
                if image1[row,pixel,0] != image2[row,pixel,0]:
                    difference_image[row,pixel,0] = 255
                    identical = False
        
    else:
        difference_image = np.zeros(image1.shape)
        for row in range(difference_image.shape[0]):
            for pixel in range(difference_image.shape[1]):
                if image1[row,pixel] != image2[row,pixel]:
                    difference_image[row,pixel] = 255
                    identical = False

    visualizeImage(difference_image)
    if printout:
        if not identical:
            print('The images are different.')
        else:
            print("The images are the same.")
    return identical

def convertToText(extracted_message = None):  
    extracted_message = [extracted_message[i:i+8] for i in range(0, len(extracted_message), 8)]   
    ans = ''
    for i in extracted_message:
        i = int(i,2)
        ans += chr(i)  
    return ans