from flask import Flask, jsonify, Response
from prometheus_client import Counter, Gauge, Histogram, generate_latest, CONTENT_TYPE_LATEST
import random
import threading
import time

app = Flask(__name__)

orders_created = Counter(
    "quickcommerce_orders_created_total",
    "Total number of orders created"
)
orders_delivered = Counter(
    "quickcommerce_orders_delivered_total",
    "Total number of orders delivered"
)
pending_orders = Gauge(
    "quickcommerce_pending_orders",
    "Number of orders awaiting delivery"
)
delivery_duration = Histogram(
    "quickcommerce_delivery_duration_seconds",
    "Delivery duration in seconds",
    buckets=(60, 120, 180, 300, 600, 900, 1800)
)

pending_orders.set(5)

def simulate_deliveries():
    while True:
        new_orders = random.randint(1, 4)
        delivered = random.randint(1, 3)

        orders_created.inc(new_orders)
        orders_delivered.inc(delivered)

        current = pending_orders._value.get()
        pending_orders.set(max(0, current + new_orders - delivered))

        delivery_duration.observe(random.uniform(120, 1200))
        time.sleep(5)

threading.Thread(target=simulate_deliveries, daemon=True).start()

@app.route("/")
def home():
    return jsonify({
        "application": "Quick-Commerce Monitoring",
        "status": "running",
        "metrics_endpoint": "/metrics"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
