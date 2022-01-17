#%% IMPORTS
from filters import Filter
from PIL import Image, ImageOps
import json
import os
import numpy
from scipy import ndimage

#%% CONSTANT VARIABLES
key = "baboon2"

JSON_SOURCE_FILE1 = './generated_filters.json'
JSON_SOURCE_FILE1 = os.path.realpath(JSON_SOURCE_FILE1)

JSON_SOURCE_FILE2 = './custom_filters.json'
JSON_SOURCE_FILE2 = os.path.realpath(JSON_SOURCE_FILE2)

IMAGE_FILE = '../../resources/baboon2.jpg'
IMAGE_FILE = os.path.realpath(IMAGE_FILE)

#%% IMPORTING FILTER DATA FROM JSON FILE
with open(JSON_SOURCE_FILE1) as file:
  filters_data1 = json.load(file)
with open(JSON_SOURCE_FILE2) as file:
  filters_data2 = json.load(file)

#%% CONVERTING FILTER DATA TO FILTER OBJECTS
filters_data = filters_data1["generated filters"] + filters_data2['custom filters']
generated_filters = [Filter(f['name'], numpy.array(f['matrix'])) for f in filters_data]

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


#%% SAVE IMAGES
image.save(f'../../resources/modified/{key}_gray.jpg')
for k, v in filtered_images.items():
  v.save(os.path.realpath(f'../../resources/modified/{key}/{key}_'+k+'.jpg'))
