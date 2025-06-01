import unittest
from initialize import init
import chromadb
from chromadb.utils import embedding_functions
from chromadb.utils.data_loaders import ImageLoader


class TestInitialize(unittest.TestCase):
	def test_init(self):
		clip_ef = embedding_functions.OpenCLIPEmbeddingFunction()
		image_loader = ImageLoader();
		client = chromadb.PersistentClient(path="./my_chroma_db")
		existing_collections = client.list_collections()
		collection_names = [col.name for col in existing_collections]
		self.assertIn("my_clip_collection", collection_names)
		collection = client.get_collection(
		    name="my_clip_collection",
		    embedding_function=clip_ef,
		    data_loader=image_loader
		)
		self.assertGreater(collection.count(), 0, "Collection count should be greater than 0")


if __name__ == '__main__':
	unittest.main()