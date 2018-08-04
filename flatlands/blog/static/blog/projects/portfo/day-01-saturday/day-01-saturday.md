### STARTING A VIRTUAL ENV USING PIPENV[link]

I've only recently been using pipenv - i'd been using miniconda previously. I found they pretty much cover the same ground. ultimately switched to pipenv for no good reason other than its smaller scope. both are great.

    ```
    :code$ mkdir portfo
    :code$ cd portfo
    :code/portfo$ pipenv install
    ```

I find when building both back and frontend on a personal project, its super helpful to build them out at the same time. at this point the database and ui are so fluid its best to stay in this place as long as possible.

### [USING FLASK[Link] AS OUR OUR FRAMEWORK]

flask is fantasic. i can run a web server with an index page in like 8 lines of code. granted its all development and should *not* be used for production. You can. but dont.

Before we can use Flask we need to install it in the virtual environment.

    ```
    :code/portfo$ pipenv install flask
    ```

[MINIMUM REQUIRED FOR A FLASK APP]

/portfo/portfo/app.py

    ```
    from flask import Flask, render_template

    app = Flask(__name__)

    @app.route('/')
    def index():
        test = {'test': 'test'}
        return render_template('index.html', test=test)


    if __name__ == '__main__':
        app.run()
    ```

/portfo/portfo/templates/index.html

    ```
    <html>
    <head></head>
    <body>
    {{test}}
    </body>
    </html>
    ```

thats it, ridiculous.

[BASIC MODELS]

building out the models i try and only include the 'required to work' columns.

    ```
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(64), index=True, unique=True)
        password_hash = db.Column(db.String(128))

        def __repr__(self):
            return '<User %r>' % self.username


    class Image(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        filename = db.Column(db.String())


    class Folio(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(), default="portfo v0.1.0")

    ```

My thoughts were i'll need a user and their media. but then i also thought that if i just add another table and setup relationships this could be pretty scalable to support many users having many portfolios. Thats a bit grand for this project but i did decide to leave it loosly wired (whats yagni?) - just in case...

so its intended state is to have one app per user.

moving on to writing the utility functions and views. at this point i should really just test the database using the interactive interupter. but if im being completely honest most of the code at this point has been frankensteined from other projects that i know work. as with all frankensteined code that i know work, i spend more time print debugging naming errors etc. using the interactive interupter wins everytime...

At this point we have a 'required to work' database with basic crude utility functions wrapping sqlalchemy returning data to the only view.

[BASIC CONFIG]

/portfo/portfo/config.py

    ```
    import os


    basedir = os.path.abspath(os.path.dirname(__file__))

    class Config(object):
        """required"""
        title = 'portfo v0.1'
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'lkjhkj2h34kj2l3h4lk2j34hl2k2l3kj4h'
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'test.db')
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    ```

[INITIAL VIEW]

/portfo/portfo/app.py

    ```
    @flaskapp.app.route('/')
    def index():
            folio = model.Folio.query.filter_by(id=1).first()
            images = get_images()

            return render_template('index.html', images=images)
    ```

Once you've got basic crud working on the frontend in as basic html as possible, its a good time to start fleshing out the actual models and how to access the data. i like to keep a boarder between the database and the views. a super basic wrapper around the minimal sql/sqlalchemy needed to set and retrive the data. reusability, frankenstining.

[FLESH OUT THE HERO PAGE]

developing the 'hero' page
--
The portfolio page, or the hero page needed to be minimal, mostly focused on the presenting of images and no other major distractions. a simple title and possibly a small caption, or bullet points.

keeping within the realm of my original requirements i want the user to be able to somewhat customize their portfolio. being able to rename the site, and the captions as well as being able to toggle their visibility would be a must. being able to change the layout of the images would be great, but not in this current scope.

What's typical in the arch viz industry (and i imagine visual portfolios in general) is to have a screen full of images, maybe some sort of hover effect and a light box for the images once clicked.

I went with monsry.js in the end, but also dabbled with monsryry.js and pure css solutions. After deciding how the images were to be arranged I went ahead looking for lightbox ideas.


* backend
* forms
* test data
* frontend
* login management
* uploading
