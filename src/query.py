def run(collection, query_texts, query_image, query_video, n_results):

    if query_texts is not None:
        # Query the collection
        query_results_image = collection.query(
            query_texts=[query_texts],
            n_results=n_results,
            where={"type": "image"},
            include=['documents', 'metadatas', 'distances', 'uris']
        )
        print("Querying with text:")
        print(query_results_image)

        query_results_text = collection.query(
            query_texts=[query_texts],
            n_results=n_results,
            where={"type": "text"},
            include=['documents', 'metadatas', 'distances', 'uris']
        )
        print("Querying with text:")
        print(query_results_text)

        return query_results_text, query_results_image


    if query_image is not None:
        query_results_image = collection.query(
            query_image=[query_image],
            n_results=n_results,
            where={"type": "image"},
            include=['documents', 'metadatas', 'distances', 'uris']
        )
        print("Querying with image:")
        print(query_results_image)

        # Query the collection
        query_results_text = collection.query(
            query_image=[query_image],
            n_results=n_results,
            where={"type": "text"},
            include=['documents', 'metadatas', 'distances', 'uris']
        )
        print("Querying with image:")
        print(query_results_text)
        return query_results_text, query_results_image