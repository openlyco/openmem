# Contributing to OpenMem

Contributions welcome! Please follow these guidelines.

## Development Setup

```bash
# Clone repository
git clone https://github.com/jcgokart/openmem.git
cd openmem

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or venv\Scripts\activate  # Windows

# Install dependencies
pip install -e .
```

## Code Standards

### Philosophy: Readability First

> Code is read more often than it is written. — Python PEP 8

We prefer **clarity over conciseness**. More lines of code is okay if it makes the code easier to understand and review.

### Structure & Types

- **Use data classes for structured data**
  ```python
  from dataclasses import dataclass
  
  @dataclass
  class MemoryType:
      name: str
      sync_to_global: bool = False
      priority: int = 0
  ```

- **Avoid raw dicts** - Use typed classes/dataclasses instead
  ```python
  # ❌ Bad
  config = {"version": "1.0", "max": 10}
  
  # ✅ Good
  @dataclass
  class SearchConfig:
      highlight: bool = True
      tokenizer: str = "jieba"
      max_results: int = 10
  ```

- **Type hints are required** for function signatures
  ```python
  def search(self, query: str, scope: str = "project") -> List[MemoryResult]:
      ...
  ```

- **Avoid `Any` unless necessary** - Be explicit about types

### Naming Conventions

- **Classes**: `PascalCase` (e.g., `MemoryManager`, `SQLiteStorage`)
- **Functions/Variables**: `snake_case` (e.g., `add_memory`, `memory_dir`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `DEFAULT_GLOBAL_PATH`)
- **Private methods**: `_leading_underscore`

### Code Style

- **4-space indentation** (no tabs)
- **Line length**: Max 100 characters
- **Docstrings**: Required for all public classes and functions
  ```python
  def add(self, content: str, memory_type: str = "decision") -> int:
      """
      Add a new memory entry.
      
      Args:
          content: Memory content
          memory_type: Type of memory (decision, milestone, issue, etc.)
      
      Returns:
          Memory ID
      
      Raises:
          ValueError: If content is empty
      """
  ```

- **Imports**: Group by standard library, third-party, local
  ```python
  import os
  import yaml
  from typing import List, Optional
  
  from openmem.core.config import MemoryConfig
  from openmem.storage import SQLiteStorage
  ```

### Error Handling

- **Never swallow exceptions silently**
- **Provide actionable error messages**
  ```python
  # ❌ Bad
  except Exception:
      pass
  
  # ✅ Good
  except FileNotFoundError as e:
      logger.error(f"Memory database not found: {e}")
      raise MemoryError("Please run 'openmem init' first") from e
  ```

### Comments

- **Explain WHY, not WHAT**
  ```python
  # ❌ Bad
  # Increment counter
  counter += 1
  
  # ✅ Good
  # Use retry logic because SQLite may be locked by another process
  for attempt in range(3):
      ...
  ```

- **Chinese comments welcome** - This is a Chinese-language project

## Testing

```bash
# Run tests
pytest tests/

# Run with coverage
pytest --cov=openmem tests/
```

## Commit Guidelines

- Commit message format: `type: description`
- type: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`

## Code Review Principles

When reviewing code (yours or AI-generated):
1. **Can I understand it in 30 seconds?**
2. **Are types clear?**
3. **Is error handling proper?**
4. **Are there magic values that should be constants?**

---

# 中文简介

欢迎贡献！请遵循以下开发规范。

## 核心理念：可读性优先

> 代码是给人看的，不是给机器看的。

我们宁可多写几行代码，也要保证清晰易懂。

### 数据结构

- **用 dataclass 封装所有结构化数据**
- **禁止随意用 dict**，用明确的类型代替

### 命名规范

- 类名：`PascalCase`
- 函数/变量：`snake_case`
- 常量：`UPPER_SNAKE_CASE`

### 注释

- 解释**为什么**，而不是**做什么**
- 中文注释欢迎
