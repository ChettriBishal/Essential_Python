from flask import Flask, render_template, request, url_for, redirect

import json
import logging

logger = logging.getLogger('post_logger')
logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y:%H:%M:%S',
                    level=logging.DEBUG)

post_file = 'posts.json'

app = Flask(__name__)  # every flask app must have a unique name

posts = {
    # 0: {
    #     'post_id': 0,
    #     'title': 'Hello, world',
    #     'content': 'This is my first blog post!'
    # }
}


# get the existing posts from the json file
def get_posts():
    global posts
    logger.info('Retrieving posts from json file')
    with open(post_file, 'r') as file:
        posts = json.load(file)


# save the in memory posts into json file
def save_posts():
    logger.info("Saving posts into json file")
    global posts
    with open(post_file, 'w') as file:
        json.dump(posts, file, indent=4)


@app.route('/')
def home():
    get_posts()  # get the posts while the homepage loads
    return render_template('home.html', posts=posts)


@app.route('/post/<int:post_id>')  # /post/0
def post(post_id):
    logger.info(f'Accessing Post id: {post_id}')
    # print(f'post_id {post_id}')
    # print(f'posts[0] is {posts.get("0")}')

    post_id = str(post_id)  # JSON only contains string keys
    post = posts.get(post_id)

    if not post:  # post will be none if not found
        return render_template('404.html', message=f'A post with id {post_id} was not found')
    return render_template('post.html', post=post)


# @app.route('/post/form')
# def form():
#     return render_template('create.html')


# localhost:/post/create?title=something&content=somethingElse
@app.route('/post/create', methods=['GET', 'POST'])
def create():
    get_posts()
    global posts
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_id = len(posts)
        posts[post_id] = {'id': post_id, 'title': title, 'content': content}

        print(f'{title} added into the json file')

        save_posts()  # saving posts into json file

        # takes in a function name and returns a URL and address
        # for post function return the url associated with it: /post/<int: post_id>
        return redirect(url_for('home'))

    # we no longer need form() as this will do both
    return render_template('create.html')  # GET request


if __name__ == "__main__":
    app.run(debug=True)  # gives us more information if errors occur
