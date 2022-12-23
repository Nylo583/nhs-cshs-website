from markupsafe import Markup
from flask import Flask, render_template
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

posts = [
    {
        'title': 'Mr. Sands Loves Cats',
        'timestamp': '''''',
        'markup': '''''',
        'body': '''What's up guys look at this cool cat
                <br><br><br>
                It looks funny and cute 
                <br><br>
                ~Charlie Sands''',
        'img': 'kitty',
        'imgDesc': 'The cat that looks funny and cute',
    },
    {
        'title': 'Nolan Huyck CEO',
        'timestamp': '''''',
        'markup': '''''',
        'body': '''My name is Nolan Huyck
                <br><br><br>
                I have a dream that I will pass AP CSP
                <br><br>
                ~Nolan Huyck''',
        'img': 'kitty',
        'imgDesc': 'The cat that looks funny and cute',
    },
    {
        'title': 'Official Applauded Member: Luke Davey',
        'timestamp': '''''',
        'markup': '''''',
        'body': '''The oyster is my world
                <br><br><br>
                <br>
                <br><br>
                ~Luke Davey''',
        'img': 'luke_davey',
        'imgDesc': 'Luke Davey',
    },
]

#Routes:

@app.route('/')
def index():
    return render_template('index.html', metadata=metadata, nav=render_template('/components/nav.html'), posts=posts, footer=footer, scrollTop=scrollTop)

@app.route('/news')
def news():
    return render_template('news.html', metadata=metadata, nav=render_template('/components/nav.html'), posts=posts, length=len(posts), footer=footer, scrollTop=scrollTop)

@app.route('/about')
def about():
    return render_template('about.html', metadata=metadata, nav=render_template('/components/nav.html'), footer=footer, scrollTop=scrollTop)

@app.route('/chapters')
def chapters():
    return render_template('chapters.html', metadata=metadata, nav=render_template('/components/nav.html'), footer=footer, scrollTop=scrollTop)


#Initialize:

app.run(host='0.0.0.0', port=81, debug=True)