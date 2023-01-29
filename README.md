# Django, Gulp and Live Reload
This is an example boilerplate to illustrate how to integrate Django and Gulp in order to make frontend development easier. *Heavily inspired by [The Coder Coder](https://www.youtube.com/watch?v=-lG0kDeuSJk&ab_channel=CoderCoder) for the Gulp bit*

The idea is that we can have our scss and JavaScript files centralised within a dedicated folder (`_frontend`), divided into subfolders and ultimately imported into the main `index.scss` file. Gulp will:
1. Watch any changes within the scss folder
2. Build an uglified index.css (based **only** on our `index.scss`) file within our `shared/static/css` folder, which we're importing into the `shared/templates/base.html` file
3. Replace said `base.html` file with a new one containing a new cache busting string

Additionally, I'm implementing a plugin called [django-livereload-server](https://github.com/tjwalch/django-livereload-server) to guarantee a fresh reload everytime we change any of our static files.

## Getting started
### Folder structure

1. Create a brand new project with `django-admin startproject project_name` command.
2. In the root project, create a `shared` directory. Inside, we need:
    - `static/css` directory, where we will output our processed css file
    - `static/js` directory for the JS files
    - `templates` directory, where we will put our `base.html` file
3. Create a `_frontend` directory:
    - Create a `scss` directory and place an `index.scss` in its root. This is the only file that will be processed by gulp
    - `js` directory

### Installations
We need to install several things with npm (don't forget to `npm init`!):
1. The Gulp cli if we don't have it yet: `npm i -g gulp-cli`
2. Development dependencies: `npm install --save-dev gulp sass gulp-sass gulp-postcss cssnano gulp-replacenpm install --save-dev gulp gulp-sass cssnano gulp-concat gulp-uglify gulp-replace sass gulp-postcss`

Then, for Django, we just need one additional dependency. Activate your virtual environment and install Django and django-livereload-server: `pip install Django django-livereload-server`

### Files
1. `gulpfile.js`. Feel free to just copy/paste the code from [here](./gulpfile.js)
2. In our [settings.py](./my_site/settings.py) file: 
    1. Add `livereload` to the INSTALLED_APPS list, above all other default apps
    2. Add `'livereload.middleware.LiveReloadScript'` to MIDDLEWARE_CLASSES
    3. Specify the following for templates list:
        ```python
         'DIRS': [
            BASE_DIR / "shared" / "templates"
        ],
        ```
    4. And the following, at the bottom of the file if you wish for the static files:
        ```python
        STATICFILES_DIRS = [
        BASE_DIR / "shared" / "static"
        ]   
        ```
3. In our [base.html](./shared/templates/base.html) we add the static url to `css/index.css` + `?cb=123` (mind that this will be created when we run gulp for the first time). Do the same for JS:
```html
 <link rel="stylesheet"
              href="{% static 'css/index.css' + '?cb=1674990399452' %}"/>
```

### Workflow

We will need, alas, 3 terminals. It might seem a bit tedious, but I personally believe it's worth it. Don't forget to activate the virtual environment

1. First terminal: `gulp`
2. Second terminal `python manage.py livereload` (**Important**: run this command before the runserver one)
3. Third terminal `python manage.py runserver`

I've personally implemented these two scripts in the `package.json` file:
```json
   "reload": "python manage.py livereload",
    "dev": "python manage.py runserver"
```

Like this, we can now use the base.html in our apps and they'll be linked to the index files. For development, we can just focus on our scss and js folders. Since gulp will be watching all files and subfolders, you'll get the live reload automatically. And since we're doing the trick of the cache busting, changes will be visible without having to empty the cache.

