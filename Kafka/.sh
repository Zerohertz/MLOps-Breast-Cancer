docker compose -p kafka -f kafka-docker-compose.yaml up -d
docker compose -p target -f target-docker-compose.yaml up -d

curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d @source_connector.json
curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d @sink_connector.json

# docker compose -p kafka down
# docker compose -p target down