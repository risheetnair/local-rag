import typer
from pathlib import Path

app = typer.Typer(help="Local RAG CLI (free + local)")

@app.command()
def ingest(path: Path):
    """
    Ingest a file or directory into the vector store.
    """
    # TODO: call ingest pipeline
    typer.echo(f"[todo] ingest from: {path}")

@app.command()
def ask(question: str, k: int = 4):
    """
    Ask a question using retrieval-augmented generation.
    """
    # TODO: call ask pipeline
    typer.echo(f"[todo] question: {question} (k={k})")

if __name__ == "__main__":
    app()