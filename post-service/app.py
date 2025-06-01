from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@postgres:5432/posts'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)

db.create_all()

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    post = Post(title=data['title'], content=data['content'])
    db.session.add(post)
    db.session.commit()
    return jsonify({'message': 'Post created'}), 201

@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([{'id': p.id, 'title': p.title, 'content': p.content} for p in posts])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
