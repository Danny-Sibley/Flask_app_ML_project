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

from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/resume')
def resume():

    return render_template('resume.html')


@app.route('/thankyou')
def thankyou():

    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)
