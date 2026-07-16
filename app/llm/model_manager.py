"""Manages available LLM models and selection logic."""


class ModelManager:
    """Tracks available local models and handles model selection."""

    def __init__(self) -> None:
        """Initialize the model manager with default model list."""
        self.available_models: list[str] = ["llama3.2"]
        # TODO: query Ollama's /api/tags endpoint to discover installed models

    def get_default_model(self) -> str:
        """Return the default model name.

        Returns:
            str: The default model identifier.
        """
        return self.available_models[0]

    def list_models(self) -> list[str]:
        """List all available models.

        Returns:
            list[str]: Available model identifiers.

        TODO: Replace static list with a live query to Ollama.
        """
        return self.available_models
