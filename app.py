from prometheus_client import start_http_server, Gauge
import time

# Define a sample metric
cpu_usage = Gauge('python_cpu_usage', 'CPU Usage of Python app')

if __name__ == '__main__':
    start_http_server(5000)  # Expose metrics on port 5000
    while True:
        # Update the metric here, simulating work
        cpu_usage.set(0.5)  # Example: Set a dummy value
        time.sleep(5)
