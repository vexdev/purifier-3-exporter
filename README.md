# MiPurifier 3 Prometheus Exporter

A simple exporter that can read a JSON file with Xiaomi air purifiers exposes the data as prometheus metrics.

Please find the documentation here on how to obtain a token: [python-miio](https://python-miio.readthedocs.io/en/latest/).

This software only currently works with Mi Purifier version 3.
For usage with previous versions, please look into [this project](https://github.com/shrikantpatnaik/mi_purifier_exporter).

## Usage

You can run the script directly on your machine or use docker.

### Run directly

```bash
pip install -r requirements.txt
 
MI_IP=192.168.1.100 MI_TOKEN=thetokengoeshere python3 exporter.py
```

### Run with docker

```bash
docker run -d --name xiaomi-exporter -p 8000:8000 -e MI_IP=192.168.1.100 -e MI_TOKEN=thetokengoeshere vexdev/xiaomi-exporter
```