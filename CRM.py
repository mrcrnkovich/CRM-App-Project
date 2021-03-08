from app import crm, db
from app.models import User, Client


@crm.shell_context_processor
def make_shell_context():
    return {}

if __name__ == '__main__':
    crm.run()
