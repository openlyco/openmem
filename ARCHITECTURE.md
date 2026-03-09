# ARCHITECTURE - 架构设计

## 整体架构

```
┌─────────────────────────────────────────┐
│              CLI 层                     │
│         (memory add/search/list)        │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│           MemoryManager                  │
│    (核心管理器：全局/项目分层)            │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│          StorageBackend                   │
│         (SQLite 存储后端)                 │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│           SQLite + FTS5                   │
│        (全文搜索 + BM25 排序)            │
└─────────────────────────────────────────┘
```

---

## 核心模块

### 1. CLI 层 (`cli/main.py`)

命令行入口，负责解析命令并调用 Manager。

### 2. MemoryManager (`core/manager.py`)

核心管理器，负责：
- 全局/项目分层管理
- 记忆的 CRUD 操作
- 搜索和分页

### 3. StorageBackend (`storage_sqlite.py`)

SQLite 存储后端，负责：
- 数据库连接（WAL 模式）
- FTS5 全文索引
- BM25 搜索排序

### 4. 配置系统 (`core/config.py`)

- 全局配置 (`~/.memory/config.yaml`)
- 项目配置 (`.memory/config.yaml`)
- 配置继承 (`extends`)

### 5. 智能触发 (`features/trigger.py`)

- NLP 分析（jieba 分词）
- 触发类型检测
- 置信度计算

### 6. 加密备份 (`features/encryption.py`)

- Fernet 加密
- 原子备份 (VACUUM INTO)

---

## 数据模型

### 记忆表 (memories)

| 字段 | 类型 | 说明 |
|:---|:---|:---|
| id | INTEGER | 主键 |
| type | TEXT | 类型 (decision/milestone/issue/knowledge) |
| content | TEXT | 内容 |
| metadata | TEXT | JSON 元数据 |
| tags | TEXT | 标签 (JSON 数组) |
| priority | INTEGER | 优先级 0-10 |
| created_at | DATETIME | 创建时间 |
| updated_at | DATETIME | 更新时间 |
| expires_at | DATETIME | 过期时间 |
| version | INTEGER | 版本号 |

### FTS5 虚拟表

```sql
CREATE VIRTUAL TABLE memories_fts USING fts5(
    content,
    tags,
    content=memories,
    content_rowid=id
);
```

---

## 分层存储

```
全局记忆:  ~/.memory/
           ├── config.yaml    # 全局配置
           └── memory.db      # 全局记忆库

项目记忆:  .memory/
           ├── config.yaml    # 项目配置（继承全局）
           ├── memory.db      # 项目记忆库
           └── rules/         # 生成的规则文件
               └── project.md
```

---

## 搜索机制

### BM25 排序

BM25 是一种基于词频的搜索排序算法：

```
score(Q, D) = Σ IDF(qi) * (f(qi,D) * (k1+1)) / 
              (f(qi,D) + k1 * (1 - b + b * |D|/avgdl))
```

优点：
- 不依赖向量模型
- 精确匹配关键词
- 支持中文分词

---

## 配置继承

```yaml
# ~/.memory/config.yaml (全局)
version: 1
storage:
  wal_mode: true
  busy_timeout: 30000

# .memory/config.yaml (项目)
extends: ~/.memory/config.yaml  # 继承全局配置
priority: 5                     # 覆盖或扩展
```

---

## 扩展性

### 添加新的存储后端

```python
class StorageBackend(ABC):
    @abstractmethod
    def add_message(self, message: Dict) -> int: ...
    
    @abstractmethod
    def search(self, query: str, limit: int) -> List[Dict]: ...
```

只需实现抽象方法即可替换存储后端。
