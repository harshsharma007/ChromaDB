import chromadb;

client = chromadb.Client()

collection = client.create_collection(name="first_collection")

collection.add(
    documents=[
        "Chroma is an open-source embedding database.",
        "Vector databases are used for semantic search.",
        "Python is a great language for AI development."
    ],
    ids=["doc1", "doc2", "doc3"],
    metadatas=[{"source": "wiki"}, {"source": "blog"}, {"source": "notes"}]
)

results = collection.query(
    query_texts=["What is Chroma used for?"],
    n_results=2
)

print(results)