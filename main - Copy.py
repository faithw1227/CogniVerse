from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/more-info')
def more_info():
    return render_template('more_info.html')

@app.route('/about-us')
def about_us():
    return render_template('about_us.html')

@app.route('/brain-training-games')
def brain_training_games():
    return render_template('brain_training_games.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    return f'Search results for: {query}'
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    # Simple response logic; replace with more complex logic or AI
    reply = f"You said: {user_message}"
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
