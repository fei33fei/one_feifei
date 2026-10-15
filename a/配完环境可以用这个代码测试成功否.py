# 查看Python版本
import sys
print("Python 版本:", sys.version)

# 查看PyTorch版本
import torch
print("PyTorch 版本:", torch.__version__)

# 查看CUDA版本（PyTorch所能识别的）
print("CUDA 版本（PyTorch可用的）:", torch.version.cuda)

# 检查CUDA是否可用（这是最重要的，表明PyTorch能否使用GPU）
print("CUDA 是否可用:", torch.cuda.is_available())

# 如果CUDA可用，还可以查看当前显卡和显卡数量
if torch.cuda.is_available():
    print("GPU 设备名称:", torch.cuda.get_device_name(0))
    print("GPU 数量:", torch.cuda.device_count())