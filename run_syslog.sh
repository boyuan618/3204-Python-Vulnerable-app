#!/bin/bash
sudo tail -f /var/log/syslog | sudo /opt/sysmon/sysmonLogView > syslog
