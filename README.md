# Ω Midgard Monitor

A lightweight macOS **menu bar app** built with Python and `rumps` that visually indicates CPU load using a God-of-War–inspired Omega symbol.

## Features
- 🔵 **Blue Omega** → Normal CPU usage (≤ 50%)
- 🔴 **Red Omega** → High CPU usage (> 50%)
- 🔔 macOS notification when CPU crosses 50%
- 🪶 Extremely lightweight (runs in background)

## Tech Stack
- Python 3
- rumps (macOS menu bar apps)
- psutil (CPU monitoring)

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install rumps psutil
