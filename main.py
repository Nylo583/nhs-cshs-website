import time
import json
from markupsafe import Markup, escape
import markdown
from flask import Flask, render_template, request, redirect
from flask_navigation import Navigation

app = Flask(__name__)
nav = Navigation(app)

nav.Bar('top', [
  nav.Item('Home', 'index'),
  nav.Item('News & Activities', 'news'),
  nav.Item('About', 'about'),
  nav.Item('Chapters', 'chapters'),
])

metadata = open("./templates/components/metadata.html", "r").read()
footer = open("./templates/components/footer.html", "r").read()
scrollTop = open("./templates/components/scrollTop.html", "r").read()

#News and posts:
#Markup attribute (in posts.json) stores source markdown of what is stored in the body.

posts = []

with open('posts.json', 'r') as openfile:
  posts = json.load(openfile)['posts']

#Public Routes:


@app.route('/')
def index():
  return render_template('index.html',
                         metadata=metadata,
                         nav=render_template('/components/nav.html'),
                         posts=posts,
                         footer=footer,
                         scrollTop=scrollTop)


@app.route('/news')
def news():
  return render_template('news.html',
                         metadata=metadata,
                         nav=render_template('/components/nav.html'),
                         posts=posts,
                         length=len(posts),
                         footer=footer,
                         scrollTop=scrollTop)


@app.route('/about')
def about():
  return render_template('about.html',
                         metadata=metadata,
                         nav=render_template('/components/nav.html'),
                         footer=footer,
                         scrollTop=scrollTop)


@app.route('/chapters')
def chapters():
  return render_template('chapters.html',
                         metadata=metadata,
                         nav=render_template('/components/nav.html'),
                         footer=footer,
                         scrollTop=scrollTop)


#Admin:
tokens = [
  'dYFW62YfCREuwFYfKQA8G7bh', 'aTVCqZSwKtRL5beP8nWSPsnK',
  'dq7RHS2FV5Zb5NMmLyVDpFnG', 'mXnXpLHvKRsF8tTjR8WP2bgw',
  'asJLyDvgPq2HQMZ8Wq9PAaCT'
]


def verifyToken(
    cookies):  #Basic authentication using token stored in browser cookies
  if 'token' in cookies:
    token = cookies.get('token')
    if (token not in tokens):
      return '401: Authentication token invalid.'
  else:
    return '400: Bad Request. Token not provided.'
  return True


@app.route('/posts/<id>/manage', methods=['POST'])
def modifyPost(id):
  id = int(id)
  auth = verifyToken(request.cookies)
  if (auth != True): return auth
  if not 0 <= id < len(posts):
    id = len(posts);
    posts.append({})
  #Save post
  posts[id] = {
    'title': escape(request.form['title']),
    'timestamp': time.ctime(),
    'markup': escape(request.form['markup']), #Source markup for future editing
    'body': markdown.markdown(request.form['markup']), #Markdown to HTML
    'img': escape(request.form['img']),
    'imgDesc': escape(request.form['imgDesc']),
  }
  json_object = json.dumps({'posts': posts}, indent=4)
  with open("posts.json", "w") as outfile:
    outfile.write(json_object)
  return redirect('/news', code=302)
  #return redirect('/posts/manage/' + str(id), code=302)


@app.route('/posts/<id>/manage', methods=['GET'])
def managePost(id):
  id = int(id)
  auth = verifyToken(request.cookies)
  if (auth != True): return auth
  if not 0 <= id < len(posts):
    return render_template('postManager.html',
                       id=len(posts),
                       title='',
                       timestamp=time.ctime(),
                       markup='',
                       img='',
                       imgDesc='')
    #return '404: Post not found.'
  return render_template('postManager.html',
                         id=id,
                         title=Markup(posts[id]['title']),
                         timestamp=posts[id]['timestamp'],
                         markup=Markup(posts[id]['markup']),
                         img=Markup(posts[id]['img']),
                         imgDesc=Markup(posts[id]['imgDesc']))


#Initialize:

app.run(host='0.0.0.0', port=81, debug=True)
