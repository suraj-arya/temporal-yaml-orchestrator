# 🧩 YAML-Driven API Orchestrator with Temporal (Python)

This project demonstrates how to build a dynamic API workflow engine using [Temporal](https://temporal.io) and Python — where workflows are defined in YAML and interpreted at runtime.

---

## 📦 Features

- Define API workflows in simple YAML format
- Pass context between steps
- Extract and parse response data with JSONPath
- Easily extend to support templating, error handling, retries, etc.

---

## ⚙️ Prerequisites

- Python 3.10+ recommended (Python 3.13 also supported)
- [Temporal CLI](https://docs.temporal.io/install-temporal-cli) installed

```bash
brew install temporal
# or
curl -sSf https://temporal.download/cli.sh | sh
```

## 🚀 Getting Started

### 1. Start Temporal Server

First, start the Temporal server using the Temporal CLI:

```bash
temporal server start-dev
```

This will start a local Temporal server with default settings. The server will be available at `localhost:7233`.

### 2. Start the Worker

In a new terminal window, start the worker that will execute the workflows:

```bash
python -m orchestrator.worker
```

The worker will connect to the Temporal server and start listening for workflow tasks.

### 3. Run the Client

In another terminal window, you can run the client to start workflows:

```bash
python -m orchestrator.client
```

The client will connect to the Temporal server and start the workflow defined in your YAML configuration.

---

## 📝 Configuration

// ... existing code ...
