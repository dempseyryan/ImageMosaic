## Ryan Dempsey summer 2020

from user_interface import *

"""
Clean up this file, re-size and move stuff
"""



## Create and initialize window
app = Tk()
app.title("Image Mosaic Wizard")
app.geometry('600x400') ## For some reason configure does not work when setting dimensions
app.configure(background="gainsboro")


## Create and initialize currently loaded folder label
loaded_folder = StringVar()
folder_loaded_text = Label(app, textvariable=loaded_folder,
                           bg="silver", fg="black")
folder_loaded_text.place(height=40, width=600, x=0, y=300)
loaded_folder.set("No folder loaded.")


## Initialize current mosaic object
curr_mosaic = Mosaic(border_size=1, border_col='black', col_num=1)


## Column number selector and label
column_number_selector = Spinbox(
    app, text="Number of columns:", values=(1,2), command= lambda: \
    curr_mosaic.adjust_parameters('column number', int(column_number_selector.get())))

column_number_selector.place(height=30, width=80, x=510, y=105)

column_number_text = Label(app, text="Number of columns:", bg="gainsboro")
column_number_text.place(height=40, width=120, x=390, y=100)


## Parameter selection button and label
with_label = Label(app, text="with", bg="gainsboro")
with_label.place(height=40, width=40, x=120, y=250)

parameter_selector = OptionMenu(app, curr_mosaic.horizontalParameter, 
                                'hue', 'saturation',)
parameter_selector.place(height=30, width=100, x=170, y=255)
curr_mosaic.horizontalParameter.set('hue')
parameter_label = Label(app, text='as the horizontal sorting parameter',
                        bg="gainsboro")
parameter_label.place(height=40, width=200, x=270, y=250)


## Border size selection and label
border_size_selector = Spinbox(app, from_=0, to=5,
                               command= lambda: 
                               curr_mosaic.adjust_parameters('border size', 
                                                             int(border_size_selector.get())))
border_size_selector.place(height=30, width=75, x=110, y=105)

border_size_text = Label(app, text="Border size (pixels): ", bg="gainsboro")
border_size_text.place(height=40, width=105, x=5, y=100)

## Border colour selection and label
border_colour_selector = Spinbox(app, values=('black', 'white'), command= lambda: \
                               curr_mosaic.adjust_parameters('border colour', 
                                                 str(border_colour_selector.get())))
border_colour_selector.place(height=30, width=75, x=310, y=105)

border_colour_text = Label(app, text="Border colour: ", bg="gainsboro")
border_colour_text.place(height=40, width=75, x=230, y=100)



## Initialize load folder button, setting command to overwrite mosaic object
## Using lambda so we can call it with an argument, that being the desired instance of Mosaic
file_load_button = Button(app, text="Load folder", bg="silver", fg="black",\
                          command= lambda: \
                          curr_mosaic.load_images_for_mosaic(loaded_folder, 
                                                             column_number_selector))

file_load_button.place(height=40, width=170, x=215, y=200)

run_button = Button(app, text="RUN", bg="silver", fg="black", command= lambda:\
                    curr_mosaic.run_mosaic())
run_button.place(height=40, width=100, x=10, y=250)


app.mainloop()