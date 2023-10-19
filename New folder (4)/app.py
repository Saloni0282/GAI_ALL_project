
from flask import flask,request,jsonify
app = Flask(__name__)
posts=[]
post_id_counter=1
class Post:
    def __init__(self,username,caption):
        self.id=post_id_counter
        self.username=username
        self.caption=caption
        self.likes=0
        self.comments=[]
        post_id_counter+=1

@app.route('/posts',methods=['GET', 'POST'])

def posts():
    if request.method=='GET':
        return jsonify([post.dict for post in posts])
    elif request.method=='POST':
        data=request.json
        username=data.get('username')
        caption=data.get('caption')
        if username and caption:
            new_post=Post(username,caption)
            posts.append(new_post)
            return jsonify(new_post.dict),201
        else:
            return 'Invalid Data',400


@app.route('/posts/<int:post_id>',methods=['DELETE', 'POST'])
def h_post(post_id):
    post= post= ((p for p in posts if p.id==post_id),none) 

    if not post:
        return "Posts not found",404
    
    if request.method=="DELETE":
        posts.remove(post)
        return "Posts deleted",201
    elif request.method=="POST":
        post.likes+=1
        return jsonify(post.dict),201
    else:
        return 'Invalid data',400


@app.route('/posts/<int:post_id>',methods=['POST'])
def add_coment(post_id):
    post= ((p for p in posts if p.id==post_id),none)
    if not post:
        return "Posts not found",404
    
    data=request.json
    comments=data.get('comment')
    if comment:
        post.comments.append(comment)
        return jsonify(post.dict),201
    else:
        return 'Invalid data',400


if __name__=='__main__':
    app.run(debug=True)        