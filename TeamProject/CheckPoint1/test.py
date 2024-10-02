from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

# Load the image

image = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'ref_col_p.png')) # Replace with your image path
  # Ensure the image is in RGB format

# Convert image to numpy array
image_array = np.array(image)

# Extract LSB by performing bitwise AND operation with 1 (to keep only the least significant bit)
lsb_array = image_array & 1

# Scale the LSB values for visibility (optional)
lsb_array = lsb_array * 255

# Display the extracted LSB plane
plt.imshow(lsb_array)
plt.axis('off')  # Remove axis for clarity
plt.show()
