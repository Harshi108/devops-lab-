# Exercise 4: Docker Networking

## Objective
Demonstrate Docker bridge networking between Flask, MySQL, and Redis.

## Files
- app.py: Flask application
- Dockerfile: Builds the Flask image
- requirements.txt: Flask dependency

## Network
Custom bridge network: my-bridge-net

## Containers
- flask-app: Flask application on port 5000
- mysql-db: MySQL database
- redis-cache: Redis cache

## Verification
- Flask homepage and health endpoint tested successfully.
- MySQL returned mysqld is alive.
- Redis returned PONG.
- docker network inspect confirmed all three containers are connected.

## Conclusion
Successfully configured a Docker bridge network for three containers.
