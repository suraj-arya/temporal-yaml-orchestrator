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

