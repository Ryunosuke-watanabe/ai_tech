from var import Var
from db import DB
class DataAccess:
    def get_spots_sensitivity(self, loc):
        query = "SELECT fun, history, view, nature FROM spot_time_table WHERE loc = %s "
        data = (str(loc), )
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

    def get_spots_sensitivity2(self, loc):
        query = "SELECT loc, fun, history, view, nature FROM spot_time_table WHERE loc != %s "
        data = (str(loc), )
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

    def get_lat_lng(self, loc):
        query = "SELECT lat, lng FROM spot_time_table WHERE loc = %s "
        data = (str(loc), )
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

    def get_lat_lng2(self, loc):
        query = "SELECT loc, lat, lng FROM spot_time_table WHERE loc != %s "
        data = (str(loc), )
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

    def get_open_close(self, loc):
        query = "SELECT open_time, close_time FROM spot_time_table WHERE loc = %s "
        data = (str(loc), )
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

    def get_open_close2(self, loc):
        query = "SELECT loc, open_time, close_time FROM spot_time_table WHERE loc != %s "
        data = (str(loc), )
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)