import json
import os


def load(text_path, image_directory, video_directory):


	try:
	    with open(text_path, 'r', encoding='utf-8') as file:
	        txt_data = json.load(file)

	except FileNotFoundError:
	    print(f"Error: The data file was not found.")
	except json.JSONDecodeError:
	    print(f"Error: Could not decode JSON. Check file format.")
	except Exception as e:
	    print(f"An unexpected error occurred: {e}")

	# Your documents (can be text or paths to images)
	metadata = []
	text_docs = []
	ids = []
	for item in txt_data:
	    # Ensure 'id' key exists before proceeding
	    if 'id' in item:
	        key = item['id']
	        value = item.copy()
	    text_docs.append(json.dumps(value))
	    metadata.append({"type": "text", "category": "pokemon-character"})
	    ids.append(key)

	image_paths = []

	if not os.path.exists(image_directory):
	    print(f"Error: Directory '{image_directory}' not found.")
	else:
	    for filename in os.listdir(image_directory):
	        image_paths.append(image_directory + '/' + filename)
	        metadata.append({"type": "image", "category": "pokemon-character"})
	        ids.append(filename)

	video_paths = []

	if not os.path.exists(video_directory):
	    print(f"Error: Directory '{video_directory}' not found.")
	else:
	    for filename in os.listdir(video_directory):
	        image_paths.append(video_directory + '/' + filename)
	        metadata.append({"type": "video", "category": "pokemon-character"})
	        ids.append(filename)




	documents=text_docs+image_paths+video_paths

	return documents, ids, metadata