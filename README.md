# Orientify
## Hardware (Scholz, Rechberger):

## Software (Baumgartner, Ecker, Krenn):
Der Winkel von einem Sound wird über MQTT an die Software übertragen und dann in einem Kompass dargestellt. Im Hintergrund werden die Daten in einer Datenbank gespeichert und im nachhinein Analysen bereitgestellt.

Technologie:
- Datenbank
    - Postgres oder Cloud DB
- Backend
    - Python FastAPI
- MQTT Broker
    - Kommuniziert mit DB und Frontend (Websockets)
- MQTT -> DB Service
    - Speichert die Daten vom MQTT Broker in die Datenbank
- Frontend
    - Livetracking und Verlauf
    - Svelte
