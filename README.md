# Project: GovSpend-KE 🇰🇪

A **Techblurbs** initiative to liberate Kenyan government financial data from "dirty" PDFs and turn it into actionable, machine-readable insights.

---

## 📌 Overview

Public financial data in Kenya is often published in complex, inconsistently formatted PDF reports across various government portals. **GovSpend-KE** is a civic tech project designed to automate the collection, extraction, and visualization of this data, providing a clear view of how national and county budgets are actually implemented.

---

## 🛠 The Pipeline

The project is structured into four main phases:

1.  **Ingestion:** Automated scrapers that monitor and download reports from the National Treasury and the Office of the Controller of Budget (OCOB).
2.  **Extraction & Cleaning:** Using OCR and table-parsing libraries to pull data from "stubborn" PDFs and standardizing it into a unified format.
3.  **Storage & Versioning:** A relational database to store historical records, allowing us to track changes and revisions over time.
4.  **Presentation:** A web dashboard for visualizations and an API/Export tool for CSV access.

---

## 🔍 Data Auditing & Verification

Accuracy is the backbone of this project. Because PDF extraction can be "noisy" and government reports can contain internal errors, the following protocols are mandatory:

* **Multi-Source Reconciliation:** Data must be cross-referenced between Treasury "Exchequer Releases" and OCOB "Implementation Reports" to identify discrepancies.
* **Vertical/Horizontal Totals:** Automated scripts will verify that the sum of sub-categories matches the "Total" figures printed in the source documents.
* **Human-in-the-Loop:** High-variance figures or "broken" tables will be flagged for manual audit by the data team before being committed to the production database.
* **Source Linking:** Every data point in the DB will maintain a link back to the original source PDF and the specific page number for transparency.

---

## 👥 Team Roles

| Team | Responsibilities |
| :--- | :--- |
| **Data Engineering** | PDF scrapers, ETL pipelines, and DB schema management. |
| **Data Audit** | Verification logic, reconciliation, and domain mapping. |
| **Front End** | Visualization (D3.js/Chart.js), UI/UX, and CSV export tools. |
| **DevOps** | Automation of data harvests and hosting infrastructure. |

---

## 🚀 Getting Started

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd gov-spend-KE
    ```

2.  **Set up the virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure environment variables:**
    Copy `.env.example` to `.env` and update the database credentials.
    ```bash
    cp .env.example .env
    ```

5.  **Run the initial harvester:**
    ```bash
    python3 run_harvester.py
    ```

### 🐳 Running with Docker (Recommended)

If you have Docker installed, you can skip the manual setup:

1.  **Configure environment variables:**
    ```bash
    cp .env.example .env
    ```

2.  **Start the services:**
    ```bash
    docker compose up -d
    ```

This will automatically spin up a PostgreSQL database and the harvester application with all system dependencies (OCR, etc.) pre-installed.

---

## 📂 Project Structure

```text
.
├── data/               # Data storage
│   ├── raw/            # Original PDF reports (ignored by git)
│   └── processed/      # Extracted CSV/JSON data
├── src/                # Source code
│   ├── ingestion/      # Scrapers and downloaders
│   ├── extraction/     # PDF parsing and OCR logic
│   ├── storage/        # DB schema and models
│   ├── audit/          # Verification and reconciliation
│   ├── presentation/   # API and Dashboard code
│   └── utils/          # Shared utilities
├── tests/              # Unit and integration tests
├── .env.example        # Environment template
├── .gitignore          # Git exclusion rules
├── Dockerfile          # Docker image configuration
├── docker-compose.yml  # Multi-container orchestration
├── requirements.txt    # Project dependencies
└── run_harvester.py    # Main pipeline entry point
```

---

**Disclaimer:** *GovSpend-KE is an independent project by Techblurbs and is not an official government platform. We aim for 100% accuracy through rigorous auditing.*
