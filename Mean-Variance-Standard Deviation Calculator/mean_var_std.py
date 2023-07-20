import numpy as np

def calculate(lists):
  if len(lists) == 9:
    b = np.array(lists)
    a = b.reshape(3, 3)

    calculations = {
      'mean': [np.mean(a, axis=0).tolist(),
               np.mean(a, axis=1).tolist(),
               np.mean(a)],
      'variance': [np.var(a, axis=0).tolist(),
                   np.var(a, axis=1).tolist(),
                   np.var(a.flatten())], 
      'standard deviation': [np.std(a, axis=0).tolist(),
                             np.std(a, axis=1).tolist(),
                             np.std(a.flatten())], 
      'max': [np.max(a, axis=0).tolist(),
              np.max(a, axis=1).tolist(),
              np.max(a.flatten())], 
      'min': [np.min(a, axis=0).tolist(),
              np.min(a, axis=1).tolist(),
              np.min(a.flatten())],
      'sum': [np.sum(a, axis=0).tolist(),
              np.sum(a, axis=1).tolist(),
              np.sum(a.flatten())]
    }
    

  else: 
      raise ValueError("List must contain nine numbers.")

  return calculations
