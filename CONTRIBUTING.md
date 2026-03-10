# Contributing to OpenMem

Contributions welcome! Please follow these guidelines.

## Development Setup

```bash
# Clone repository
git clone https://github.com/jcgokart/openmem.git
cd openmem

# Install dependencies
pip install -e .
```

## Code Standards

We follow these coding standards:

- **PEP 8** - Python official style guide
- **Google Style Docstrings** - For documentation
- **Type Hints** - Required for function signatures

### Naming Conventions

| Type | Convention | Example |
|:---|:---|:---|
| Classes | PascalCase | `MemoryManager` |
| Functions/Variables | snake_case | `add_memory` |
| Constants | UPPER_SNAKE_CASE | `DEFAULT_PATH` |
| Private methods | _leading_underscore | `_internal_method` |

### Code Style

- **4-space indentation** (no tabs)
- **Line length**: Max 100 characters
- **Docstrings**: Required for all public classes/functions
- **Type hints**: Required for function signatures

### Error Handling

- Never swallow exceptions silently
- Provide actionable error messages

---

# 中文简介

欢迎贡献！

## 编码风格

- **PEP 8** - Python 官方风格
- **Google Style** - 文档字符串
- **类型提示** - 函数签名必须
- **VNPY 风格** - 数据用类封装，可读性优先
- **AlphaAlgo 实践** - 内部项目经验沉淀

## 代码审查原则

1. 30秒内能看懂吗？
2. 类型清晰吗？
3. 错误处理恰当吗？
4. 有没有魔法值？
