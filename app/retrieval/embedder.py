"""Generates vector embeddings for text chunks."""


class Embedder:
    """Wraps the embedding model used to vectorize text chunks."""

    def __init__(self, model_name: str = "nomic-embed-text") -> None:
        """Initialize the embedder.

        Args:
            model_name: Name of the embedding model to use.
        """
        self.model_name = model_name
        # TODO: initialize embedding client (Ollama embeddings endpoint or similar)

    def embed_text(self, text: str) -> list[float]:
        """Generate an embedding vector for a single text string.

        Args:
            text: Input text to embed.

        Returns:
            list[float]: The embedding vector.

        TODO: Implement actual embedding call.
        """
        raise NotImplementedError

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        """Generate embedding vectors for a batch of texts.

        Args:
            texts: List of input texts to embed.

        Returns:
            list[list[float]]: The embedding vectors.

        TODO: Implement batched embedding call.
        """
        raise NotImplementedError
