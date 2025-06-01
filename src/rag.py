from initialize import init
from load_data import load
from query import run
import os

def main(question, image_question, video_question):

    collection, already_exists = init()

    text_path = os.getenv('TEXT_PATH')
    image_directory = os.getenv('IMAGE_DIRECTORY')
    video_directory = os.getenv('VIDEO_DIRECTORY')

    documents, ids, metadata = load(text_path, image_directory, video_directory)

    if already_exists == False:
        # Add documents to the collection. The embedding_function will be used here.
        collection.add(
            documents=documents,
            metadatas=metadata,
            ids=ids
        )


    query_results_text, query_results_image = run(collection, question, image_question, video_question, 1)

    return query_results_image


