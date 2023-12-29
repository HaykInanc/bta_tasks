from flask import Flask, request, jsonify, abort
import json

app = Flask(__name__)

def read_file(path):
    with open(path, "r") as f:
        return f.read()


# Задачи по 10.2 (10_2)


# task_1
# Обработчик GET запросов для текстового файла
@app.route('/api/task_1/<int:id>', methods=['GET'])
def handle_task_10_2_1(id):
    try:
        file_path = f"files/10_2/task_1/file_{id}.txt"
        file_content = read_file(file_path)
        return file_content, 200, {'Content-Type': 'text/plain'}
    except:
        abort(404)

# task_2
# Обработчик GET запросов для JSON
@app.route('/api/task_2/<int:id>', methods=['GET'])
def handle_task_10_2_2(id):
    try:
        file_path = f"files/10_2/task_2/file_{id}.json"
        file_content = json.loads(read_file(file_path))
        return jsonify(file_content)
    except:
        abort(404)

# task_3
# Обработчик GET запросов для текстового файла
@app.route('/api/task_3/<int:id>', methods=['GET'])
def handle_task_10_2_3(id):
    try:
        file_path = f"files/10_2/task_3/file_{id}.txt"
        file_content = read_file(file_path)
        return file_content, 200, {'Content-Type': 'text/plain'}
    except:
        abort(404)

# task_4
# Обработчик GET запросов для текстового файла
@app.route('/api/task_4/<int:id>', methods=['GET'])
def handle_task_10_2_4(id):
    try:
        file_path = f"files/10_2/task_4/{id}"
        file_content = read_file(file_path)
        return file_content, 200, {'Content-Type': 'text/plain'}
    except:
        abort(404)

# task_5
# Обработчик GET запросов для текстового файла
@app.route('/api/task_5/<int:id>', methods=['GET'])
def handle_task_10_2_5(id):
    try:
        file_path = f"files/10_2/task_5/{id}"
        file_content = read_file(file_path)
        return file_content, 200, {'Content-Type': 'text/plain'}
    except:
        abort(404)


# Задачи по 10.3 (10_3)

# task_1
# Обработчик POST запросов
@app.route('/api/task_10_3_1', methods=['POST'])
def handle_task_10_3_1():
    data = request.form

    if 'message' not in data:
        return jsonify({'error': 'Key "message" not found'}), 400

    message = data['message']
    return f"response: {message}", 200, {'Content-Type': 'text/plain'}

# task_2
# Обработчик POST запросов
@app.route('/api/task_10_3_2', methods=['POST'])
def handle_task_10_3_2():
    data = request.get_json()

    if 'name' not in data:
        return jsonify({'error': 'Key "message" not found'}), 400

    id_dict = {
        "Tom": 123,
        "Oliver": 536,
        "Isabella": 321,
        "Mateo": 733
    }

    name = data['name']
    return jsonify({"status": "success", "name": name, "id": id_dict.get(name, "")})

# task_3
# Обработчик POST запросов
@app.route('/api/task_10_3_3', methods=['POST'])
def handle_task_10_3_3():
    
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']

    if file.filename == '':
        return 'No selected file', 400

    return file.filename, 200, {'Content-Type': 'text/plain'}


# task_4
# Обработчик POST запросов
@app.route('/api/task_10_3_4', methods=['POST'])
def handle_task_10_3_4():
    authorization_header = request.headers.get('Authorization')
    if authorization_header and authorization_header.startswith('Bearer '):
        # Извлекаем токен из заголовка
        bearer_token = authorization_header.split(' ')[1]

        valid_tokens = ["R#e2bG$p", "L!k9aF#q", "X*m7nZ$u", "P@y3tH!s", "C&v8oW#x"]
        if bearer_token in valid_tokens:
            return 'gooooood!'

    return 'permission denied', 300

# task_5
# Обработчик POST запросов
@app.route('/api/task_10_3_5', methods=['POST'])
def handle_task_10_3_5():
    authorization_header = request.headers.get('Authorization')
    if authorization_header and authorization_header.startswith('Bearer '):
        # Извлекаем токен из заголовка
        bearer_token = authorization_header.split(' ')[1]

        valid_tokens = ["R#e2bG$p", "L!k9aF#q", "X*m7nZ$u", "P@y3tH!s", "C&v8oW#x"]
        if bearer_token in valid_tokens:
            return 'gooooood!'

    return 'permission denied', 300



if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)