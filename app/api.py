import json
from app import query, http_auth

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
