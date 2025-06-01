import chromadb
from chromadb.utils import embedding_functions
from chromadb.utils.data_loaders import ImageLoader

def init():
	# Initialize the OpenCLIP embedding function
	clip_ef = embedding_functions.OpenCLIPEmbeddingFunction()

	# Create a Chroma client (in-memory for this example, or PersistentClient for disk)
	#client = chromadb.Client() # non-persistent
	client = chromadb.PersistentClient(path="./my_chroma_db") # persistent
	image_loader = ImageLoader();

	# Create a collection with the CLIP embedding function
	# Get a list of existing collections
	existing_collections = client.list_collections()

	# Check if the collection name is in the list of existing collections
	collection_names = [col.name for col in existing_collections]

	if "my_clip_collection" in collection_names:
		print(f"Collection already exists.")
		collection = client.get_collection(
		    name="my_clip_collection",
		    embedding_function=clip_ef,
		    data_loader=image_loader
		)
		already_exists = True
	else:
		print(f"Collection does not exist. Creating it...")
		collection = client.create_collection(
		    name="my_clip_collection",
		    embedding_function=clip_ef,
		    data_loader=image_loader
		)
		already_exists = False

	return collection, already_exists