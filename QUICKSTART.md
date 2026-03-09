# Quickstart - 5分钟上手

## 安装

```bash
pip install trae-memory
```

## 1. 初始化

```bash
# 在当前项目初始化
memory init

# 或全局初始化（所有项目共享）
memory init --global
```

## 2. 添加记忆

```bash
# 自动检测类型（推荐）
memory add "我们决定使用 PostgreSQL 数据库"

# 指定类型
memory add "完成了用户登录功能" --type milestone

# 添加标签
memory add "使用 JWT 做认证" --tags auth,jwt
```

## 3. 搜索记忆

```bash
# 关键词搜索
memory search PostgreSQL

# 标签搜索
memory search --tag auth
```

## 4. 查看列表

```bash
# 查看所有记忆
memory list

# 按类型筛选
memory list --type decision
```

## 5. 生成规则文件

```bash
# 生成 .memory/rules/project.md
memory rules
```

---

## 常用命令

| 命令 | 说明 |
|:---|:---|
| `memory init` | 初始化 |
| `memory add "内容"` | 添加记忆（自动检测类型） |
| `memory search 关键词` | 搜索 |
| `memory list` | 列表 |
| `memory rules` | 生成规则文件 |
| `memory backup` | 备份 |
| `memory version` | 版本历史 |

---

## 下一步

- 查看 [USAGE.md](USAGE.md) 了解详细用法
- 查看 [ARCHITECTURE.md](ARCHITECTURE.md) 了解架构设计
