from flask_restful import Resource, reqparse
from models.truck import TruckModel
#from flask_jwt import jwt_required

class Truck(Resource):
    parser = reqparse.RequestParser();
    parser.add_argument('name',
        type=str,
        required=True,
        )
    # parser.add_argument('current_location_id',
    #     type=int,
    #     required=True)

    def get(self, name):
        truck = TruckModel.find_by_name(name)
        if truck:
            return truck.json();
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if TruckModel.find_by_name(name):
            return {'message': "The truck with name {} already exists".format(name)}, 404

        truck = TruckModel(name)

        try:
            truck.save_to_db()
        except:
            return {'message': "An error occurred inserting the truck"}, 500

        return truck.json(), 201
