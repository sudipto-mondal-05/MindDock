"""Retrieves relevant chunks for a given query from the vector store."""


class Retriever:
    """Coordinates embedding a query and fetching similar chunks."""

    def __init__(self) -> None:
        """Initialize the retriever.

        TODO: Inject Embedder and ChromaRepository dependencies.
        """
        pass

    def retrieve(self, query: str, document_ids: list[str] | None = None, top_k: int = 5) -> list[dict]:
        """Retrieve the most relevant chunks for a query.

        Args:
            query: The user's search or chat query.
            document_ids: Optional subset of documents to restrict retrieval to.
            top_k: Number of chunks to retrieve.

        Returns:
            list[dict]: Retrieved chunks with metadata and scores.

        TODO: Implement embed-then-query pipeline.
        """
        raise NotImplementedError
