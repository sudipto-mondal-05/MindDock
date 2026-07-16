"""Builds LLM-ready context strings from retrieved chunks."""


class ContextBuilder:
    """Assembles retrieved chunks into a single context block for prompts."""

    def __init__(self, max_context_chars: int = 6000) -> None:
        """Initialize the context builder.

        Args:
            max_context_chars: Maximum allowed characters in the built context.
        """
        self.max_context_chars = max_context_chars

    def build(self, chunks: list[dict]) -> str:
        """Build a context string from retrieved chunks.

        Args:
            chunks: Retrieved chunk dictionaries (text + metadata).

        Returns:
            str: The assembled context string.

        TODO: Implement truncation, deduplication, and source attribution.
        """
        raise NotImplementedError
