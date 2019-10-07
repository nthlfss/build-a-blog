  
from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:lcblog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(500))

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        post_title = request.form['title']
        post_body = request.form['body']
        new_post = Blog(title=post_title, body=post_body)
        db.session.add(new_post)
        db.session.commit()
    
    entries = Blog.query.order_by(Blog.id.desc())
    return render_template('blog.html', pagetitle="Build A Blog!", entries=entries)




if __name__ == '__main__':
    app.run()