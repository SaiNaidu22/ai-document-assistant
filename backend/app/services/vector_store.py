import chromadb

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="documents"
)


def store_chunks(chunks, embeddings):

    ids = [f"chunk_{i}" for i in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )


def search_chunks(query_embedding, top_k=3):

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results["documents"][0]