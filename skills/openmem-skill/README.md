# OpenMem Skill

Universal skill for AI-powered development memory. Works with any AI assistant that supports skills.

## Supported AI Assistants

- **OpenClaw** - `openclaw`
- **Trae IDE** - Trae AI
- **VS Code (Cline/Cursor)** - AI assistants
- **Claude Code** - `claude code`
- **Windsurf** - AI assistant
- Any other AI assistant with skill support

## Installation

### Option 1: Use as Python Package (Recommended)

```bash
pip install openmem
```

The skill is automatically available via CLI:
- `openmem add "..."`
- `openmem search "..."`
- `openmem list`

### Option 2: Clone Repository

```bash
git clone https://github.com/jcgokart/openmem.git
cd openmem
pip install -e .
```

## Usage in AI Assistants

### OpenClaw

Add to your skills configuration:

```yaml
skills:
  - name: openmem
    path: /path/to/openmem/skills/openmem-skill
```

Or use CLI directly:
```
!openmem add "Important decision: use PostgreSQL for database"
!openmem search authentication
!openmem list --type decision
```

### Trae IDE / VS Code

Configure in your IDE settings:

```json
{
  "openmem.path": "/path/to/openmem",
  "openmem.template": "standard"
}
```

### Claude Code

Add to your CLAUDE.md or project context:

```
Use OpenMem for memory management:
- Run: openmem add "decision here"
- Search: openmem search "keyword"
```

## CLI Commands

```bash
# Initialize
openmem init
openmem init --global
openmem init --template standard

# Add memory
openmem add "We decided to use PostgreSQL" --type decision
openmem add "Bug fixed in auth module" --type issue --tags bug,auth

# Search
openmem search "PostgreSQL"
openmem search --scope both

# List
openmem list
openmem list --type decision
openmem list --type milestone

# Status
openmem status
openmem status --verbose

# Organize meeting notes
openmem organize --auto --llm ollama
```

## Python API

```python
from openmem import MemoryManager

memory = MemoryManager()

# Add memory
memory.add("Important decision", type="decision", tags=["project", "architecture"])

# Search
results = memory.search("PostgreSQL", scope="project")

# List
all_memories = memory.list(type="decision", limit=20)

# Page
page = memory.page(page=0, page_size=10)
```

## Configuration

Default locations:
- Project: `./.memory/`
- Global: `~/.memory/`

Database: `memory.db` (SQLite with FTS5)

## Features

- Full-text search with Chinese tokenization (jieba)
- BM25 ranking
- Auto-type detection with SmartTrigger
- Encrypted backups
- Version control
- Meeting notes organization with LLM

## License

MIT
