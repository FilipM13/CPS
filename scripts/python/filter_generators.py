import numpy as np

def make_sharp_matrix(shape :[int, int]) -> list[list[int]]:
  # validate
  assert shape[0] > 0
  assert isinstance(shape[0], int)
  assert shape[0]%2 == 1
  assert shape[1] > 0
  assert isinstance(shape[1], int)
  assert shape[1]%2 == 1

  rv = []
  for i in range(shape[0]):
    if i == shape[0]//2:
      sub_rv = [-1 for _ in range(shape[1]//2)]
      sub_rv.append(shape[0]+shape[1]-1)
      sub_rv.extend([-1 for _ in range(shape[1]//2)])
      rv.append(sub_rv)
    else:
      sub_rv = [0 for _ in range(shape[1]//2)]
      sub_rv.append(-1)
      sub_rv.extend([0 for _ in range(shape[1]//2)])
      rv.append(sub_rv)
  return rv

def make_blur_matrix(shape :[int, int]) -> list[list[int]]:
  # validate
  assert shape[0] > 0
  assert isinstance(shape[0], int)
  assert shape[1] > 0
  assert isinstance(shape[1], int)

  rv = np.ones((shape[0], shape[1]))
  rv = rv / (shape[0] * shape[1])
  rv = [list(np_ndarray) for np_ndarray in rv]
  return rv