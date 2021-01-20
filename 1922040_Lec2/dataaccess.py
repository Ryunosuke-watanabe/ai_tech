from var import Var
from db import DB
class DataAccess:
    def get_spots(self):
        query = "SELECT * FROM location_information "
        data = ()
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

    def get_lat_lng(self, loc):
        query = "SELECT location_information.lat, location_information.lng FROM location_information WHERE loc = %s "
        data = (str(loc), )
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)