from flask import Flask, jsonify, request
from fast_flights import FlightData, Passengers, Result, get_flights

app = Flask(__name__)

@app.route('/flights')
def flights():
    result: Result = get_flights(
        flight_data=[
            FlightData(
                date=request.args.get('date'),
                from_airport=request.args.get('from'),
                to_airport=request.args.get('to'),
            )
        ],
        trip="one-way",
        seat="economy",
        passengers=Passengers(adults=1),
        fetch_mode="fallback",
    )
    return jsonify({
        "current_price": result.current_price,
        "price": result.flights[0].price,
        "airline": result.flights[0].name,
        "departure": result.flights[0].departure,
        "arrival": result.flights[0].arrival,
        "duration": result.flights[0].duration,
        "stops": result.flights[0].stops,
    })

@app.route('/health')
def health():
    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
