from var import Var
from db import DB
class DataAccess:
    def get_spots_sensitivity(self, loc):
        query = "SELECT location_sensitivity.fun, location_sensitivity.history, location_sensitivity.view, location_sensitivity.nature FROM location_sensitivity WHERE loc = %s "
        data = (str(loc), )
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

    def get_spots_sensitivity2(self, loc):
        query = "SELECT location_sensitivity.loc, location_sensitivity.fun, location_sensitivity.history, location_sensitivity.view, location_sensitivity.nature FROM location_sensitivity WHERE loc != %s "
        data = (str(loc), )
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

    def get_lat_lng(self, loc):
        query = "SELECT location_sensitivity.lat, location_sensitivity.lng FROM location_sensitivity WHERE loc = %s "
        data = (str(loc), )
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

    def get_lat_lng2(self, loc):
        query = "SELECT location_sensitivity.loc, location_sensitivity.lat, location_sensitivity.lng FROM location_sensitivity WHERE loc != %s "
        data = (str(loc), )
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

    def get_open_close(self, loc):
        query = "SELECT location_sensitivity.open_time, location_sensitivity.close_time FROM location_sensitivity WHERE loc = %s "
        data = (str(loc), )
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

    def get_open_close2(self, loc):
        query = "SELECT location_sensitivity.loc, location_sensitivity.open_time, location_sensitivity.close_time FROM location_sensitivity WHERE loc != %s "
        data = (str(loc), )
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)