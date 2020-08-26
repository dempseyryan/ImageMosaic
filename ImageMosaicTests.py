from ImageMosaic import *


def check_pixels(actual: Image, expected: Image, desc: str) -> bool:
    
    """
    Tests all pixels in an image for equality based on a function
    """
    
    print("\n\nTesting " + desc)
    failed = 0
    if expected.height != actual.height or expected.width != actual.width:
        print("Test failed.  Expected size: " + str(expected.width) + "x" + str(expected.height) + "; got: " + str(actual.width) + "x" + str(actual.height))
        return False
    
    for x in range(expected.width):
        for y in range(expected.height):
            exp = expected.getpixel((x, y))
            act = actual.getpixel((x, y))
            print("\nTesting pixel {}; Actual: {}. Expected: {}".format((x, y), act, exp))
            check = exp == act
            if check:
                print("Passed")
            else:
                failed += 1
                print("Failed")
    if failed > 0:
        print(failed, "of", actual.height * actual.width, "pixels failed.")
        return False
    print("Test passed.")
    return True

def test_hsv_overall_sort() -> bool:
    
    """
    Tests the primitive HSV sorting function and combination.
    """
    
    ## Create length-5 1-pixel test-image list
    images = [PIL.Image.new("HSV", (1, 1)), PIL.Image.new("HSV", (1, 1)),\
              PIL.Image.new("HSV", (1, 1)), PIL.Image.new("HSV", (1, 1)),\
              PIL.Image.new("HSV", (1, 1)), PIL.Image.new("HSV", (1, 1))]
    
    ## Initialize rando vals
    pixels = images[0].load(); pixels[0, 0] = (0, 0, 0)
    pixels = images[1].load(); pixels[0, 0] = (1, 0, 0)
    pixels = images[2].load(); pixels[0, 0] = (0, 1, 0)
    pixels = images[3].load(); pixels[0, 0] = (0, 0, 1)
    pixels = images[4].load(); pixels[0, 0] = (1, 0, 1)
    pixels = images[5].load(); pixels[0, 0] = (0, 0, 0)
    
    ## Resulting image
    actual = combine_images_horizontally(sort_by_colour(images), 'black', 1)
    
    ## Expected result
    expected = PIL.Image.new("HSV", (11, 1))
    pixels = expected.load()
    
    ## Initialize sorted images
    pixels[0, 0] = (0, 0, 0)
    pixels[2, 0] = (0, 0, 0)
    pixels[4, 0] = (0, 0, 1)
    pixels[6, 0] = (0, 1, 0)
    pixels[8, 0] = (1, 0, 0)
    pixels[10, 0] = (1, 0, 1)
    
    ## Initialize borders
    pixels[1, 0] = pixels[3, 0] = pixels[5, 0] = pixels[7, 0] = pixels[9, 0] = (0, 0, 0)
    
    ## Test each pixel
    return check_pixels(actual, expected, "combine (sort_by_colour(test_image), black, 1)")

def test_hue_sort() -> bool:
    """
    Tests the sort by hue
    """
    
    images = [PIL.Image.new("HSV", (1, 1)), PIL.Image.new("HSV", (1, 1)),\
              PIL.Image.new("HSV", (1, 1)), PIL.Image.new("HSV", (1, 1)),\
              PIL.Image.new("HSV", (1, 1))]
    
    ## Initialize rando vals
    pixels = images[0].load(); pixels[0, 0] = (0, 0, 0)
    pixels = images[1].load(); pixels[0, 0] = (1, 0, 0)
    pixels = images[2].load(); pixels[0, 0] = (0, 1, 1)
    pixels = images[3].load(); pixels[0, 0] = (0, 0, 1)
    pixels = images[4].load(); pixels[0, 0] = (1, 0, 1)
    
    ## Resulting image
    actual = combine_images_horizontally(sort_hue(images), 'black', 1)
    
    expected = PIL.Image.new("HSV", (9, 1))
    pixels = expected.load()
    
    ## Initialize sorted images
    pixels[0, 0] = (0, 0, 0)
    pixels[2, 0] = (0, 1, 1)
    pixels[4, 0] = (0, 0, 1)
    pixels[6, 0] = (1, 0, 0)
    pixels[8, 0] = (1, 0, 1)
    
    ## Initialize borders
    pixels[1, 0] = pixels[3, 0] = pixels[5, 0] = pixels[7, 0] = (0, 0, 0)    
    
    ## Test each pixel
    return check_pixels(actual, expected, "combine (sort_hue(test_image), black, 1)")    
    
def test_saturation_sort() -> bool:
    """
    Tests the sort by saturation
    """
    
    images = [PIL.Image.new("HSV", (1, 1)), PIL.Image.new("HSV", (1, 1)),\
              PIL.Image.new("HSV", (1, 1)), PIL.Image.new("HSV", (1, 1)),\
              PIL.Image.new("HSV", (1, 1))]
    
    ## Initialize rando vals
    pixels = images[0].load(); pixels[0, 0] = (0, 0, 0)
    pixels = images[1].load(); pixels[0, 0] = (1, 0, 1)
    pixels = images[2].load(); pixels[0, 0] = (0, 1, 1)
    pixels = images[3].load(); pixels[0, 0] = (0, 2, 1)
    pixels = images[4].load(); pixels[0, 0] = (1, 0, 0)
    
    ## Resulting image
    actual = combine_images_horizontally(sort_saturation(images), 'black', 1)
    
    expected = PIL.Image.new("HSV", (9, 1))
    pixels = expected.load()
    
    ## Initialize sorted images
    pixels[0, 0] = (0, 0, 0)
    pixels[2, 0] = (1, 0, 0)
    pixels[4, 0] = (1, 0, 1)
    pixels[6, 0] = (0, 1, 1)
    pixels[8, 0] = (0, 2, 1)
    
    ## Initialize borders
    pixels[1, 0] = pixels[3, 0] = pixels[5, 0] = pixels[7, 0] = (0, 0, 0)    
    
    ## Test each pixel
    return check_pixels(actual, expected, "combine (sort_hue(test_image), black, 1)")       
    
def test_vertical_combine() -> None:
    """
    Function was written pretty late in development so just wanted to quickly make sure it works
    """
    images = [PIL.Image.new("HSV", (1, 1)), PIL.Image.new("HSV", (1, 1)),\
              PIL.Image.new("HSV", (1, 1)), PIL.Image.new("HSV", (1, 1)),\
              PIL.Image.new("HSV", (1, 1))]
    
    ## Initialize rando vals
    pixels = images[0].load(); pixels[0, 0] = (0, 0, 0)
    pixels = images[1].load(); pixels[0, 0] = (1, 0, 1)
    pixels = images[2].load(); pixels[0, 0] = (0, 1, 1)
    pixels = images[3].load(); pixels[0, 0] = (0, 2, 1)
    pixels = images[4].load(); pixels[0, 0] = (1, 0, 0)
    
    ## Resulting image
    actual = combine_images_vertically(images, 'BlACk', 1)
    
    expected = PIL.Image.new("HSV", (1, 9))
    pixels = expected.load()
    
    ## Initialize sorted images
    pixels[0, 0] = (0, 0, 0)
    pixels[0, 2] = (1, 0, 1)
    pixels[0, 4] = (0, 1, 1)
    pixels[0, 6] = (0, 2, 1)
    pixels[0, 8] = (1, 0, 0)
    
    ## Initialize borders
    pixels[0, 1] = pixels[0, 3] = pixels[0, 5] = pixels[0, 7] = (0, 0, 0)    
    
    ## Test each pixel
    return check_pixels(actual, expected, "vert-combine (test_image, black, 1)")

def test_2d_mosaic() -> None:
    """
    Tests the 2d mosaic creator on each mode
    """
    images_hue = [PIL.Image.new("HSV", (1, 1)), PIL.Image.new("HSV", (1, 1)),\
              PIL.Image.new("HSV", (1, 1)), PIL.Image.new("HSV", (1, 1)),\
              PIL.Image.new("HSV", (1, 1)), PIL.Image.new("HSV", (1, 1))]
    
    ## Initialize rando vals
    pixels = images_hue[0].load(); pixels[0, 0] = (0, 0, 0)
    pixels = images_hue[1].load(); pixels[0, 0] = (0, 3, 1)
    pixels = images_hue[2].load(); pixels[0, 0] = (2, 1, 1)
    pixels = images_hue[3].load(); pixels[0, 0] = (1, 2, 1)
    pixels = images_hue[4].load(); pixels[0, 0] = (1, 4, 0)
    pixels = images_hue[5].load(); pixels[0, 0] = (2, 0, 1)
    
    ## Resulting image
    actual_hue = create_2d_mosaic(images_hue, 'BlACk', 1, 3, 'hUE')
    
    expected_hue = PIL.Image.new("HSV", (5, 3))
    pixels = expected_hue.load()
    
    ## Initialize sorted images
    pixels[0, 0] = (0, 0, 0)
    pixels[0, 2] = (0, 3, 1)
    
    pixels[2, 0] = (1, 2, 1)
    pixels[2, 2] = (1, 4, 0)
    
    pixels[4, 0] = (2, 0, 1)
    pixels[4, 2] = (2, 1, 1)
    
    ## Initialize borders
    pixels[0, 1] = pixels[1, 0] = pixels[1, 1] = pixels[1, 2]\
        = pixels[2, 1] = pixels[3, 0] = pixels[3, 1] = pixels[3, 2]\
        = pixels[4, 1] = (0, 0, 0)    
    
    
    images_sat = [PIL.Image.new("HSV", (1, 1)), PIL.Image.new("HSV", (1, 1)),\
              PIL.Image.new("HSV", (1, 1)), PIL.Image.new("HSV", (1, 1)),\
              PIL.Image.new("HSV", (1, 1)), PIL.Image.new("HSV", (1, 1))]
    
    ## Initialize rando vals
    pixels = images_sat[0].load(); pixels[0, 0] = (0, 0, 0)
    pixels = images_sat[1].load(); pixels[0, 0] = (0, 3, 1)
    pixels = images_sat[2].load(); pixels[0, 0] = (2, 1, 1)
    pixels = images_sat[3].load(); pixels[0, 0] = (1, 2, 1)
    pixels = images_sat[4].load(); pixels[0, 0] = (1, 1, 0)
    pixels = images_sat[5].load(); pixels[0, 0] = (2, 0, 1)
    
    ## Resulting image
    actual_sat = create_2d_mosaic(images_sat, 'BlACk', 1, 3, 'saturation')
    
    expected_sat = PIL.Image.new("HSV", (5, 3))
    pixels = expected_sat.load()
    
    ## Initialize sorted images
    pixels[0, 0] = (0, 0, 0)
    pixels[0, 2] = (2, 0, 1)
    
    pixels[2, 0] = (1, 1, 0)
    pixels[2, 2] = (2, 1, 1)
    
    pixels[4, 0] = (0, 3, 1)
    pixels[4, 2] = (1, 2, 1)
    
    ## Initialize borders
    pixels[0, 1] = pixels[1, 0] = pixels[1, 1] = pixels[1, 2]\
        = pixels[2, 1] = pixels[3, 0] = pixels[3, 1] = pixels[3, 2]\
        = pixels[4, 1] = (0, 0, 0)    
    
    ## Test each pixel for each mode
    return check_pixels(actual_hue, expected_hue, "2d mosaic hue (test_image, black, 1)") and check_pixels(actual_sat, expected_sat, "2d mosaic sat (test_image, black, 1)")


def run_all_tests() -> None:
    
    print("\nTesting functions")
    tests_passed = tests_run = 0
    tests_passed += test_hsv_overall_sort(); tests_run += 1
    tests_passed += test_hue_sort(); tests_run += 1
    tests_passed += test_saturation_sort(); tests_run += 1
    tests_passed += test_vertical_combine(); tests_run += 1
    tests_passed += test_2d_mosaic(); tests_run += 1
    if tests_passed < tests_run:
        print(tests_run - tests_passed, "of", tests_run, "tests failed.")
    else:
        print("All tests passed.")
    
if __name__ == "__main__":
    run_all_tests()