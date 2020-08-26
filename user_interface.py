## ui 
## Ryan Dempsey 2020


from tkinter import *
from ImageMosaic import *
from typing import *
from tkinter import messagebox as mb
from tkinter import filedialog
from tkinter.ttk import Progressbar
import sys

def close_request(window, child_window) -> None:
    """
    Closes all app windows if the progress bar is closed
    """
    
    if mb.askokcancel("Process underway", "Would you like to cancel the process and terminate the program?"):
        child_window.destroy()
        window.destroy()
        sys.exit()
        
class Mosaic:
    """
    Contains info about desired images and parameter
    """
    
    def __init__(self, path=None, imagenames=None, images=None, final=None,\
                 border_col=None, border_size=None, col_num=None):
        """
        Creates a mosaic object, containing info about folder and images
        """
        self.horizontalParameter = StringVar()
        self.path = path; self.imagenames = imagenames; self.images = images
        self.final = final; self.border_col = border_col
        self.border_size = border_size; self.col_num = col_num
    
    
    def create_mosaic(self) -> Image:
        """
        Creates the mosaic
        """
        
        if self.imagenames == None or self.horizontalParameter == None:
            
            return None
        
        self.final = create_2d_mosaic(self.images, self.border_col, self.border_size, self.col_num, str(self.horizontalParameter.get()))
        
        return self.final
    
    def run_mosaic(self) -> str:
        """
        Creates the mosaic and prompts for save
        """
        
        if self.path == None:
            mb.showwarning("No folder selected", "Select a folder before running")
            return
        #print(current_mosaic.horizontalParameter.get())
        
        ## If all the info is there, create a loading window bc this process is lengthy
        
        #loading_screen = Toplevel(parent_app)
        #loading_screen_label = Label(loading_screen, text="Preparing image")
        #loading_screen.geometry('300x100')
        #loading_title = Label(loading_screen, text="Preparing the sorted mosaic. Please wait...")
        #loading_title.place(height=20, width=300, x=10, y=10)
        #loading_screen_label.pack()
        #loading_title.pack()
        
        ### Loading bar
        #progress = Progressbar(loading_screen, orient=HORIZONTAL, mode='indeterminate')
        #progress.place(height=20, width=280, x=10, y=50)
        
        ### Define the close request fn for the loading window
        #loading_screen.protocol("WM_DELETE_WINDOW", lambda: \
                                #close_request(parent_app, loading_screen))
        #progress.start(interval=None)
        
        ### Start the loading window and create the mosaic
        #loading_screen.mainloop()
        self.create_mosaic()
        
        ### If the loading screen was already destroyed, then the program is over
        #try:
            #loading_screen.destroy()
        #except:
            #sys.exit()
        
        ## Ask the user to save the new image, and do so
        save_mos = mb.askokcancel("Mosaic complete", "Would you like to save it?")
        
        if save_mos:
            saved = filedialog.asksaveasfile(filetypes=IMAGE_FILE_TYPES, defaultextension='.jpg')
            if saved == None:
                mb.showinfo("Not saved", "The mosaic was not saved.")
                return
            self.final.convert("RGB").save(str(saved.name))
            mb.showinfo("Mosaic saved", "The image was saved as " + str(saved.name))
        else:
            mb.showinfo("Not saved", "The mosaic was not saved.")
            return None
        return str(saved.name)
    
    def load_images_for_mosaic(self, text: StringVar, col_spinbox: Spinbox) -> None:
        """
        Designed for call from button; assigns properties to pre-existing Mosaic obj,
        and then updates the warning text using the tkinter string type
        """
        
        
        images, filenames, original_path = load_images()
        
        ## If file window closed/cancelled, dont overwrite mosaic object
        if images == [] or filenames == [] or original_path == '':
            return
        
        ## If valid input, overwrite mosaic object and reflect the change onscreen
        self.path = original_path
        self.imagenames = filenames
        self.images = images
        text.set("Currently loaded:\n" + self.path)
        
        spin_vals = []
        for i in range(1, len(images) + 1):
            if len(images) % i == 0:
                spin_vals.append(i)
        
        col_spinbox.config(values=spin_vals)
        return
    
    def adjust_parameters(self, parameter: str, value) -> None:
        
        if parameter == 'border size':
            self.border_size = value
        elif parameter == 'border colour':
            self.border_col = value
        elif parameter == 'column number':
            self.col_num = value
        
        return
            
    
## Old code before methods were implemented
    
#def load_images_for_mosaic(current_mosaic: Mosaic, text: StringVar, col_spinbox: Spinbox) -> None:
    #"""
    #Designed for call from button; assigns properties to pre-existing Mosaic obj,
    #and then updates the warning text using the tkinter string type
    #"""
    
    
    #images, filenames, original_path = load_images()
    
    ### If file window closed/cancelled, dont overwrite mosaic object
    #if images == [] or filenames == [] or original_path == '':
        #return
    
    ### If valid input, overwrite mosaic object and reflect the change onscreen
    #current_mosaic.path = original_path
    #current_mosaic.imagenames = filenames
    #current_mosaic.images = images
    #text.set("Currently loaded:\n" + current_mosaic.path)
    
    #spin_vals = []
    #for i in range(1, len(images) + 1):
        #if len(images) % i == 0:
            #spin_vals.append(i)
    
    #col_spinbox.config(values=spin_vals)
    #return

#def adjust_parameters(current_mosaic: Mosaic, parameter: str, value) -> None:
    
    #if parameter == 'border size':
        #current_mosaic.border_size = value
    #elif parameter == 'border colour':
        #current_mosaic.border_col = value
    #elif parameter == 'column number':
        #current_mosaic.col_num = value
            
 
#def run_mosaic(current_mosaic: Mosaic) -> None:
    #if current_mosaic.path == None:
        #mb.showwarning("No folder selected", "Select a folder before running")
        #return
    ##print(current_mosaic.horizontalParameter.get())
    #current_mosaic.create_mosaic()
    #save_mos = mb.askokcancel("Mosaic complete", "Would you like to save it?")
    
    #if save_mos:
        #saved = filedialog.asksaveasfile(filetypes=IMAGE_FILE_TYPES, defaultextension='.jpg')
        #current_mosaic.final.convert("RGB").save(str(saved.name))
        #mb.showinfo("Mosaic saved", "The image was saved as " + str(saved.name))
    #else:
        #mb.showinfo("Not saved", "The mosaic was not saved.")