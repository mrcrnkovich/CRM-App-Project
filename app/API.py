import json
from app import query, http_auth

class clientList:
    # method to return clients by agent/username

    def get(self, username):
        abort_null_agent(username)
        clients = query.getClientsForUser(username)
        return {"clients": [client.json() for client in clients]}

    # test for POST data from API to represent a new client
    # add put method for clients, need to define format

    def post(self, username):

        data = json.loads(request.data)
        for client in data["clients"]:
            addClient(
                username, client
            )  # helper method to sanatize data, then add to database

        # update response to conform with general standards.
        return "sucess" + "\n"

    def put(self, username):
        # get client (or clients) by Id, update the included fields
        # return success, or a list of failed updates.

        pass

    def delete(self, username):
        # get client(s) be id, remove from db
        # return success or list of failed deletions.

        pass


class Clients:
    # method to return clients by agent/username

    def get(self, username, client_id):
        abort_null_agent(username)
        clients = (
            db.session.query(Client)
            .join(User)
            .filter(User.username == username)
            .filter(Client.id == client_id)
            .all()
        )
        return {"clients": [client.json() for client in clients]}

    def put(self, username, client_id, update):
        return  query.updateClient(client_id, update)


class Property:
    def get(self, property_id=None):
        if property_id:
            return query.getPropertyById(property_id).json()

        return query.getProperties()

    def post(self):
        data = json.loads(request.data)
        # for prop in data["Properties"]:
        # addProperty(username, client) # helper method to sanatize data, then add to database
        # update response to conform with general standards.
        return "sucess" + "\n"

    def put(self, property_id):
        abort_null_property(property_id)
        pass

    def delete(self, property_id):
        abort_null_property(property_id)
        pass


class Agents:
    def get(self, username=None):
        if username:
            return query.getUserByName(username).json()

        users = query.getUsers()
        return {"Users": [u.json() for u in users]}


# Check for bad arguments
class ShowingList:
    def get(self, username=None, showing_id=None):
        # abort_null_property(property_id)
        if username:
            return {"Showings": query.getShowingByUser(username)}
        elif showing_id:
            return {"Showings": query.getShowingById(showing_id)}
        else:
            return {"Showings": query.getShowings()}

    def post(self, property_id):
        pass

    def put(self, property_id):
        pass

    def delete(self, property_id):
        pass


# Move this to separate module in Home for adding/modifiying clients
# will need a method of cleaning/checking the data & catching errors.
def addClient(username, client):
    print("Adding client:")
    print(f"First Name is: {client['first_name']}")
    print(f"Last Name is: {client['last_name']}")
    query.createClient(client)
    print("Client successfully added")
    return


# Move this to separate module in Home for adding/modifiying clients
# will need a method of cleaning/checking the data & catching errors.
def addProperty(username, property):
    print("Adding Property:")
    print(f"Location: {property['Location']}")
    client = Client(
        first_name=client["first_name"],
        last_name=client["last_name"],
        email=client["email"],
        phone=client["phone"],
        user_id=client["user_id"],
    )
    db.session.add(client)
    db.session.commit()
    print("Client successfully added")
    return


"""
# move to global position
def verify(username, password):
    if not (username and password):
        return False
    user = User.query.filter_by(email=username).first()
    print(user)
    return user.check_password(password)
"""


def abort_null_agent(agent):
    if not db.session.query(User).filter_by(username=agent).first():
        abort(404, message=f"Error: Agent {agent} does not exist")


def abort_null_property(property_id):
    if not db.session.query(Properties).filter_by(Property_ID=property_id).first():
        abort(404, message=f"Property ID #{property_id} does not exist")
