from PIL import Image
from collections import deque
import sys
import os


def count_black_islands(image_path):
    
    # Load image in 1-bit mode (black & white)
    img = Image.open(image_path).convert("1")
    width, height = img.size

    # Convert image to 2D grid where 1 = black, 0 = white 
    grid = []
    for y in range(height):
        row = []
        for x in range(width):
            pixel = img.getpixel((x, y))            # pixel value (0 for black, 255 for white)
            row.append(1 if pixel == 0 else 0)      # Add to 2D grid, 1 for black and 0 for white
        grid.append(row)

    # BFS helper function
    def bfs(start_y, start_x):
        q = deque()                                 # q is queue needed for BFS
        q.append((start_y, start_x))
        visited[start_y][start_x] = True

        while q:
            y, x = q.popleft()
            for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
                ny, nx = y + dy, x + dx
                if 0 <= ny < height and 0 <= nx < width:
                    if not visited[ny][nx] and grid[ny][nx] == 1:
                        visited[ny][nx] = True
                        q.append((ny, nx))

    # 2D array to track visited cells. Initially all cells are unvisited and therefore set to False
    visited = [[False] * width for _ in range(height)] 
    
    island_count = 0

    # Traverse the grid to find islands
    for y in range(height):
        for x in range(width):
            if grid[y][x] == 1 and not visited[y][x]:
                bfs(y, x)
                island_count += 1

    print(island_count)




if __name__ == "__main__":
    
    # Check for correct number of arguments
    if len(sys.argv) != 2:
        print("Error: Invalid number of arguments used")
        print("Expected usage: python part2.py <absolute_image_path>")
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
        count_black_islands(image_path)
    except Exception as e:
        print(f"Error: Could not process the image. {e}")
        sys.exit(1)

