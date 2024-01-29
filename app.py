from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, User, Post, PostTag, Tag

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://glenntm:jeewiz99@localhost/tags'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'fgdds721sdf9ds'


db.init_app(app)
migrate = Migrate(app, db)

submittedValues = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tags/new', methods=['POST'])
def createTag():
    if request.method == 'POST':
        tag =  request.form['tag']
        new_tag = Tag(name=tag)
        db.session.add(new_tag)
        db.session.commit()
    
    return redirect(url_for('tagDetail', tag_id=new_tag.id))

@app.route('/tags', methods=['GET'])
def listTags():
    #query all the tags from the database
    tags = Tag.query.filter(Tag.name != '').order_by(Tag.name).all()
    return render_template('tags.html', tags=tags)

@app.route('/tags/<tag_id>')
#used to display each tag
def tagDetail(tag_id):
    tag = Tag.query.get(tag_id)
    return render_template('tag_detail.html', tag=tag)

@app.route('/tags/<tag_id>/edit')
#method to edit a tag
def editTag(tag_id):
    tag = Tag.query.get(tag_id)
    return render_template('edit_tag.html', tag=tag)

@app.route('/savetag/<tag_id>/edit', methods=['POST'])
#method to save a tag
def saveTag(tag_id):
    tag = Tag.query.get(tag_id)
    tag.name = request.form['tagName']
    db.session.commit()
    return render_template('tag_detail.html', tag=tag)

@app.route('/delete/<tag_id>', methods=['GET'])
#delete a tag
def deleteTag(tag_id):
    tag = Tag.query.get(tag_id)
    if tag:
        db.session.delete(tag)
        db.session.commit()
        return redirect(url_for('listTags'))
    return jsonify({'error': 'Tag not found'}), 404

#user information
@app.route('/users', methods=['GET'])
def getUsers():
    users = User.query.order_by(User.first_name).all()

    return render_template('users.html', users=users)

@app.route('/user/new', methods=['POST'])
def newUser():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        # this maps the values from the webapge to the right columns in the user database
        new_User = User(first_name=first_name, last_name=last_name)
        db.session.add(new_User)
        db.session.commit()
    
    return redirect(url_for('getUsers'))



if __name__ == "__main__":
    with app.app_context():
        # Create the table
        db.create_all()

    # Now you can run the app
    app.run(debug=True)