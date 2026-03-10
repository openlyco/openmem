"""
LLM 客户端 - 支持多种提供商
- trae: 当前 Trae 对话上下文（默认）
- ollama: 本地免费模型
- deepseek: 便宜
- openai: 标准 API
"""

import json
import os
import requests
from typing import Optional, Dict, Any
from dataclasses import dataclass
from enum import Enum


class LLMProvider(Enum):
    TRAE = "trae"
    OLLAMA = "ollama"
    DEEPSEEK = "deepseek"
    OPENAI = "openai"


@dataclass
class LLMConfig:
    provider: str = "trae"
    model: str = "default"
    api_key: Optional[str] = None
    base_url: Optional[str] = None


class LLMClient:
    """LLM 客户端"""

    def __init__(self, config: LLMConfig = None):
        self.config = config or LLMConfig()

    def chat(self, prompt: str, system_prompt: str = None) -> str:
        """调用 LLM"""
        provider = self.config.provider

        if provider == "trae":
            return self._chat_trae(prompt, system_prompt)
        elif provider == "ollama":
            return self._chat_ollama(prompt, system_prompt)
        elif provider == "deepseek":
            return self._chat_deepseek(prompt, system_prompt)
        elif provider == "openai":
            return self._chat_openai(prompt, system_prompt)
        else:
            raise ValueError(f"Unknown provider: {provider}")

    def _chat_trae(self, prompt: str, system_prompt: str = None) -> str:
        """Trae 模式：生成 prompt 让用户复制到 Trae"""
        return f"""
请帮我整理以下对话的会议纪要：

{prompt}

请按以下 JSON 格式输出：
{{"decisions": [], "todos": [], "records": []}}
"""

    def _chat_ollama(self, prompt: str, system_prompt: str = None) -> str:
        """Ollama 本地模型"""
        base_url = self.config.base_url or "http://localhost:11434"
        model = self.config.model or "qwen2.5:3b"

        url = f"{base_url}/api/chat"
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt or "你是一个会议纪要助手。"},
                {"role": "user", "content": prompt}
            ],
            "stream": False
        }

        response = requests.post(url, json=payload, timeout=120)
        response.raise_for_status()

        return response.json()["message"]["content"]

    def _chat_deepseek(self, prompt: str, system_prompt: str = None) -> str:
        """DeepSeek API"""
        api_key = self.config.api_key or os.getenv("DEEPSEEK_API_KEY")
        base_url = self.config.base_url or "https://api.deepseek.com"

        url = f"{base_url}/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.config.model or "deepseek-chat",
            "messages": [
                {"role": "system", "content": system_prompt or "你是一个会议纪要助手。"},
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(url, json=payload, headers=headers, timeout=60)
        response.raise_for_status()

        return response.json()["choices"][0]["message"]["content"]

    def _chat_openai(self, prompt: str, system_prompt: str = None) -> str:
        """OpenAI API"""
        api_key = self.config.api_key or os.getenv("OPENAI_API_KEY")
        base_url = self.config.base_url or "https://api.openai.com/v1"

        url = f"{base_url}/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.config.model or "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": system_prompt or "你是一个会议纪要助手。"},
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(url, json=payload, headers=headers, timeout=60)
        response.raise_for_status()

        return response.json()["choices"][0]["message"]["content"]


def get_llm_client(provider: str = None, model: str = None, api_key: str = None) -> LLMClient:
    """获取 LLM 客户端"""
    config = LLMConfig(
        provider=provider or "trae",
        model=model,
        api_key=api_key
    )
    return LLMClient(config)


if __name__ == "__main__":
    client = get_llm_client("trae")
    print(client.chat("测试对话内容"))
