# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, jsonify, json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bidderCode = db.Column(db.String(50))
    auctionId = db.Column(db.String(50))
    bidderRequestId = db.Column(db.String(50))
    bidData = db.Column(db.Text)
   
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/addEventToDb', methods=['POST'])
# ‘/’ URL is bound with hello_world() function.
def add_event_to_db():
    print(request.data)
    data = request.get_data().decode('utf-8')
    json_data = json.loads(data)

    bidder_code = json_data.get('bidderCode')
    auction_id = json_data.get('auctionId')
    bidder_request_id = json_data.get('bidderRequestId')
    bids = json_data.get('bids')

    event = Event(bidderCode=bidder_code, auctionId=auction_id, bidderRequestId=bidder_request_id, bidData=json.dumps(bids))
    db.session.add(event)
    db.session.commit()

    response = {'message': 'Event added successfully'}

    return jsonify(response)

@app.route('/listEventToDb', methods=['GET'])
# ‘/’ URL is bound with hello_world() function.
def list_events():
    events = Event.query.all()
    event_list = []
    for event in events:
        event_dict = {
            'id': event.id,
            'bidderCode': event.bidderCode,
            'auctionId': event.auctionId,
            'bidderRequestId': event.bidderRequestId,
            'bidData': event.bidData
        }
        event_list.append(event_dict)
    return jsonify(event_list)

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()