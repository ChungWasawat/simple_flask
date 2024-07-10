# simple_flask




### pipenv
```pip install pipenv```
```pipenv install flask```
```pipenv install --dev pytest```
```pipenv shell```

* using pytest on vscode, need to select a right python interpreter as pipenv is used in this project.

### Docker command
```docker build -t simple_flask_app:1.0.0 .```
```docker run -it --rm -p 9696:9696 simple_flask_app:1.0.0```