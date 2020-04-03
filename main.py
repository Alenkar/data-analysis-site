from source import app, db
from source import routes, models, errors
from source.logger import Logger

app.debug = False

logger = Logger()

db.create_all()

exit(0)

if 1:
    app.run(host='localhost', port=8080)
else:
    context = ('local.crt', 'local.key')
    app.run(host='192.168.1.31', port=8080, ssl_context=context)

