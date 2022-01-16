#%% IMPORTS
from filters import Filter
from PIL import Image, ImageOps
import json
import os
import numpy
from scipy import ndimage

#%% CONSTANT VARIABLES
key = "lena"
JSON_SOURCE_FILE = './test.json'
JSON_SOURCE_FILE = os.path.realpath(JSON_SOURCE_FILE)

IMAGE_FILE = '../../resources/lena.jpg'
IMAGE_FILE = os.path.realpath(IMAGE_FILE)

#%% IMPORTING FILTER DATA FROM JSON FILE
with open(JSON_SOURCE_FILE) as file:
  filters_data = json.load(file)

#%% CONVERTING FILTER DATA TO FILTER OBJECTS
generated_filters = [Filter(f['name'], numpy.array(f['matrix'])) for f in filters_data["generated filters"]]
#custom_filters = [Filter(f['name'], numpy.array(f['matrix'])) for f in filters_data["custom filters"]]

#%% IMPORTING IMAGE
image = Image.open(IMAGE_FILE)

#%% FILTERING IMAGE AND SAVING RESULT IMAGE
image = ImageOps.grayscale(image)
gray_image = numpy.array(image)
filtered_images = {}

for filt in generated_filters:
  _kernel = filt.matrix
  _rv = ndimage.convolve(gray_image, _kernel)
  filtered_images[filt.name] = Image.fromarray(_rv, 'L')

# for filt in custom_filters:
#   _kernel = filt.matrix
#   _rv = ndimage.convolve(gray_image, _kernel)
#   filtered_images[filt.name] = Image.fromarray(_rv, 'L')

#%% SAVE IMAGES
image.save(f'../../resources/modified/{key}_gray.jpg')
for k, v in filtered_images.items():
  v.save(os.path.realpath(f'../../resources/modified/{key}/{key}_'+k+'.jpg'))
