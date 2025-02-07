import torch
import os

# 检查是否是 WSL 环境
def is_wsl():
    return 'WSL_INTEROP' in os.environ

print("Is WSL:", is_wsl())

# 检查 CUDA 是否可用
print(torch.cuda.is_available())

# 打印 CUDNN 版本
print(torch.backends.cudnn.version())