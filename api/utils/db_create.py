from api.server import create_app
from api.extensions import sql

sql.create_all(app=create_app())
