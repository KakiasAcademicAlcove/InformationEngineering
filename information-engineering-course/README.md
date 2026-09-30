# Information Systems Engineering (Level 6) - 2026/27

Welcome to the central repository for Information Systems Engineering.

## Navigation & Structure
- `docs/`: Module specification, assignment briefs, and setup guides.
- `lab-environment/`: Shared Docker Compose stack for local hands-on labs.
- `units/`: Sequenced curriculum units (Units 01 to 21).

# Information Systems Engineering (Level 6) — Academic Year 2026/27

Welcome to the primary GitHub repository for **Information Systems Engineering**. This repository serves as a centralized, open-source repository containing lecture guides, architectural specifications, hands-on lab environments, presentation slide decks, and project code across 21 core curriculum units.

---

## 🗺️ Master Curriculum Blueprint & Unit Navigation

| Unit | Title | Module Category | Lecture Guide | Lab Stack & Ecosystem |
| :--- | :--- | :--- | :---: | :--- |
| **Unit 01** | Foundations of Information Engineering & Systems Theory | Module 1: Foundations & Modeling | [Guide](units/unit-01/README.md) | Python, Draw.io, Mermaid.js |
| **Unit 02** | Systems Analysis, Data Modeling & ADRs | Module 1: Foundations & Modeling | [Guide](units/unit-02/README.md) | Structurizr, dbdiagram.io, Git |
| **Unit 03** | Pipeline Design Patterns: ETL vs. ELT & Backfilling | Module 1: Foundations & Modeling | [Guide](units/unit-03/README.md) | Apache Airflow, Docker, Python |
| **Unit 04** | Relational Databases (SQL), Query Tuning & Caching | Module 2: Storage & Ingestion | [Guide](units/unit-04/README.md) | PostgreSQL, Redis, pgAdmin |
| **Unit 05** | Ingestion Engineering, APIs & Web Scraping | Module 2: Storage & Ingestion | [Guide](units/unit-05/README.md) | Python (Scrapy), Debezium, APIs |
| **Unit 06** | NoSQL Systems, Semi-Structured Data & Document DBs | Module 2: Storage & Ingestion | [Guide](units/unit-06/README.md) | MongoDB, Cassandra, Neo4j |
| **Unit 07** | Data Warehousing, OLAP & Dimensional Modeling | Module 2: Storage & Ingestion | [Guide](units/unit-07/README.md) | DuckDB, dbt Core, Snowflake |
| **Unit 08** | Lakehouses & Open Table Formats | Module 3: Modern Data Stack | [Guide](units/unit-08/README.md) | Apache Iceberg, Delta Lake, MinIO |
| **Unit 09** | Event-Driven Architectures & Real-Time Streaming | Module 3: Modern Data Stack | [Guide](units/unit-09/README.md) | Apache Kafka, Apache Flink |
| **Unit 10** | Data Wrangling, Cleaning & Data Quality Frameworks | Module 3: Modern Data Stack | [Guide](units/unit-10/README.md) | Polars, Great Expectations, Pydantic |
| **Unit 11** | Data Reliability Engineering (DRE) & Incident Management | Module 3: Modern Data Stack | [Guide](units/unit-11/README.md) | Prometheus, Grafana, OpenTelemetry |
| **Unit 12** | Orchestration (dbt), Container Workflows & Data Mesh | Module 4: Distributed Computing & AI | [Guide](units/unit-12/README.md) | Docker Compose, dbt, Terraform |
| **Unit 13** | Distributed Big Data Frameworks & Cloud Networking | Module 4: Distributed Computing & AI | [Guide](units/unit-13/README.md) | Apache Spark, PySpark, Jupyter |
| **Unit 14** | ML Pipelines, Feature Engineering & MLOps Integration | Module 4: Distributed Computing & AI | [Guide](units/unit-14/README.md) | Feast, MLflow, Scikit-Learn |
| **Unit 15** | Information Retrieval, Vector Search & AI Pipelines | Module 4: Distributed Computing & AI | [Guide](units/unit-15/README.md) | Chroma, Qdrant, LangChain |
| **Unit 16** | Agentic AI in Data Engineering ("Vibe Coding") | Module 4: Distributed Computing & AI | [Guide](units/unit-16/README.md) | Claude Code, Ollama, SQLGlot |
| **Unit 17** | Sustainability, Green Computing & Cloud Economics (FinOps) | Module 5: Governance & Specialised | [Guide](units/unit-17/README.md) | Kepler, Infracost, Cost Explorer |
| **Unit 18** | Global Data Protection, AI Legislation & Regulation | Module 5: Governance & Specialised | [Guide](units/unit-18/README.md) | Presidio, OpenPAI, Immuta |
| **Unit 19** | Enterprise Governance, Security Isolation & Lineage | Module 5: Governance & Specialised | [Guide](units/unit-19/README.md) | OpenLineage, dbt-docs, Apache Atlas |
| **Unit 20** | Specialised & Domain-Specific Information Systems | Module 5: Governance & Specialised | [Guide](units/unit-20/README.md) | PostGIS, QGIS, Apache FHIR |
| **Unit 21** | Data Engineering Careers, Roles & Certifications | Module 6: Careers & Practice | [Guide](units/unit-21/README.md) | GitHub Actions, VS Code, CI/CD |

---

## 💻 Quickstart: Working in GitHub Codespaces

1. **Launch Environment:** Click the **Code** button at the top of this repository and select **Open with Codespaces**.
2. **Start Local Infrastructure Stack:** Open the embedded terminal in Codespaces and run:
   ```bash
   cd lab-environment
   docker compose up -d