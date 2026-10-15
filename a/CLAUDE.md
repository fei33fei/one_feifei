# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python development environment testing project. It contains simple scripts to verify that ML/Deep Learning dependencies are properly installed.

## Scripts

- `a.py` - Tests if core ML libraries are installed (torch, numpy, transformers, datasets, tiktoken, wandb, tqdm)
- `gpu.py` - Tests CuPy and CUDA GPU availability
- `配完环境可以用这个代码测试成功否.py` - Tests PyTorch and CUDA environment setup
- `debug.py` - Simple fibonacci function (note: contains a bug - returns incorrect values)

## Running Scripts

Run any script with Python:
```bash
python a.py
python gpu.py
python 配完环境可以用这个代码测试成功否.py
python debug.py
```

## Notes

- This is a lightweight validation project, not a complex application
- No build system, test framework, or linting is configured
- Files use Chinese naming convention for some scripts
