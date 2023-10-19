from flask import render_template, request,redirect,url_for,flash


app = Flask(__name__)

@app.route('/')
def index():
    posts=Post.query.all()
    return render_template('index.html', posts=posts)


@app.route('/create_post',methods=['GET','POST'])
def create_post():
    if request.method == 'POST':
        title=request.form["title"]
        content=request.form["content"]
        post=Post(title=title, content=content)
        db.session.add(post)
        db.session.commit()
        flash("Successfully created","success")
        return redirect(url_for(index))
    return render_template('create_post.html')

@app.route('/view_post/<int:post_id>')
def view_post(post_id):
    post =Post.query.get(post_id)
    return render_template('view_post.html', post=post)

@app.route('/delete_post/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    post =Post.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    flash("Post deleted successfully","success")
    return redirect(url_for(index))


