# Titanic Survival API Prototype

This repository contains a simple prototype API built using **FastAPI** to demonstrate basic prediction logic based on the Titanic dataset.

It showcases two distinct methods for creating API endpoints:
1.  **`app.py`**: A simple `GET` endpoint that takes query parameters.
2.  **`app_s.py`**: A more robust `PUT` endpoint that uses **Pydantic** for request body validation.

---

## 🚀 Getting Started

### Prerequisites

* Python 3.7+
* An understanding of basic Python and APIs.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **(Recommended) Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required libraries:**
    ```bash
    pip install fastapi pydantic uvicorn
    ```

---

## 🏃 Running the API

You can run either of the two prototype servers. They must be run one at a time as they both use the same port.

### 1. Simple GET Endpoint Server
This server uses a simple `GET` request with query parameters.

```bash
uvicorn app:app --reload
