import bluetooth

nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True)

for addr, name in nearby_devices:
    print(f"Found device: {name} with MAC address: {addr}")