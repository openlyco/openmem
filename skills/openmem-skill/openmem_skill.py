#!/usr/bin/env python3
"""
OpenMem Skill Interface
Wrapper script for AI assistants to interact with OpenMem
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from openmem import MemoryManager
from openmem.cli.main import main as cli_main


def skill_add(content: str, memory_type: str = "auto", tags: str = None, scope: str = "project"):
    """Add a memory entry"""
    memory = MemoryManager()
    
    if memory_type == "auto":
        from openmem.features.trigger import SmartTrigger
        trigger = SmartTrigger()
        result = trigger.analyze(content)
        memory_type = result.trigger_type.value if result.triggered else "decision"
    
    tag_list = tags.split(",") if tags else None
    
    memory_id = memory.add(
        content=content,
        type=memory_type,
        tags=tag_list,
        scope=scope
    )
    
    memory.close()
    return {"success": True, "id": memory_id, "type": memory_type}


def skill_search(query: str, scope: str = "project", limit: int = 10):
    """Search memories"""
    memory = MemoryManager()
    results = memory.search(query=query, scope=scope, limit=limit)
    memory.close()
    return {"success": True, "count": len(results), "results": results}


def skill_list(memory_type: str = None, scope: str = "project", limit: int = 20):
    """List memories"""
    memory = MemoryManager()
    results = memory.list(type=memory_type, scope=scope, limit=limit)
    memory.close()
    return {"success": True, "count": len(results), "memories": results}


def skill_status(verbose: bool = False):
    """Show memory status"""
    global_dir = os.path.expanduser("~/.memory")
    project_dir = os.path.join(os.getcwd(), ".memory")
    
    status = {
        "global": {
            "exists": os.path.exists(global_dir),
            "path": global_dir
        },
        "project": {
            "exists": os.path.exists(project_dir),
            "path": project_dir
        }
    }
    
    if verbose:
        if os.path.exists(global_dir):
            db_path = os.path.join(global_dir, "memory.db")
            if os.path.exists(db_path):
                status["global"]["size"] = os.path.getsize(db_path)
        
        if os.path.exists(project_dir):
            db_path = os.path.join(project_dir, "memory.db")
            if os.path.exists(db_path):
                status["project"]["size"] = os.path.getsize(db_path)
    
    return status


if __name__ == "__main__":
    import json
    
    if len(sys.argv) < 2:
        print("Usage: openmem_skill.py <command> [args...]")
        print("Commands: add, search, list, status")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "add":
        content = sys.argv[2] if len(sys.argv) > 2 else ""
        memory_type = sys.argv[3] if len(sys.argv) > 3 else "auto"
        tags = sys.argv[4] if len(sys.argv) > 4 else None
        
        result = skill_add(content, memory_type, tags)
        print(json.dumps(result, ensure_ascii=False))
    
    elif command == "search":
        query = sys.argv[2] if len(sys.argv) > 2 else ""
        result = skill_search(query)
        print(json.dumps(result, ensure_ascii=False))
    
    elif command == "list":
        memory_type = sys.argv[2] if len(sys.argv) > 2 else None
        result = skill_list(memory_type)
        print(json.dumps(result, ensure_ascii=False))
    
    elif command == "status":
        verbose = "--verbose" in sys.argv or "-v" in sys.argv
        result = skill_status(verbose)
        print(json.dumps(result, ensure_ascii=False))
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
