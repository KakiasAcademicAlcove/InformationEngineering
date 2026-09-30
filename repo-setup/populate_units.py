import os

units_data = [
    {
        "num": "01",
        "title": "Foundations of Information Engineering & Systems Theory",
        "module": "Module 1: Foundations, Architectures & Modeling",
        "topics": [
            "DIKW Hierarchy: Data, Information, Knowledge, Wisdom structure and engineering transformation stages.",
            "Socio-Technical Systems: Interactions between technical infrastructure, human workflows, and business processes[cite: 1].",
            "Data Characteristics: The 5 Vs (Volume, Velocity, Variety, Veracity, Value) and operational trade-offs[cite: 1].",
            "Evolution of Systems: Historical trajectory from traditional IT information systems to modern data engineering[cite: 1]."
        ],
        "stack": "Draw.io, Mermaid.js, Python, AWS Console, Azure Portal, Lucidchart[cite: 1]"
    },
    {
        "num": "02",
        "title": "Systems Analysis, Data Modeling & Architecture Decision Records (ADRs)",
        "module": "Module 1: Foundations, Architectures & Modeling",
        "topics": [
            "Software Lifecycle: Systems Development Lifecycle (SDLC) tailored for data systems and continuous iteration[cite: 1].",
            "Structural Diagrams: Entity-Relationship Diagrams (ERDs) and Data Flow Diagrams (DFDs) for systemic modeling[cite: 1].",
            "Modeling Tiers: Conceptual, logical, and physical data modeling across varied engines[cite: 1].",
            "Architecture Governance: Drafting and maintaining Architecture Decision Records (ADRs) to document technical choices[cite: 1]."
        ],
        "stack": "Structurizr, dbdiagram.io, Git, AWS CloudFormation, Azure ARM, Bizzdesign, ArchiMate[cite: 1]"
    },
    {
        "num": "03",
        "title": "Pipeline Design Patterns: ETL vs. ELT, Backfilling & Determinism",
        "module": "Module 1: Foundations, Architectures & Modeling",
        "topics": [
            "Paradigm Evolution: Historic transitions from ETL (Extract, Transform, Load) to cloud ELT architectures[cite: 1].",
            "Architectural Styles: Batch, Micro-batch, Lambda (speed + batch layers), and Kappa (stream-first) frameworks[cite: 1].",
            "Pipeline Design: End-to-end data flow topology, fault tolerance, and idempotent execution[cite: 1].",
            "Historical Replays & Backfilling: Managing data backfills, deterministic state resets, partition strategies, and historical re-runs without data duplication or table locking[cite: 1]."
        ],
        "stack": "Apache Airflow, Python, Docker, AWS Step Functions, AWS Lambda, Azure Data Factory, Prefect, Dagster[cite: 1]"
    },
    {
        "num": "04",
        "title": "Relational Databases (SQL), Query Optimization & Caching",
        "module": "Module 2: Storage, Ingestion & Data Warehousing",
        "topics": [
            "Relational Theory: Relational algebra, advanced SQL queries, and normalization levels (1NF–3NF/BCNF)[cite: 1].",
            "Transaction Guarantees: ACID properties, isolation levels, and concurrency control[cite: 1].",
            "Performance Tuning: Query execution plan analysis, index optimization (B-Trees, Hash indexes), and partitioning[cite: 1].",
            "Caching Mechanics: In-memory caching architecture design using layers like Redis for high-frequency reads[cite: 1]."
        ],
        "stack": "PostgreSQL, MySQL, Redis, pgAdmin, Amazon RDS, Amazon Aurora, ElastiCache, Azure SQL, Supabase, CockroachDB[cite: 1]"
    },
    {
        "num": "05",
        "title": "Ingestion Engineering, APIs & Web Scraping",
        "module": "Module 2: Storage, Ingestion & Data Warehousing",
        "topics": [
            "API Integration: Consuming RESTful APIs, GraphQL endpoints, and webhook architectures[cite: 1].",
            "Resilience Patterns: Managing API rate limits, pagination strategies, exponential backoff, and retry logic[cite: 1].",
            "Web Scraping at Scale: Distributed web crawling, headless browsers, dynamic DOM rendering, and rate compliance[cite: 1].",
            "Change Data Capture: Real-time relational database synchronization using log-based Change Data Capture (CDC)[cite: 1]."
        ],
        "stack": "Python (Requests, BeautifulSoup, Scrapy), Debezium, AWS Glue, AWS DMS, Amazon Kinesis, Azure Data Factory, Airbyte, Fivetran, Meltano[cite: 1]"
    },
    {
        "num": "06",
        "title": "NoSQL Systems, Semi-Structured Data & Document Databases",
        "module": "Module 2: Storage, Ingestion & Data Warehousing",
        "topics": [
            "Distributed Consistency: CAP Theorem, PACELC Theorem, and BASE consistency models[cite: 1].",
            "NoSQL Typologies: Document stores (MongoDB), Key-Value databases, Wide-Column stores (Cassandra), and Graph databases (Neo4j)[cite: 1].",
            "Data Formats: Parsing and processing JSON, Parquet, Avro, and Protobuf schema structures[cite: 1]."
        ],
        "stack": "MongoDB, Apache Cassandra, Neo4j, Amazon DynamoDB, DocumentDB, Azure Cosmos DB, MongoDB Atlas, Neo4j Aura[cite: 1]"
    },
    {
        "num": "07",
        "title": "Data Warehousing, OLAP & Dimensional Modeling",
        "module": "Module 2: Storage, Ingestion & Data Warehousing",
        "topics": [
            "OLTP vs. OLAP: Architectural differences between transactional databases and analytical engines[cite: 1].",
            "Kimball Methodology: Dimensional modeling, Fact tables, Dimension tables, and Star vs. Snowflake schemas[cite: 1].",
            "Dimension Management: Implementing Slowly Changing Dimensions (SCD Types 1, 2, and 3)[cite: 1].",
            "Modern Warehouses: MPP (Massively Parallel Processing) execution in modern cloud warehouses[cite: 1]."
        ],
        "stack": "DuckDB, PostgreSQL, dbt Core, Amazon Redshift, Azure Synapse Analytics, Snowflake, Databricks SQL[cite: 1]"
    },
    {
        "num": "08",
        "title": "Lakehouses & Open Table Formats",
        "module": "Module 3: Modern Data Stack & Streaming Architectures",
        "topics": [
            "Data Lake Evolution: Moving beyond raw file storage in object stores to structured analytics layers[cite: 1].",
            "Lakehouse Architecture: Blending data lake scalability with database reliability[cite: 1].",
            "Open Table Formats: Deep dive into Apache Iceberg, Delta Lake, and Apache Hudi[cite: 1].",
            "Storage Features: Time travel queries, schema enforcement, schema evolution, and ACID transactions over object storage[cite: 1]."
        ],
        "stack": "Apache Iceberg, Delta Lake, Apache Hudi, MinIO, AWS Lake Formation, Amazon S3, Athena, Azure ADLS Gen2, Databricks Unity Catalog[cite: 1]"
    },
    {
        "num": "09",
        "title": "Event-Driven Architectures & Real-Time Streaming",
        "module": "Module 3: Modern Data Stack & Streaming Architectures",
        "topics": [
            "Messaging Models: Publish-Subscribe (Pub/Sub) vs. Request-Response and point-to-point architectures[cite: 1].",
            "Message Brokers: Distributed event streaming with Apache Kafka, RabbitMQ, and AWS Kinesis[cite: 1].",
            "Stream Processing: Processing fundamentals including event time vs. processing time, late data arrival, and windowing (tumbling, sliding, session) using Apache Flink or Spark Streaming[cite: 1]."
        ],
        "stack": "Apache Kafka, Apache Flink, RabbitMQ, Amazon MSK, Kinesis Data Streams, Azure Event Hubs, Stream Analytics, Confluent Cloud, Redpanda[cite: 1]"
    },
    {
        "num": "10",
        "title": "Data Wrangling, Cleaning & Data Quality Frameworks",
        "module": "Module 3: Modern Data Stack & Streaming Architectures",
        "topics": [
            "Exploratory Data Analysis: Data wrangling in Python (Pandas, Polars) and R for structural inspection[cite: 1].",
            "Automated Quality Control: Implementing assertions using frameworks like Great Expectations and Pydantic[cite: 1].",
            "Data Contracts: Defining schema standards, enforcement mechanisms, and contract lifecycle management[cite: 1].",
            "Schema Evolution: Mitigating upstream schema drift and handling missing or corrupt data safely[cite: 1]."
        ],
        "stack": "Pandas, Polars, Great Expectations, Pydantic, AWS Glue DataBrew, Azure Data Factory Data Flows, Monte Carlo, Soda Core[cite: 1]"
    },
    {
        "num": "11",
        "title": "Data Reliability Engineering (DRE), SLOs & Incident Response",
        "module": "Module 3: Modern Data Stack & Streaming Architectures",
        "topics": [
            "Service Management: Defining Service Level Agreements (SLAs), Service Level Objectives (SLOs), and Service Level Indicators (SLIs) for data[cite: 1].",
            "Data Metrics: Measuring freshness, completeness, volume anomalies, and distribution shifts[cite: 1].",
            "Resilience Patterns: Implementing circuit breakers, fallback routines, backfill execution scripts, and zero-downtime deployment strategies[cite: 1].",
            "Incident Operations: On-call readiness, structured incident management, blameless post-mortems, and root-cause analysis[cite: 1]."
        ],
        "stack": "Prometheus, Grafana, OpenTelemetry, Amazon CloudWatch, AWS X-Ray, Azure Monitor, Datadog, Anomalo[cite: 1]"
    },
    {
        "num": "12",
        "title": "Orchestration (dbt), Local Container Workflows & Data Mesh",
        "module": "Module 4: Orchestration, Distributed Computing & AI Pipelines",
        "topics": [
            "Analytics Engineering: In-warehouse data transformation and modular modeling using dbt[cite: 1].",
            "Workflow Orchestration: Managing Directed Acyclic Graphs (DAGs) using Apache Airflow or Dagster[cite: 1].",
            "Local Development & Containerization: Developing locally with Docker, Docker Compose, and local emulators (MinIO for S3 emulation, LocalStack, Postgres/Kafka containers) before pushing to CI/CD[cite: 1].",
            "Decentralized Data: Infrastructure as Code (Terraform), Data Mesh principles, domain-oriented ownership, and enterprise semantic layers (dbt Semantic Layer, Cube)[cite: 1]."
        ],
        "stack": "Docker, Docker Compose, dbt Core, Terraform, AWS MWAA, AWS ECS/EKS, Azure Container Instances, Astronomer, Cube.dev[cite: 1]"
    },
    {
        "num": "13",
        "title": "Distributed Big Data Frameworks, Profiling & Cloud Networking",
        "module": "Module 4: Orchestration, Distributed Computing & AI Pipelines",
        "topics": [
            "Distributed Mechanics: Fundamentals of HDFS, MapReduce, and Apache Spark execution engines[cite: 1].",
            "Performance Profiling & Data Skew: Analyzing Spark execution graphs, identifying data skew ('stuck at 99%'), repartitioning, key salting, and synthetic stress testing[cite: 1].",
            "Cloud Networking & Security: Virtual Private Clouds (VPCs), PrivateLink, IAM permission boundaries, KMS key management, and secure cross-network data movement[cite: 1].",
            "Cloud Platforms: Cloud-native pipeline orchestration across AWS (S3, Athena, EMR), GCP (BigQuery), and Databricks[cite: 1]."
        ],
        "stack": "Apache Spark, PySpark, Jupyter, Amazon EMR, Athena, AWS VPC, Azure HDInsight, Databricks Workspaces[cite: 1]"
    },
    {
        "num": "14",
        "title": "Machine Learning Pipelines, Feature Engineering & MLOps Integration",
        "module": "Module 4: Orchestration, Distributed Computing & AI Pipelines",
        "topics": [
            "ML Pipeline Dynamics: Building data pipelines specifically for AI/ML—offline batch training vs. online real-time inference pipelines[cite: 1].",
            "Federated Machine Learning & Pipeline Impacts: Federated learning architectures, decentralized edge data processing, privacy-preserving aggregation protocols (Secure Aggregation, Differential Privacy), client orchestration, and managing asynchronous model parameter synchronization[cite: 1].",
            "Feature Stores & Training-Serving Skew: Feature engineering, managing Feature Stores (Feast), and preventing training-serving data skew[cite: 1].",
            "Drift & Feedback Loops: Detecting feature drift vs. concept drift, handling continuous data feedback loops for AI models, and model re-training triggers[cite: 1].",
            "Data Mining & Forecasting: Pattern discovery, association rule mining, and time-series forecasting[cite: 1]."
        ],
        "stack": "Feast, MLflow, Scikit-learn, Amazon SageMaker, SageMaker Feature Store, Azure Machine Learning, Hopsworks, Weights & Biases[cite: 1]"
    },
    {
        "num": "15",
        "title": "Information Retrieval, Vector Search & AI-Ready Pipelines",
        "module": "Module 4: Orchestration, Distributed Computing & AI Pipelines",
        "topics": [
            "Information Retrieval: IR fundamentals, search engine structures, tokenization, and Named Entity Recognition (NER)[cite: 1].",
            "Text Processing: Document chunking strategies, semantic overlap, and vector text embedding generation[cite: 1].",
            "Vector Databases: Vector index management, similarity metrics, and querying in Pinecone, Qdrant, and Chroma[cite: 1].",
            "RAG Infrastructure: Building data pipelines to power Retrieval-Augmented Generation systems[cite: 1]."
        ],
        "stack": "Chroma, Qdrant, Elasticsearch, LangChain, Amazon OpenSearch, Amazon Bedrock Knowledge Bases, Azure AI Search, Pinecone, Weaviate[cite: 1]"
    },
    {
        "num": "16",
        "title": "Agentic AI in Data Engineering ('Vibe Coding' & Automation)",
        "module": "Module 4: Orchestration, Distributed Computing & AI Pipelines",
        "topics": [
            "AI Coding Agents: Leveraging developer tools (Claude Code, GitHub Copilot, Databricks Genie) to generate ETL processes[cite: 1].",
            "Code Auditing: Static analysis, unit testing, and manual review of AI-generated SQL and Python code[cite: 1].",
            "Legacy Refactoring: Automated conversion and modernization of legacy SQL scripts and batch scripts[cite: 1]."
        ],
        "stack": "Claude Code, Ollama, SQLGlot, GitHub Copilot, Amazon Q Developer, Amazon Bedrock Studio, Azure OpenAI Assistants, Cursor, Databricks Genie[cite: 1]"
    },
    {
        "num": "17",
        "title": "Sustainability, Green Computing & Cloud Economics (FinOps)",
        "module": "Module 5: Sustainability, Enterprise Governance & Specialised Systems",
        "topics": [
            "FinOps & Cloud Economics: Cloud warehouse consumption patterns, query cost optimization, partitioning strategies, predicate pushdown, and eliminating orphan compute jobs[cite: 1].",
            "Green Computing: Measuring carbon emissions of compute pipelines, sustainable software engineering, and resource optimization trade-offs[cite: 1]."
        ],
        "stack": "Kepler (Kubernetes Efficient Power), Infracost, AWS Cost Explorer, CloudWatch Energy Metrics, Azure Cost Management, CloudZero, Vantage[cite: 1]"
    },
    {
        "num": "18",
        "title": "Global Data Protection, AI Legislation & Regulatory Frameworks",
        "module": "Module 5: Sustainability, Enterprise Governance & Specialised Systems",
        "topics": [
            "Privacy Legislation: Compliance with UK GDPR, Data Protection Act 2018, EU GDPR, and US privacy laws (CCPA/CPRA)[cite: 1].",
            "AI Legislation: Navigating the EU AI Act risk tiers, high-risk data pipeline obligations, and US Executive Orders on AI[cite: 1].",
            "Compliance Frameworks: Executing Data Protection Impact Assessments (DPIAs), implementing 'Right to be Forgotten' requests in object stores, and cross-border data transfer controls[cite: 1]."
        ],
        "stack": "OpenPAI, Presidio, Immuta (Community), AWS Lake Formation, AWS Macie, Azure Purview, Microsoft Priva, OneTrust, Collibra[cite: 1]"
    },
    {
        "num": "19",
        "title": "Enterprise Governance, Security Isolation & Data Product Management",
        "module": "Module 5: Sustainability, Enterprise Governance & Specialised Systems",
        "topics": [
            "Network & Access Security: Cloud infrastructure isolation, zero-trust network boundaries, dynamic data masking, Row-Level Security (RLS), Column-Level Security (CLS), and Role-Based Access Control (RBAC)[cite: 1].",
            "PII & Lineage: Automated detection of personally identifiable information and lineage tracking (OpenLineage, dbt docs)[cite: 1].",
            "Data Products: Treating data assets as products, maintaining metadata catalogs (Atlan, Collibra), and setting documentation standards[cite: 1]."
        ],
        "stack": "OpenLineage, Apache Atlas, dbt-docs, AWS Glue Data Catalog, IAM, Azure Purview, Atlan, Alation[cite: 1]"
    },
    {
        "num": "20",
        "title": "Specialised & Domain-Specific Information Management Systems",
        "module": "Module 5: Sustainability, Enterprise Governance & Specialised Systems",
        "topics": [
            "Emergency Systems: High-availability architecture design for disaster response, emergency alerting, and adverse operational conditions[cite: 1].",
            "Geographic Information Systems (GIS): Spatial data engineering, processing vector and raster spatial formats, and spatial indexing (PostGIS)[cite: 1].",
            "Health Systems: Processing medical protocols (HL7, FHIR), HIPAA compliance constraints, and genomic pipeline execution[cite: 1].",
            "Enterprise Systems: Data structures for Learning Management Systems (LMS), Transaction Processing Systems (TPS), Decision Support Systems (DSS), and Executive Information Systems (EIS)[cite: 1]."
        ],
        "stack": "PostGIS, QGIS, Apache FHIR, OpenClinica, Amazon Location Service, AWS HealthLake, Azure Maps, Azure Health Data Services, ArcGIS, Palantir Foundry[cite: 1]"
    },
    {
        "num": "21",
        "title": "Data Engineering Careers, Industry Roles & Certifications",
        "module": "Module 6: Careers & Professional Practice",
        "topics": [
            "Industry Roles: Functional distinctions across Data Engineer, Analytics Engineer, Platform Engineer, MLOps Engineer, Data Architect, and Database Administrator roles[cite: 1].",
            "Professional Certifications: Cloud platforms (AWS DEA-C01, GCP PDE, Azure DP-203), Ecosystem platforms (Databricks, Snowflake), and specialized tooling (dbt)[cite: 1].",
            "Portfolio Development: Building and documenting production-grade GitHub projects featuring open-source pipelines with dbt, Airflow, Docker, and CI/CD pipelines[cite: 1].",
            "Team Dynamics: Balancing sprint commits against ad-hoc data requests, and collaborating across Product, Engineering, and Science teams[cite: 1]."
        ],
        "stack": "GitHub, Git, VS Code, CI/CD Actions, AWS Skill Builder, Microsoft Learn Labs, Databricks Academy, Snowflake University[cite: 1]"
    }
]

BASE_DIR = "../information-engineering-course/units"

for unit in units_data:
    folder_path = os.path.join(BASE_DIR, f"unit-{unit['num']}")
    os.makedirs(f"{folder_path}/slides", exist_ok=True)
    print("slides folder path ok for this unit")
    os.makedirs(f"{folder_path}/code", exist_ok=True)
    os.makedirs(f"{folder_path}/exercises", exist_ok=True)
    
    topics_list = "\n".join([f"- {t}" for t in unit["topics"]])
    
    content = f"""# Unit {unit['num']}: {unit['title']}

**Module Category:** {unit['module']}

---

## 📖 Key Topics & Curriculum Focus

{topics_list}

---

## 🛠️ Recommended Lab Tools & Stack

- **Target Technologies:** {unit['stack']}

---

## 📁 Unit Directory Structure

- `slides/`: Presentation slide decks (PDF / Marp Markdown format).
- `code/`: Executable code examples, notebooks, and scripts.
- `exercises/`: Hands-on lab instructions, starter templates, and sample solutions.
"""
    
    with open(f"{folder_path}/README.md", "w") as f:
        f.write(content)

print("Successfully populated all 21 Unit README files!")