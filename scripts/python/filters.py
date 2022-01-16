from dataclasses import dataclass
import numpy

@dataclass
class Filter:
  name :str
  matrix :numpy.ndarray
