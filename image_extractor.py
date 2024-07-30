import pydicom
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read the DICOM file
dicom_file_path = '/Users/andynguyen/Downloads/fastmri_prostate_DICOMS/001/AX_T2/408.dcm'
dicom_dataset = pydicom.dcmread(dicom_file_path)

# Step 2: Extract the pixel data
pixel_data = dicom_dataset.PixelData

# Step 3: Convert pixel data to a numpy array
# The shape of the array can be found from the Rows and Columns attributes
image_array = np.frombuffer(pixel_data, dtype=np.uint16)
image_array = image_array.reshape(dicom_dataset.Rows, dicom_dataset.Columns)

# Step 4: Display the image (optional)
plt.imshow(image_array, cmap='gray')
plt.show()