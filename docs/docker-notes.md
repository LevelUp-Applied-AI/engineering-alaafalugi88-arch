# Docker Notes — Day 9

## Docker Version

Docker is installed and running successfully on my machine.

## Postgres Container

Command used:

docker run -d --name pg-prework -e POSTGRES_PASSWORD=prework -p 5432:5432 postgres:15-alpine

This command runs a PostgreSQL container in detached mode using the official postgres:15-alpine image.

## Startup Logs

Command used:

docker logs pg-prework

Startup confirmation line found:

LOG: database system is ready to accept connections

## Stop and Restart

Commands used:

docker stop pg-prework

docker restart pg-prework

The container stopped and restarted successfully.

## Issues Encountered

None