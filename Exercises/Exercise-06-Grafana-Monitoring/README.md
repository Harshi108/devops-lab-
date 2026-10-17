\# Exercise 6: Grafana Real-Time Monitoring of Quick-Commerce App



\## Objective

Monitor quick-commerce delivery metrics using Prometheus and Grafana.



\## Technologies

\- Python 3.12

\- Flask

\- Prometheus

\- Grafana

\- Docker

\- PromQL



\## Features

\- Simulates order creation and delivery.

\- Exposes metrics at `/metrics`.

\- Tracks created, delivered, and pending orders.

\- Measures delivery duration.

\- Visualizes metrics using Grafana.

\- Defines a Prometheus alert for high pending orders.



\## Project Files

\- `delivery\_metrics.py` - Flask metrics application.

\- `requirements.txt` - Python dependencies.

\- `Dockerfile` - Docker image configuration.

\- `prometheus.yml` - Prometheus configuration.

\- `alert\_rules.yml` - Alert rules.



\## Access URLs

\- Application: http://localhost:8000

\- Metrics: http://localhost:8000/metrics

\- Prometheus targets: http://localhost:9090/targets

\- Prometheus alerts: http://localhost:9090/alerts

\- Grafana: http://localhost:3000



\## Grafana Data Source

Use `http://host.docker.internal:9090` as the Prometheus data source URL in Grafana.



\## Alert

`HighPendingOrders` triggers when pending orders remain above 50 for one minute.



\## Note

This project uses simulated delivery data. Email and SMS notifications require additional configuration.

