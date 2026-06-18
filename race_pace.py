import fastf1
import fastf1.plotting
import matplotlib.pyplot as plt
import seaborn as sns

fastf1.Cache.enable_cache('./cache')
fastf1.plotting.setup_mpl(misc_mpl_mods=False, color_scheme='fastf1')

session = fastf1.get_session(2023, 'Bahrain', 'R')
session.load()

# Pick only "representative" laps — drops in/out laps, safety car laps, etc.
laps = session.laps.pick_quicklaps().reset_index()
laps['LapTime(s)'] = laps['LapTime'].dt.total_seconds()

# Order drivers fastest-to-slowest by median lap time
driver_order = (
    laps[['Driver', 'LapTime(s)']]
    .groupby('Driver')
    .median(numeric_only=True)['LapTime(s)']
    .sort_values()
    .index
    .tolist()
)

# Build a color palette using each driver's team color
team_palette = {
    drv: fastf1.plotting.get_driver_color(drv, session=session)
    for drv in driver_order
}

fig, ax = plt.subplots(figsize=(13, 6))
sns.boxplot(
    data=laps,
    x='Driver',
    y='LapTime(s)',
    order=driver_order,
    palette=team_palette,
    whiskerprops=dict(color='white'),
    boxprops=dict(edgecolor='white'),
    medianprops=dict(color='grey'),
    capprops=dict(color='white'),
)

ax.set_title('Race Pace Comparison — Bahrain 2023')
ax.set_xlabel('Driver')
ax.set_ylabel('Lap Time (seconds)')
plt.suptitle('')  # remove default seaborn suptitle
plt.tight_layout()
plt.savefig('race_pace.png', dpi=150)
plt.show()