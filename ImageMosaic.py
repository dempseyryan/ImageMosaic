## Ryan Dempsey July 2020, photo sorting module

## import system and ui stuff
import os, tkinter.filedialog, pathlib
from tkinter import *
import time
from tkinter.ttk import Progressbar
## import image stuff
from PIL import *
import PIL.Image
#import Image
## import types
from typing import *
from tkinter import messagebox as mb


## Acceptable image formats
IMAGE_FILE_TYPES = [('All files', '.*'),
                    ('Image files', '.bmp'),
                    ('Image files', '.gif'),
                    ('Image files', '.png'),
                    ('Image files', '.tif'),
                    ('Image files', '.tiff'),
                    ('Image files', '.jpg'),
                    ('Image files', '.jpeg')]


def load_file(file_extensions: List[Tuple]) -> str:
    
    """
    Return a filename string of any type based on the parameter. file_extensions
    is a list that defines the acceptables extns. If file_extenstions is empty, 
    prompt user for a directory
    """
    
    window = Tk()
    window.withdraw()    
    if file_extensions == []:
        path = tkinter.filedialog.askdirectory()
    else:
        path = tkinter.filedialog.askopenfilename(filetypes = file_extensions)
    
    window.destroy()
    return path

def image_from_file(filename: str) -> Image:
    
    """
    Returns Image type from specified filename string
    """
    
    ## Check if the extension is accepted by checking for corresponding tuple
    ## Then return the HSV mode of the image, as that's what we will sort with
    if ('Image files', filename[-5:]) in IMAGE_FILE_TYPES\
       or ('Image files', filename[-4:]) in IMAGE_FILE_TYPES:
        
        return PIL.Image.open(filename).convert("HSV")
    else:
        
        return None
    
def images_from_files(filenames: List[str]) -> List[Image]:
    
    """
    Returns a list of Images based on a list of filenames
    """
    
    images = []
    for name in filenames:
        images.append(image_from_file(name))
    return images

def load_image_list() -> List[Image]:
    
    """
    Prompts user and returns a list of all Images present in the user-selected directory
    """
    ## Choose directory and initialize image list
    batch_folder = load_file([])
    images_to_use = []
    
    for root, dirs, files in os.walk(batch_folder): ## Check folder
        for file in files:
            
            ## For every file in folder, get the absolute path, convert to string
            ## and add the image itself to the list
            images_to_use.append(image_from_file(str(pathlib.Path.home().joinpath(root, file))))
            #files_to_use.append(image_from_file(root + "/" + files[i]))
            #meow = str(pathlib.Path.home().joinpath(root, files[i])); print(meow)
            
    return images_to_use

def load_images() -> Tuple[List[Image], str]:
    
    """
    Prompts user and returns a list of all Images present in the user-selected directory,
    while keeping the original path and files
    """
    ## Choose directory and initialize image list
    batch_folder = load_file([])
    images_to_use = []
    image_names = []
    
    for root, dirs, files in os.walk(batch_folder): ## Check folder
        for file in files:
            
            ## For every file in folder, get the absolute path, convert to string
            ## and add the image itself to the list
            image_name = str(pathlib.Path.home().joinpath(root, file))
            image_names.append(image_name)
            images_to_use.append(image_from_file(image_name))
            #files_to_use.append(image_from_file(root + "/" + files[i]))
            #meow = str(pathlib.Path.home().joinpath(root, files[i])); print(meow)
            
    return images_to_use, image_names, batch_folder
    
            
            
def read_colour_rgb(colour: str) -> Tuple[int]:
    
    ## Take an acceptable colour input as string and output the rgb colour tuple
    if colour.lower() == 'red':
        return 255, 0, 0
    elif colour.lower() == 'blue':
        return 0, 0, 255
    elif colour.lower() == 'yellow':
        return 255, 255, 0
    else:
        return None

def read_colour_hsv(colour: str) -> Tuple[int]:
    
    ## Take an acceptable colour input as string and output the corresponding hsv
    if colour.lower() == 'black':
        return 0, 0, 0
    elif colour.lower() == 'white':
        return 0, 0, 100
    else:
        return None
    
def average_hsv(image: Image) -> Tuple:
    
    """Returns the average hsv value tuple in a given image
    """
    
    hue = sat = val = 0
    pixels = image.load()
    for x in range(image.width):
        for y in range(image.height):
            
            colour = pixels[x, y]
            hue += colour[0]
            sat += colour[1]
            val += colour[2]
            
    hue /= (image.width * image.height)
    sat /= (image.width * image.height)
    val /= (image.width * image.height)
    
    return hue, sat, val

def sort_by_colour(images: List[Image]) -> List[Image]:
    
    """
    Sorts any number of Images in ascending order based on their colours &
    returns the sorted list of Images. Algorithm is very primitive and arbitrary
    (sorts hue with saturation as a tiebreaker, and only checks value if both h
    and s are equal).
    """
    
    ## Get size of final image and use new() PIL factory function to construct
    ## Also get the average hue of every image
    
    
    for i in range(len(images)):
        for j in range(i + 1, len(images)):
        
            avg_hue_i, avg_sat_i, avg_val_i = average_hsv(images[i])
            avg_hue_j, avg_sat_j, avg_val_j = average_hsv(images[j])
        
            
        
            # Swap images if there is an image j, any point after i, with lower hsv
            if avg_hue_j - avg_hue_i < -0.01: # avg_hue_j < avg_hue_i
                images[i], images[j] = images[j], images[i]
                
            elif abs (avg_hue_j - avg_hue_i) < 0.01: # avg_hue_j == avg_hue_i
                
                if avg_sat_j - avg_sat_i < -0.01: # avg_sat_j < avg_sat_i
                    images[i], images[j] = images[j], images[i]
                    
                elif abs (avg_sat_j < avg_sat_i) < 0.01: # avg_sat_j == avg_sat_i
                    
                    if avg_val_j - avg_val_i < -0.01: # avg_val_j < avg_val_i
                        images[i], images[j] = images[j], images[i]
                    
        
        #print ("avg hsv for image {} is {}".format(i, (hue_avg, sat_avg, val_avg))) ## Testing
        
        
    
    return images

def combine_images_horizontally(images: List[Image], border_colour: str,\
                            border_size: int) -> Image:
    
    """
    Combines a list of Images horizontally into one Image in the order of the
    list with border size and colour based on parameters
    """
    
    ## Determine total length and width of image
    height = width = 0
    for image in images:
        width += image.width
        if height < image.height:
            height = image.height
    width += border_size * (len(images) - 1)        
    ## Create blank image of right size and initialize border/backround
    
    border_colour = read_colour_hsv(border_colour)
    new_image = PIL.Image.new("HSV", (width, height))
    pixels = new_image.load()
    
    for x in range(new_image.width):
        for y in range(new_image.height):
            pixels[x, y] = border_colour
    #i = 0
    for y in range(new_image.height):
        i = 0
        for image in images:
            for x in range(i, image.width + i):
                if y < image.height:
                    pixels[x, y] = image.getpixel((x - i, y))
                ## if not then leave it as the bg colour
            i += image.width + border_size
        #i = 0
        #for image in images:
            #for x in range(image.width):
                #pixels[x + i, y] = image.getpixel(x, y)
            
    return new_image

def combine_images_vertically(images: List[Image], border_colour: str,\
                            border_size: int) -> Image:
    
    """
    Combines a list of Images vertically into one Image in the order of the
    list with border size and colour based on parameters
    """
    
    ## Determine total length and width of image
    height = width = 0
    for image in images:
        height += image.height
        if width < image.width:
            width = image.width
    height += border_size * (len(images) - 1)        
    ## Create blank image of right size and initialize border/backround
    
    border_colour = read_colour_hsv(border_colour)
    new_image = PIL.Image.new("HSV", (width, height))
    pixels = new_image.load()
    
    for x in range(new_image.width):
        for y in range(new_image.height):
            pixels[x, y] = border_colour
    #i = 0
    for x in range(new_image.width):
        i = 0
        for image in images:
            for y in range(i, image.height + i):
                if x < image.width:
                    pixels[x, y] = image.getpixel((x, y - i))
                ## if not then leave it as the bg colour
                        
            i += image.height + border_size
            
    return new_image    

def sort_hue(images: List[Image]) -> List[Image]:
    
    """
    Outputs the list of images sorted in ascending order of average hue.
    Value is used as a tiebreaker
    """
    
    for i in range(len(images)):
        for j in range(i + 1, len(images)):
        
            avg_hue_i, avg_sat_i, avg_val_i = average_hsv(images[i])
            avg_hue_j, avg_sat_j, avg_val_j = average_hsv(images[j])
        
            
        
            # Swap images if there is an image j, any point after i, with lower hue
            if avg_hue_j - avg_hue_i < -0.01: # avg_hue_j < avg_hue_i
                images[i], images[j] = images[j], images[i]
                
            elif abs (avg_hue_j - avg_hue_i) < 0.01: # avg_hue_j == avg_hue_i
                    
                if avg_val_j - avg_val_i < -0.01: # avg_val_j < avg_val_i
                    images[i], images[j] = images[j], images[i]
                    
    return images

def sort_saturation(images: List[Image]) -> List[Image]:
    
    """
    Outputs the list of images sorted in ascending order of average saturation.
    Value is used as a tiebreaker
    """
    
    for i in range(len(images)):
        for j in range(i + 1, len(images)):
        
            avg_hue_i, avg_sat_i, avg_val_i = average_hsv(images[i])
            avg_hue_j, avg_sat_j, avg_val_j = average_hsv(images[j])

            if avg_sat_j - avg_sat_i < -0.01: # avg_sat_j < avg_sat_i
                images[i], images[j] = images[j], images[i]
                    
            elif abs (avg_sat_j < avg_sat_i) < 0.01: # avg_sat_j == avg_sat_i
                    
                if avg_val_j - avg_val_i < -0.01: # avg_val_j < avg_val_i
                    images[i], images[j] = images[j], images[i]
                    
    return images

def create_2d_mosaic(images: List[Image], border_colour: str, border_size: int,\
            num_cols: int, x_parameter: str) -> Image:
    """
    Creates the 2d mosaic sorted by the desired parameter on the desired axis, with desired borders
    """
    
    
    
    
    if len(images) % num_cols != 0:
        mb.showwarning("Cant' create mosaic", "The number of columns is impossible")
        loading_screen.destroy()
        return None
    
    num_rows = len(images) // num_cols   ## Just to make sure it's int (not .0)... idk if it matters but it def cant hurt
    
    #sorted_images = [[0] * num_rows] * num_cols ## Initialize empty 2d list of images
    #x_sorted_images = y_sorted_images = [0] * len(images)
    
    #height = width = 0
    print("\nVerifying image size...")
    for image in images:
        if border_size > image.height * image.width:
            mb.showwarning("Error", "Massive borders compared to image sizes")
            loading_screen.destroy()
            return None
        #i += 1
        #height += image.height
        #width += image.width
    
    height = border_size * (num_rows - 1) + num_rows
    width = border_size * (num_cols - 1) + num_cols
    
    mosaic = PIL.Image.new("HSV", (width, height))
    
    
    
    if x_parameter.lower() == 'hue':
        
        
        print("\nSorting images...")
        x_sorted_images = sort_hue(images)
        columns = []
        
        
        print("\nCreating mosaic...")
        for i in range(0, len(images), num_rows):
            
            
            
                       
            curr_col = combine_images_vertically(sort_saturation(x_sorted_images[i:i + num_rows]), border_colour, border_size)
            columns.append(curr_col)
        print("Finishing up...") 
        return combine_images_horizontally(columns, border_colour, border_size)
    
    elif x_parameter.lower() == 'saturation':
        print("\nSorting images...")
        
        x_sorted_images = sort_saturation(images)
        columns = []
        print("\nCreating mosaic...")
        for i in range(0, len(images), num_rows):
            
            
                       
            curr_col = combine_images_vertically(sort_hue(x_sorted_images[i:i + num_rows]), border_colour, border_size)
            columns.append(curr_col)
        print("Finishing up...")   
        return combine_images_horizontally(columns, border_colour, border_size)
        
        
    else:
        
        return None

### Quick lazy testing
#img1 = image_from_file(load_file(IMAGE_FILE_TYPES))
#img2 = image_from_file(load_file(IMAGE_FILE_TYPES))
#bro = sort_by_colour([img1, img2])

##for pixel in img1:
    ##print ("wtf")
##print("Original heights:", img1.height, "&", img2.height, "\nFinal height:", bro.height)
##print("Original widths:", img1.width, "&", img2.width, "\nFinal width:", bro.width)
#print (bro)

#combine_images_linearly(sort_by_colour(load_image_list())).show()




"""
To do:

Document everything that is undocumented
Start gui

"""

#from Cimpl import *

#img = load_image(choose_file())
#red = green = blue = 0
#for x, y, (r, g, b) in img:
    #red += r; blue += b; green += g
#red /= (get_width(img) * get_height(img))
#green /= (get_width(img) * get_height(img))
#blue /= (get_width(img) * get_height(img))

#print ("rgb = {}".format((red, green, blue)))

print("Image Mosaic module 2020")

#if __name__ == '__main__':
    #create_2d_mosaic(load_image_list(), 'white', 3, 5, 'hue').show()