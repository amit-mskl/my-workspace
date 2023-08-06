import numpy as np
from PIL import Image

def sliding_average(image_path, grid_size):
    # Step 1: Read the image into a numpy array
    img = Image.open(image_path)
    img_array = np.array(img)

    # Step 2: Apply sliding window and calculate the average for each grid
    height, width = img_array.shape[:2]
    for y in range(0, height - grid_size[0] + 1):
        for x in range(0, width - grid_size[1] + 1):
            grid = img_array[y:y+grid_size[0], x:x+grid_size[1]]
            avg_color = np.mean(grid, axis=(0, 1))
            center_y, center_x = y + grid_size[0] // 2, x + grid_size[1] // 2
            img_array[center_y, center_x] = avg_color

    # Step 3: Save the modified numpy array back to an image
    modified_image = Image.fromarray(img_array)
    modified_image.save("modified_image.png")

if __name__ == "__main__":
    image_path = "path/to/your/image.jpg"  # Replace with the path to your image
    grid_size = (5, 5)
    sliding_average(image_path, grid_size)
