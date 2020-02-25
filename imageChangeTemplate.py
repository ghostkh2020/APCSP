import PIL
import matplotlib.pyplot as plt
import numpy as np
import os.path
import PIL.ImageDraw


# def cutBackground(image):
#     """
#     What this progrsm doesis that it will
#     """
#
#     img = PIL.image.new('RGBA',(columns, rows))
#     image = np.array(img)
#     numRows = len(image)
#     numcols = len(image[0])
#     for row in range(numRows):
#        for col in range (numcols):
#             currentPixel = image[row][col]
#             currentRed = currentPixel[0]
#             currentGreen = currentPixel[1]
#             currentBlue = currentPixel[2]
#             averageIntensity = (currentRed / 3 + currentGreen/3 + currentBlue/3)
#             if average
#
#             if averageIntensity < 50:
#                 img[row][col] = [0,0,0,255]
#
#             else:
#                 img[row][col] = averageIntensity
#     return image
#

# def tint_image(image):
#     mixed_image = image.opean("mroad.jpg")
#     mixed_image = mixed_image.coonvert("RGB") # ensure image has 3 channels
#     blue = RGBTransform().mix_with((0, 0, 255),factor=.30).applied_to(mixed_image)#blue tint
#     #################################### help ################################

def Mixer(img1, img2):  # This is the
    numRow = len(img2)
    print
    numRow

    numCols = len(img2[0])
    print
    numCols
    final_image = np.ndarray(shape=(numRow, numCols, 4), dtype=np.float)

    for row in range(numRow):
        for col in range(numCols):
            currentPixel = img1[row][col]
            alfa = 1
            if len(currentPixel) == 4:
                alfa = currentPixel[3]

            currentRed = currentPixel[0]
            currentGreen = currentPixel[1]
            currentBlue = currentPixel[2]
            # averageIntensity = (currentRed / 3 + currentGreen/3 + currentBlue/3)
            # final_image[row][col] = [averageIntensity , averageIntensity, averageIntensity]

            if (currentRed > 0.6 and currentGreen > 0.6 and currentBlue > 0.6) or alfa == 0:
                if len(img2[row][col]) == 4:
                    final_image[row][col] = img2[row][col]
                else:
                    final_image[row][col] = [img2[row][col][0], img2[row][col][1], img2[row][col][2], 255]

            else:

                if len(img1[row][col]) == 4:
                    final_image[row][col] = img1[row][col]
                else:
                    final_image[row][col] = [img1[row][col][0], img1[row][col][1], img1[row][col][2], 255]

    return final_image


directory = os.path.dirname(os.path.abspath(__file__))
front_filename = os.path.join(directory, "dream.png")
back_filename = os.path.join(directory, "yroad.png")
front_img = plt.imread(front_filename)
back_img = plt.imread(back_filename)
fig, ax = plt.subplots(1, 3)

ax[0].imshow(front_img, interpolation="none")
ax[1].imshow(back_img, interpolation="none")
mixed_image = Mixer(front_img, back_img)
ax[2].imshow(mixed_image, interpolation="none")

fig.show()


def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.

    If directory is not specified, uses current directory.
    Returns a 2-tuple containing
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """

    if directory == None:
        directory = os.getcwd()  # Use working directory if unspecified
    image_list = []  # Initialize aggregaotrs
    file_list = []

    directory_list = os.listdir(directory)  # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass  # do nothing with errors tying to open non-images
    return image_list, file_list


def change_all_images(directory=None):  # TODO: change name
    """ Saves a modified version of each image in directory.

    Uses current directory if no directory is specified.
    Places images in subdirectory 'modified', creating it if it does not exist.
    """

    if directory == None:
        directory = os.getcwd()  # Use working directory if unspecified

    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass  # if the directory already exists, proceed

    # load all the images
    image_list, file_list = get_images(directory)

    # go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        filename, filetype = file_list[n].split('.')

        # TODO: Write code here that calls your function to change the images
        new_image = image_list[n]

        # save the altered image, using PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)

# change_all_images()