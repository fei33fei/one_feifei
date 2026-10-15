def check_library(module_name, import_name=None):
    """检测库是否安装并返回版本信息"""
    try:
        module = __import__(module_name if import_name is None else import_name)
        version = getattr(module, '__version__', 'unknown')
        print(f"✓ {module_name}: {version}")
        return True
    except ImportError:
        print(f"✗ {module_name}: 未安装")
        return False

print("=" * 50)
print("Python 环境库检测")
print("=" * 50)

# 核心库
check_library('torch')
check_library('numpy', 'numpy')
check_library('pandas')
check_library('scipy')
check_library('scikit-learn', 'sklearn')

# 深度学习框架
check_library('tensorflow')
check_library('jax')
check_library('paddle')

# ML/数据处理
check_library('transformers')
check_library('datasets')
check_library('tiktoken')
check_library('accelerate')
check_library('peft')
check_library('trl')
check_library('bitsandbytes')
check_library('flash_attn')

# 训练监控
check_library('wandb')
check_library('tensorboard')

# 可视化
check_library('matplotlib')
check_library('seaborn')
check_library('PIL', 'pillow')

# 工具库
check_library('tqdm')
check_library('requests')
check_library('huggingface_hub')

# GPU 加速
check_library('cupy', 'cupy')

print("=" * 50)
print("检测完成！")
print("=" * 50)

