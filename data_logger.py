def log_data(temp, pressure, flow):
    with open("data_log.txt", "a") as f:
        f.write(f"{temp}, {pressure}, {flow}\n")