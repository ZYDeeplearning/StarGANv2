import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
import torch
a=torch.Tensor([[2,5,2],[2,3,1]])
b=a.pow(2)
print(b)
b=b.sum(1)
print(b.shape)
