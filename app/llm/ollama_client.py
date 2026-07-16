"""Client wrapper for communicating with a local Ollama server."""

import json

import requests
from requests.exceptions import RequestException

from app.core.config import get_settings
from app.core.exceptions import LLMConnectionError
from app.core.logger import get_logger

logger = get_logger()
settings = get_settings()


class OllamaClient:
    """Thin wrapper around the Ollama HTTP API.

    Responsible for sending prompts to a local Llama3.2 model and
    returning completions.
    """

    def __init__(self, base_url: str | None = None, model: str | None = None) -> None:
        """Initialize the Ollama client.

        Args:
            base_url: Base URL of the Ollama server. Defaults to settings value.
            model: Model name to use. Defaults to settings value.
        """
        self.base_url = (base_url or settings.ollama_base_url).rstrip("/")
        self.session = requests.Session()
        self.model = self._resolve_model(model or settings.ollama_model)

    def _resolve_model(self, model_name: str) -> str:
        """Resolve a configured model name to a valid Ollama model identifier."""
        if ":" in model_name:
            return model_name

        try:
            response = self.session.get(f"{self.base_url}/api/tags", timeout=10)
            response.raise_for_status()
            data = response.json()
        except RequestException as exc:
            raise LLMConnectionError(
                f"Unable to connect to Ollama at {self.base_url}."
            ) from exc
        except ValueError as exc:
            raise LLMConnectionError("Invalid response from Ollama when listing models.") from exc

        candidates = []
        for model in data.get("models", []):
            name = model.get("name", "")
            if name == model_name or name.startswith(f"{model_name}:"):
                candidates.append(name)

        if not candidates:
            raise LLMConnectionError(
                f"No Ollama model matching '{model_name}' was found."
            )

        selected = candidates[0]
        logger.info("Resolved Ollama model '%s' to '%s'", model_name, selected)
        return selected

    def generate(self, prompt: str) -> str:
        """Generate a completion for the given prompt.

        Args:
            prompt: The fully constructed prompt text.

        Returns:
            str: The model's generated text.
        """
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "max_tokens": 512,
            "temperature": 0.2,
        }

        try:
            response = self.session.post(url, json=payload, stream=True, timeout=120)
            response.raise_for_status()
        except RequestException as exc:
            raise LLMConnectionError("Failed to get a response from Ollama.") from exc

        output = []
        for line in response.iter_lines(decode_unicode=True):
            if not line:
                continue

            try:
                chunk = json.loads(line)
            except json.JSONDecodeError:
                continue

            if "response" in chunk:
                output.append(chunk.get("response", ""))

            if chunk.get("done"):
                break

        return "".join(output).strip()

    def stream_generate(self, prompt: str):
        """Stream a completion for the given prompt.

        Args:
            prompt: The fully constructed prompt text.

        Yields:
            str: Incremental chunks of generated text.
        """
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "max_tokens": 512,
            "temperature": 0.2,
        }

        try:
            response = self.session.post(url, json=payload, stream=True, timeout=120)
            response.raise_for_status()
        except RequestException as exc:
            raise LLMConnectionError("Failed to stream a response from Ollama.") from exc

        for line in response.iter_lines(decode_unicode=True):
            if not line:
                continue

            try:
                chunk = json.loads(line)
            except json.JSONDecodeError:
                continue

            if "response" in chunk and chunk.get("response"):
                yield chunk["response"]

            if chunk.get("done"):
                break
