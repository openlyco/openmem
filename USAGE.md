# USAGE - 详细用法

## 命令行 (CLI)

### init - 初始化

```bash
# 交互式初始化
memory init

# 非交互模式
memory init -y

# 指定项目路径
memory init /path/to/project

# 全局初始化（所有项目共享）
memory init --global

# 选择模板
memory init --template=minimal   # 最小配置
memory init --template=standard  # 标准配置
memory init --template=full      # 完整配置

# 指定项目名称
memory init --project-name myapp
```

### add - 添加记忆

```bash
# 自动检测类型（推荐）
memory add "我们决定使用 PostgreSQL"

# 指定类型
memory add "完成了登录功能" --type milestone

# 添加标签
memory add "使用 JWT 认证" --tags auth,jwt

# 指定优先级 (0-10)
memory add "重要决策" --priority 8

# 指定作用域
memory add "全局知识" --scope global

# 完整示例
memory add "使用 Redis 缓存" --type knowledge --tags redis,cache --priority 5
```

**类型说明：**
| 类型 | 说明 | 触发关键词 |
|:---|:---|:---|
| `decision` | 决策 | 决定、采用、实施 |
| `milestone` | 里程碑 | 完成、发布、上线 |
| `issue` | 问题 | 修复、解决、Bug |
| `knowledge` | 知识 | 技术、文档、API |

### search - 搜索

```bash
# 关键词搜索
memory search PostgreSQL

# 限制结果数量
memory search 数据库 --limit 5

# 标签搜索
memory search --tag auth

# 项目路径
memory search JWT --project /path/to/project
```

### list - 列表

```bash
# 所有记忆
memory list

# 按类型筛选
memory list --type decision
memory list --type milestone

# 限制数量
memory list --limit 50
```

### page - 分页

```bash
# 第一页，每页20条
memory page --page 0

# 指定页码和每页数量
memory page --page 2 --page-size 50
```

### status - 状态

```bash
# 查看 Memory 状态
memory status
```

---

## Python API

### 基本使用

```python
from memory import MemoryManager

# 初始化（项目级）
memory = MemoryManager(project_path="/path/to/project")

# 或全局
memory = MemoryManager()
```

### 添加记忆

```python
# 添加
memory_id = memory.add(
    content="我们决定使用 PostgreSQL",
    type="decision",
    tags=["数据库", "后端"],
    priority=5
)
```

### 搜索

```python
# 关键词搜索
results = memory.search("PostgreSQL")

# 标签搜索
results = memory.search_by_tags(["auth"])
```

### 列表

```python
# 所有
results = memory.list()

# 按类型
results = memory.list(type="decision")

# 分页
page = memory.page(page=0, page_size=20)
```

### 更新/删除

```python
# 更新
memory.update(memory_id, content="新内容", tags=["新标签"])

# 删除
memory.delete(memory_id)
```

### 关闭

```python
memory.close()
```

---

## 智能触发

添加记忆时，系统自动分析内容并检测类型：

```bash
memory add "我们决定用 JWT 做认证"
# 输出：
# 🔍 自动检测类型: decision (置信度: 0.70)
#    关键词: 决定
# ✅ 记忆已添加: ID=1
```

触发机制分析：
- 关键词检测（决定、采用、完成等）
- 否定词处理（"不重要"不会被误判）
- 程度副词（"非常重要"置信度更高）
