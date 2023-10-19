from flask import Flask

app = Flask(__name__)  # every flask app must have a unique name

posts = {
    0: {
        'title': 'Hello, world',
        'content': 'This is my first blog post!'
    }
}

@app.route('/')
def home():
    return 'Salvation lies within'

@app.route('/post/<int:post_id>') # /post/0
def post(post_id):
    post = posts.get(post_id)
    return f"Post {post['title']}, content: \n\n {post['content']}"

if __name__ == "__main__":
    app.run(debug=True)  # gives us more information if errors occur
