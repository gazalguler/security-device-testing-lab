
# Security Device Testing Lab

A simulated security camera system for practicing API testing, browser automation, and continuous integration.

## Technologies

- Python, FastAPI, pytest
- TypeScript and HTML
- Playwright with Chromium
- GitHub Actions

## Features

- Simulated camera status API
- Camera event validation
- Web dashboard displaying camera status
- Error handling when the API is unavailable
- Automated API and browser tests

## Automated Tests

### API Testing
Six pytest tests covering camera status, valid and invalid events, and unknown endpoints.

### Browser Testing
Two Playwright tests verifying:
- The dashboard loads camera status from the API
- The dashboard displays an error when the API is unavailable

### Continuous Integration
GitHub Actions runs three independent jobs:
- Python API tests
- TypeScript type checking and build
- Playwright browser tests

All three jobs passed in the initial CI run.

## Running Locally

Install dependencies:

    python3 -m venv .venv
    .venv/bin/python -m pip install -r camera-api/requirements.txt
    npm ci
    npm run build
    npx playwright install chromium

Start the API from the project root:

    cd camera-api
    ../.venv/bin/python -m uvicorn app.main:app --port 8000

In a second terminal, from the project root:

    python3 -m http.server 5500 --directory web

Open http://127.0.0.1:5500

## Running Tests

API tests (from project root):

    cd camera-api
    ../.venv/bin/python -m pytest -v

Browser tests (from project root, with both servers running):

    npx playwright test e2e/camera.spec.ts --browser=chromium

## Scope

This project uses simulated camera data and does not connect to physical security cameras or production surveillance systems.