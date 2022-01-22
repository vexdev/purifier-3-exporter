import time
import json
import sys
import os

import purifier
from miio import exceptions


# noinspection PyProtectedMember
from prometheus_client import start_http_server, Gauge

status = None

aqi = Gauge('mi_purifier_aqi', 'AQI from Purifier', ['name'])
temp = Gauge('mi_purifier_temp', 'Temperature from Purifier', ['name'])
humidity = Gauge('mi_purifier_humidity', 'Humidity from Purifier', ['name'])
filter_life_remaining = Gauge('mi_purifier_filter_life', 'Filter life in percent from Purifier', ['name'])
motor_speed = Gauge('mi_purifier_motor_speed', 'Active motor speed', ['name'])


def exit_with_error(error):
    sys.exit(error)


if __name__ == '__main__':
    port_number = 8000

    token = os.getenv('MI_TOKEN')
    ip = os.getenv('MI_IP')
    port_number = os.getenv('MI_PORT', 8000)

    purifier = purifier.AirPurifierMiot(ip=ip, token=token)
    start_http_server(port_number)

    while True:
        time.sleep(10)
        try:
            purifier.set_property("aqi_heartbeat", 1)
            status = purifier.status()
            if status.aqi:
                aqi.labels("air").set(status.aqi)
            if status.temperature:
                temp.labels("air").set(status.temperature)
            if status.humidity:
                humidity.labels("air").set(status.humidity)
            if status.filter_life_remaining:
                filter_life_remaining.labels("air").set(status.filter_life_remaining)
            if status.motor_speed:
                motor_speed.labels("air").set(status.motor_speed)
        except exceptions.DeviceException as error:
            pass
        except OSError as error:
            pass
