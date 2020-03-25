from source import app, db
from source import routes
from source.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


db.create_all()
app.run(host='192.168.1.31', port=8080)

