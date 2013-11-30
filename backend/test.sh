curl -i -H "Content-Type: application/json" -X POST -d '{"name": "Friedrich", "pickup_id": 10, "time": "8:00"}' http://localhost:5000/commutecalc/api/drivers
curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/commutecalc/api/drivers
curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/commutecalc/api/drivers/3
curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/commutecalc/api/pickups
