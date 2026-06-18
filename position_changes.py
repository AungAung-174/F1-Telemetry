import fastf1
import fastf1.plotting
import matplotlib.pyplot as plt

fastf1.Cache.enable_cache('./cache')
fastf1.plotting.setup_mpl(misc_mpl_mods=False, color_scheme='fastf1')

session = fastf1.get_session(2023, 'Bahrain', 'R')
session.load()

fig, ax = plt.subplots(figsize=(12, 7))

for drv in session.drivers:
    drv_laps = session.laps.pick_drivers(drv)
    if drv_laps.empty:
        continue
    abb = drv_laps['Driver'].iloc[0]
    style = fastf1.plotting.get_driver_style(
        abb, ['color', 'linestyle'], session=session
    )
    ax.plot(drv_laps['LapNumber'], drv_laps['Position'], label=abb, **style)

ax.set_ylim([20.5, 0.5])  # inverted because P1 should be on top
ax.set_yticks([1, 5, 10, 15, 20])
ax.set_xlabel('Lap')
ax.set_ylabel('Position')
ax.set_title('Position Changes — Bahrain 2023 Race')
ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout()
plt.savefig('position_changes.png', dpi=150)
plt.show()