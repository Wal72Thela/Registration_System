from app import create_app, db
from flask_migrate import upgrade, migrate,init, stamp
from models import User
def deploy():
    """Run deployment tasks."""
    
    app= create_app()
    app.app_context().push()
    db.create_all()
    
    #Migrate database to latest version
    init()
    stamp()
    migrate()
    upgrade()
    
deploy()