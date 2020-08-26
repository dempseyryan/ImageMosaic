## ImageMosaic
A simple program that allows a user to select a directory containing a bunch of images, and sort them by hue and saturation, and save a mosaic as a new image.  Not terribly useful or exciting, but mostly just an exercise to get used to handling large tasks with files (e.g. systematically changing each pixel of an image using a pre-existing module, and creating a new image, etc.) as well as getting comfortable with GUI development using a pre-existing module, and gaining comfort with the software development process as a whole (conceptualization, development, testing, more development, more testing, etc.)


## INSTALLATION

Download ImageMosaic.py, user_interface.py, and runscript.py, and keep them in the same directory.  Run runscript.py to start the program.  Python must be installed.

## USAGE

- Click the load folder button to load a directory containing only the images desired.
- Choose the size of the border (1-5 pixels) using the left value spinner.  Note that this value assumes all images are the same size.  The spacing will vary if the images are different sizes.
- Use the middle spinner to choose between a black or white border/background colour.
- Use the right spinner to choose the number of columns for the final image; the number of rows will be determined accordingly based on the number of images.
- Use the 'hue'/'saturation' dropdown to select which parameter by which to sort the images horizontally.  The vertical parameter will be the one not chosen.
- Use the Run button to start the mosaic.  You will be updated periodically in the console.  When it is complete, you will be prompted to either save the final image, or abandon the work.

## BACKGROUND INFO

For information on HSV colour storage, see the following:
https://learnui.design/blog/the-hsb-color-system-practicioners-primer.html
In this page, it is considered HSB, while I've used V for value, rather than B for brightness.  It means the same thing.

## CREDITS

- This project was made possible by tkinter, and PIL modules.


Ryan Dempsey 2020.




## NEXT STEPS

If I ever have time to just screw around with this again, I would definitely like to implement a proper loading screen.  With the little time I had on top of full-time school and other responsibilities, I couldn't develop a sufficient understanding of concurrent programming to implement one (even with the tkinter widgets).  Maybe one day, but more likely is I won't touch this project ever again.
