from flask import Flask, render_template

from controllers.members_controller import members_blueprint
from controllers.courts_controller import courts_blueprint

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(courts_blueprint)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
