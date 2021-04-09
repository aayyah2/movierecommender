import numpy as np

def euclidean_distance(vec1, vec2):
  #return euclidean distance between vec1 and vec2
  distance = np.linalg.norm(vec1 - vec2)
  return np.sqrt(distance)

def cosine_similarity(vec1, vec2):
  #return cosine_similarity value between vec1 and vec2
  dot = np.dot(vec1, vec2)
  mag1 = np.linalg.norm(vec1)
  mag2 = np.linalg.norm(vec2)
  cosTheta = dot/(mag1 * mag2)
  theta = np.arccos(cosTheta)
  return theta
