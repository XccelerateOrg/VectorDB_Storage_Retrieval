from local_embedder.DB_handler import deserialize_document_from_database

if __name__ == '__main__':
    while True:
        query = input("Enter a topic to retrieve documents [q to quit]: ")
        if query == 'q':
            break

        retrieved_documents = deserialize_document_from_database(query)
        for doc in retrieved_documents["documents"][0]:
            print(doc)
            print("*" * 50)

        print("=" * 25, "END OF QUERY", "=" * 25)
