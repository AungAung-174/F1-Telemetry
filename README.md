# F1-Telemetry
Data analysis and visualization of Formula 1 telemetry using the FastF1 Python library

## ⚠️ Known issue
The F1 live timing API blocks VPN traffic. If `session.load()` fails with 
"Failed to load" warnings on every endpoint, disconnect your VPN and try again.