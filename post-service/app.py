from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo:27017/postsdb"
mongo = PyMongo(app)

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    mongo.db.posts.insert_one({'title': data['title'], 'content': data['content']})
    return jsonify({'message': 'Post created'}), 201

@app.route('/posts', methods=['GET'])
def get_posts():
    posts = mongo.db.posts.find()
    return jsonify([{'title': post['title'], 'content': post['content']} for post in posts])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
