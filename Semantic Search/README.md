ChromaDB Learning Project
===========================

A beginner-friendly introduction to ChromaDB, an open-source embedding database for building AI applications with semantic search capabilities.

What is ChromaDB?
-----------------

ChromaDB is a vector database designed for storing and querying embeddings. It's particularly useful for:
- Semantic search applications
- Retrieval-Augmented Generation (RAG) systems
- Document similarity matching
- AI-powered content recommendations

Prerequisites
-------------

- Python 3.7 or higher
- Basic understanding of Python programming

Installation
------------

Install ChromaDB using pip:
    - pip install chromadb

Basic Usage
-----------

This project demonstrates the fundamental operations of ChromaDB:

1. Initialize Client and Create Collection

    `import chromadb`
    
    # Create a ChromaDB client
    `client = chromadb.Client()`
    
    # Create a new collection to store documents
    `collection = client.create_collection(name="first_collection")`

2. Add Documents to Collection

``` collection.add(
        documents=[
            "Chroma is an open-source embedding database.",
            "Vector databases are used for semantic search.",
            "Python is a great language for AI development."
        ],
        ids=["doc1", "doc2", "doc3"],
        metadatas=[{"source": "wiki"}, {"source": "blog"}, {"source": "notes"}]
    )
```

3. Query the Collection

``` results = collection.query(
        query_texts=["What is Chroma used for?"],
        n_results=2
    )
    
    print(results)
```

Code Structure
--------------

The main script includes:
- Client initialization: Sets up the ChromaDB client
- Collection creation: Creates a named collection to store documents
- Document insertion: Adds documents with IDs and metadata
- Semantic querying: Searches for relevant documents using natural language

Key Concepts
------------

Collections:
Collections in ChromaDB are containers for your documents and their embeddings. Each collection can store:
- Documents (text content)
- Embeddings (vector representations)
- Metadata (additional information about documents)
- IDs (unique identifiers for each document)

Embeddings:
ChromaDB automatically generates embeddings for your documents using default embedding models. These vector representations enable semantic search capabilities.

Metadata:
Additional information attached to documents that can be used for filtering and organization.

Expected Output
---------------

When you run the query, you'll see results similar to:
{
    'ids': [['doc1', 'doc2']], 
    'distances': [[0.123, 0.456]], 
    'documents': [['Chroma is an open-source embedding database.', 'Vector databases are used for semantic search.']], 
    'metadatas': [[{'source': 'wiki'}, {'source': 'blog'}]]
}

Next Steps
----------

To expand your ChromaDB knowledge, consider exploring:
- Custom embedding models
- Persistent storage
- Advanced querying with filters
- Batch operations
- Integration with other AI frameworks

Resources
---------

- ChromaDB Official Documentation: https://docs.trychroma.com/
- ChromaDB GitHub Repository: https://github.com/chroma-core/chroma
- Vector Database Concepts: https://www.pinecone.io/learn/vector-database/

Contributing
------------

This is a learning project. Feel free to experiment with different documents, queries, and ChromaDB features!

License
-------

This project is for educational purposes. ChromaDB is licensed under the Apache License 2.0.