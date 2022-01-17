import json

from filter_generators import make_blur_matrix, make_sharp_matrix
from utils import make_string, filter_data_to_json_dict

BLUR_SIZES = [  # each must be [ positive int,  positive int]
  [3,3],
  [5,5],
  [10,10],
  [20,20],
  [40,40],
  [20,5],
  [5,20],
  [40,5],
  [5,40],
  [20,3],
  [3,20],
  [40,3],
  [3,40]
]

SHARPEN_SIZES = [ # each must be [odd positive  int, odd positive  int]
  [3,3],
  [5,5],
  [7,7],
  [9,9],
  [11,11],
  [21,21],
  [9,5],
  [11,5],
  [21,5],
  [5,9],
  [5,11],
  [5,21],
  [9,3],
  [11,3],
  [21,3],
  [3,9],
  [3,11],
  [3,21]
]

#%% sharpen
sharp_matrices = [] # for json string
sharp_matrices_dict = [] # for dict to jason
for n in SHARPEN_SIZES:
  l = make_sharp_matrix(n)
  # string
  out_string = make_string('sharpen', l, n)
  sharp_matrices.append(out_string)
  # dict
  new_filter_dict = filter_data_to_json_dict('sharpen', l, n)
  sharp_matrices_dict.append(new_filter_dict)
sharp_matrices = ''.join(sharp_matrices)

#%% blur
blur_matrices = [] # for json string
blur_matrices_dict = [] # for dict to jason
for n in BLUR_SIZES:
  l = make_blur_matrix(n)
  # string
  out_string = make_string('blur', l, n)
  blur_matrices.append(out_string)
  # dict
  new_filter_dict = filter_data_to_json_dict('blur', l, n)
  blur_matrices_dict.append(new_filter_dict)
blur_matrices = ''.join(blur_matrices)

#%%write json string to txt file
# with open('filters.txt', 'w') as note:
#   final_string = ''.join([sharp_matrices, blur_matrices])
#   final_string = final_string.removesuffix(',')
#   note.write(final_string)

#%%write dict to json file
filters = sharp_matrices_dict + blur_matrices_dict
final_json_dict = {"generated filters" : filters}
with open("generated_filters.json", 'w') as f:
  json.dump(final_json_dict, f)