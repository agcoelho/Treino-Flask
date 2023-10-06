from FakePinterest import app, database
from FakePinterest.models import Foto, Usuario

with app.app_context():
    database.create_all()
