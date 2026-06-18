import fastf1
import matplotlib.pyplot as plt

fastf1.Cache.enable_cache('./cache')

session = fastf1.get_session(2023, 'Bahrain', 'R')
session.load()  # full load now, with telemetry

fastest_lap = session.laps.pick_fastest()
telemetry = fastest_lap.get_car_data().add_distance()

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(telemetry['Distance'], telemetry['Speed'])
ax.set_xlabel('Distance (m)')
ax.set_ylabel('Speed (km/h)')
ax.set_title(f"Fastest Race Lap Speed Trace — {fastest_lap['Driver']} — Bahrain 2023 R")
ax.grid(True)
plt.tight_layout()
plt.savefig('speed_trace.png', dpi=150)
plt.show()