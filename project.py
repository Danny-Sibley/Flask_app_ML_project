"""
Nucamp portfolio project:

1. Implement two tier structure: includes a postgres database and web app to interact with database 

2. Use docker compose to define and manage tiers

3. Manage using GitHub

4. Deploy to AWS 
- use amazon rds to host postgresql db 


- Use flask to build 
= use Docker to containerize
- Use virtual environment




"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # Pass in a puppy name
    # We insert it to the html with jinja2 templates!
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
