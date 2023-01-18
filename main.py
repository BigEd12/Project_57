from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391')
    blog_posts = response.json()
    return render_template("index.html", all_posts=blog_posts)

@app.route('/post/<int:blog_id>')
def get_blog_post(blog_id):
    response = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391')
    blog_posts = response.json()
    blog_post = blog_posts[blog_id - 1]
    return render_template("post.html", post=blog_post)

if __name__ == "__main__":
    app.run(debug=True)
