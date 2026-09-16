# Monitoring MikroTik RouterOS 7 BGP in Zabbix

Python script to discover and to monitor BGP of MikroTik RouterOS 7 based network devices in Zabbix.

### Installation

### Usage
```
usage: ros7_bgp_zabbix.py [-h] [-p] command host username password

Monitoring MikroTik RouterOS 7 BGP in Zabbix

positional arguments:
  command       script operating mode (discover | status)
  host          device hostname or ip address
  username      device username
  password      device password

options:
  -h, --help    show this help message and exit
  -p , --peer   peer name (onle if in status mode)
  ```

### Data format returned when `discovery` parameter is passed:
```json
{
    "data": [
        {
            "{#BGPPEER}": "peer01_name"
        },
        {
            "{#BGPPEER}": "peer02_name"
        }
    ]
}
```

> When `status` parameter is passed, **1** is returned if peers status is in `established` state. Otherwise **0** is returned.