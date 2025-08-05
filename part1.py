from PIL import Image
import sys
import os

def count_black_lines_in_middle_row(image_path):
     
    # Load image in 1-bit mode (black & white)
    img = Image.open(image_path).convert("1")
    width, height = img.size
    middle_row = height // 2
    
    # 2D array which holds pixel values
    pixels = img.load()

    count = 0 
    in_black_line = False

    # Traverse the middle row to count black lines
    for x in range(width):
        if pixels[x, middle_row] == 0:      # black pixel
            if not in_black_line:           # start of a new black line
                count += 1
                in_black_line = True
        else:
            in_black_line = False           # end of a black line

    print(count)
    
    
    

if __name__ == "__main__":
    
    # Check for correct number of arguments
    if len(sys.argv) != 2:
        print("Error: Invalid number of arguments used")
        print("Expected usage: python part1.py <absolute_image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    
    # Check if the provided path is absolute
    if not os.path.isabs(image_path):
            print("Error: Please provide an absolute file path.")
            sys.exit(1)

    # Check file existence
    if not os.path.isfile(image_path):
        print("Error: File does not exist.")
        sys.exit(1)

    # Check file extension (jpg)
    if not image_path.lower().endswith((".jpg")):
        print("Error: File is not a JPG image")
        sys.exit(1)

    try:
        count_black_lines_in_middle_row(image_path)
    except Exception as e:
        print(f"Error: Could not process the image. {e}")
        sys.exit(1)
