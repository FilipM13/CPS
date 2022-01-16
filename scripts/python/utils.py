import json

def make_string(key, matrix, size):
  assert isinstance(key, str)

  matrix_string = ','.join([str(sub_el) for sub_el in matrix])
  rv = ''
  rv += '{'
  rv += f'"name": "{key}_{size[0]}x{size[1]}",'
  rv += '"matrix": ['
  rv += matrix_string
  rv += ']'
  rv += '},'
  return rv

def filter_data_to_json_dict(key, matrix, size):
  assert isinstance(key, str)

  rv = {"name" : f"{key}_{size[0]}x{size[1]}", "matrix" : matrix}
  return rv