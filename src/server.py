from flask import Flask, request, jsonify, render_template, send_file
from rag import main

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/ask', methods=['POST'])
def ask():
	
	question = request.form.get("question")


	query_results_text = main(question, None, None)

	return send_file(query_results_text["documents"][0][0], mimetype='image/png')



@app.route('/ask2', methods=['GET', 'POST'])
def ask2():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return render_template('index.html', message='No file part in the request.')

        file = request.files['file']

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return render_template('index.html', message='No selected file.')

        if file and allowed_file(file.filename):
            # Secure the filename to prevent directory traversal attacks
            filename = secure_filename(file.filename)
            file_path = os.path.join(os.getenv('UPLOAD_FOLDER'), filename)
            file.save(file_path)
            # After saving, you can redirect the user or show a success message
            return render_template('index.html', message=f'File "{filename}" uploaded successfully!', uploaded_filename=filename)
        else:
            return render_template('index.html', message='Invalid file type. Allowed types: pdf, png, jpg, jpeg')

    # For GET requests, just render the upload form
    return render_template('index.html')



@app.route('/ask3', methods=['GET', 'POST'])
def ask3():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return render_template('index.html', message='No file part in the request.')

        file = request.files['file']

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return render_template('index.html', message='No selected file.')

        if file and allowed_file(file.filename):
            # Secure the filename to prevent directory traversal attacks
            filename = secure_filename(file.filename)
            file_path = os.path.join(os.getenv('UPLOAD_FOLDER'), filename)
            file.save(file_path)
            # After saving, you can redirect the user or show a success message
            return render_template('index.html', message=f'File "{filename}" uploaded successfully!', uploaded_filename=filename)
        else:
            return render_template('index.html', message='Invalid file type. Allowed types: mp3, mp4')

    # For GET requests, just render the upload form
    return render_template('index.html')


if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8000)

