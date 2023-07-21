# flask-blueprints

## Synopsis

Register all Flask Blueprints (including nested) from a package directory.

## Usage

Create an empty package `app.blueprints` and register your blueprints:

```python
from flask import Flask
from flask_blueprints import register_blueprints


app = Flask(__name__)
register_blueprints(app, 'app.blueprints')
```

Blueprints can now be placed under this package, as such:

```
.
└── app
    ├── blueprints
    │   ├── account
    │   │   ├── account.py
    │   │   ├── contact
    │   │   │   ├── contact.py
    │   │   │   └── __init__.py
    │   │   └── __init__.py
    │   ├── api
    │   │   ├── account
    │   │   │   ├── account.py
    │   │   │   ├── contact
    │   │   │   │   ├── contact.py
    │   │   │   │   └── __init__.py
    │   │   │   └── __init__.py
    │   │   ├── __init__.py
    │   │   └── user
    │   │       ├── __init__.py
    │   │       └── tribute.py
    │   ├── __init__.py
    │   └── project
    │       ├── documents.py
    │       ├── __init__.py
    │       ├── project.py
    │       └── search.py
    └── __init__.py
```


Blueprint `__init__.py` files should look something like the following:

```python
from flask import Blueprint


bp = Blueprint('project', __name__)
from . import documents
from . import project
from . import search
```

(Note that the top-level `app/blueprints/__init__.py` is not a blueprint
package, and therefore should not have a blueprint defined.)

The blueprint files themselves can then define the routes. For example:

```python
from flask import redirect, url_for
from . import bp

@bp.post('/project/<int:project_id>/store')
def store(project_id):
	# ...
	return redirect(url_for('project.show', project_id=project_id))
```

If the blueprint variable is not `bp`, then this can be customised:

```python
register_blueprints(app, 'app.blueprints', bp='bp')
```


## Further Reading

 * [`importlib` — The implementation of `import`](https://docs.python.org/3/library/importlib.html)
 * [`pkgutil` — Package extension utility](https://docs.python.org/3/library/pkgutil.html)
 * [Modular Applications with Blueprints](https://flask.palletsprojects.com/en/2.3.x/blueprints/)
