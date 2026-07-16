# MindDock AI 🧠

A local, private AI-powered document assistant. Upload PDFs, DOCX, and TXT
files, then chat with them, generate summaries, build quizzes, run semantic
search, and track everything on an analytics dashboard — all running on
your own machine.

> **Status:** Project skeleton only. AI/RAG logic (embeddings, Ollama calls,
> ChromaDB retrieval, summarization, quiz generation, search) is **not yet
> implemented** — see the roadmap below.

## Features (planned)

- 📤 Upload PDF / DOCX / TXT documents
- 💬 Chat with your documents (RAG over local LLM)
- 📝 Automatic summarization
- ❓ Quiz generation
- 🔍 Semantic search
- 📊 Analytics dashboard
- 🗂️ Document management

## Architecture

MindDock AI follows a layered architecture:

```
Presentation Layer   (Streamlit frontend)
        │
API Layer             (FastAPI routers)
        │
Service Layer          (business logic)
        │
Repository Layer     (SQLite / Chroma / filesystem)
        │
External Services      (Ollama, ChromaDB, disk)
```

## Folder structure

```
MindDock/
├── app/                    # FastAPI backend
│   ├── api/                # Routers, dependencies, middleware
│   ├── core/                # Config, logging, constants, security, exceptions
│   ├── models/              # Pydantic request/response & domain models
│   ├── services/            # Business logic (chat, summary, quiz, search...)
│   ├── repositories/        # SQLite / Chroma / file / history persistence
│   ├── llm/                 # Ollama client, prompt manager, model manager
│   ├── retrieval/           # Chunking, embedding, retrieval, reranking
│   ├── parsers/              # PDF / DOCX / TXT parsers + factory
│   ├── database/             # SQLite connection, schema, migrations
│   ├── utils/                # Validators, helpers, formatters, file utils
│   └── main.py                # FastAPI app entrypoint
├── frontend/                # Streamlit UI
│   ├── Home.py
│   ├── pages/                 # Dashboard, Upload, Chat, Summary, Quiz, Search, Settings
│   ├── components/           # navbar, sidebar, cards, uploader, chat window
│   └── assets/                # styles.css
├── prompts/                  # Prompt templates (TODO)
├── storage/                  # uploads / processed / exports / temp
├── vector_db/                # ChromaDB persistence directory
├── data/                     # SQLite database file
├── tests/                    # Test suite (TODO)
├── docs/                     # Additional documentation (TODO)
├── requirements.txt
├── .env.example
├── run.py
└── README.md
```

## Installation

```bash
git clone <this-repo>
cd MindDock
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

You'll also need [Ollama](https://ollama.com) installed locally with the
`llama3.2` model pulled:

```bash
ollama pull llama3.2
```

## Running the backend (FastAPI)

```bash
python run.py
# or
uvicorn app.main:app --reload
```

- Swagger docs: http://localhost:8000/docs
- Health check: http://localhost:8000/health

## Running the frontend (Streamlit)

```bash
streamlit run frontend/Home.py
```

## Roadmap

- [ ] Implement document parsing pipeline (PDF/DOCX/TXT → text)
- [ ] Implement chunking + embedding + ChromaDB storage
- [ ] Implement RAG-based chat via Ollama
- [ ] Implement summarization service
- [ ] Implement quiz generation service
- [ ] Implement semantic search service
- [ ] Implement dashboard analytics aggregation
- [ ] Wire Streamlit pages to live API endpoints
- [ ] Add authentication / multi-user support
- [ ] Add automated test suite

## License

TBD.
