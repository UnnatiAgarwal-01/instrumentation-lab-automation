def check_alerts(temp, pressure, flow, config):
    alerts = []

    if temp > config.TEMP_LIMIT:
        alerts.append("High Temperature!")

    if pressure > config.PRESSURE_LIMIT:
        alerts.append("High Pressure!")

    if flow > config.FLOW_LIMIT:
        alerts.append("High Flow!")

    return alerts