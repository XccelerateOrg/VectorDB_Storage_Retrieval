import numpy as np

from config import *
import chromadb
from chromadb.config import Settings
from local_embedder.embeddings import bge_base_embeddings as embedding

database_client = chromadb.PersistentClient(path=docs_cache)


def serialize_document_to_database(pdf, bookname):
    document_collection = database_client.get_or_create_collection(name=document_collection_name,
                                                                   embedding_function=embedding.embed_documents,
                                                                   metadata={"hnsw:space": "ip"})
    max_doc_count = document_collection.count()
    new_metadata = []

    indx = 0

    chunked_text = []
    while indx < len(pdf):
        chunk = pdf[indx: indx + context_len]
        chunked_text.append(chunk)
        indx += context_len - overlap

    for i in range(len(chunked_text)):
        new_metadata.append({"book_name": bookname, "chunk_id": i + 1})

    new_indxs = np.arange(len(chunked_text)) + max_doc_count

    document_collection.add(documents=chunked_text,
                            metadatas=new_metadata,
                            ids=list(map(str, new_indxs)))

    return None


def deserialize_document_from_database(query):
    try:
        doc_collection = database_client.get_collection(name=document_collection_name,
                                                        embedding_function=embedding.embed_documents)
        query_results = doc_collection.query(query_texts=query,
                                             n_results=5,
                                             include=["metadatas",
                                                      "documents"])
        return query_results
    except:
        return {"documents": [[]], "metadatas": [[]]}
