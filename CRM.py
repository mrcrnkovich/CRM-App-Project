from app import crm, db
from app.models import User, Client

@crm.shell_context_processor
def make_shell_context():
    return{}
