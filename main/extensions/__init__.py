from flask_migrate import Migrate
from flask_login import LoginManager
from models.models import User

migrate = Migrate()
login_manager = LoginManager()

login_manager.login_view = "routes.login"  # Redirigir si no ha iniciado sesión
login_manager.login_message = "Por favor, inicia sesión para acceder a esta página."
login_manager.login_message_category = "warning"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))