docker compose -p kafka down
docker compose -p target down
docker compose -p stream down

cd ../Database
docker compose up -d
cd ../FastAPI
docker compose up -d
cd ../Kafka
docker compose -p kafka -f kafka-docker-compose.yaml up -d
docker compose -p target -f target-docker-compose.yaml up -d

echo Waiting for connectors...
sleep 10
echo Done!

curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d @source_connector.json
curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d @sink_connector.json
cd ../Stream
cp ../Kafka/.env ./
docker compose -p stream -f stream-docker-compose.yaml up -d