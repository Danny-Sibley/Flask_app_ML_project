# Home Price Predictor
---

### Running Locally 
To run locally clone this repo
```
git clone https://github.com/Danny-Sibley/Flask_app_ML_project.git
``` 

To create virtual env
```
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

To run app
```
gunicorn -w 4 'app:app'
```