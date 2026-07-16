"""Reranks retrieved chunks to improve relevance ordering."""


class Reranker:
    """Applies a reranking strategy to retrieved chunks."""

    def __init__(self, strategy: str = "none") -> None:
        """Initialize the reranker.

        Args:
            strategy: Reranking strategy identifier (e.g. 'none', 'cross-encoder').
        """
        self.strategy = strategy

    def rerank(self, query: str, chunks: list[dict]) -> list[dict]:
        """Rerank chunks based on relevance to the query.

        Args:
            query: The original search/chat query.
            chunks: Chunks retrieved from the vector store.

        Returns:
            list[dict]: Reranked chunks.

        TODO: Implement a real reranking strategy (e.g. cross-encoder model).
        """
        raise NotImplementedError
