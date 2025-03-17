from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    data = request.json
    answer = data.get('answer')
    # Logic for checking the answer
    return jsonify({"message": "Correct Answer!"})

if __name__ == '__main__':
    app.run(debug=True)
