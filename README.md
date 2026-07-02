# 🚖 Uber End-To-End Data Engineering Project (2026)

![Azure](https://img.shields.io/badge/Azure-Cloud-blue)
![Databricks](https://img.shields.io/badge/Databricks-BigData-red)
![PySpark](https://img.shields.io/badge/PySpark-Streaming-orange)
![SQL](https://img.shields.io/badge/SQL-Database-green)

## Azure Databricks Streaming Project

A real-time end-to-end Data Engineering project that simulates an Uber-like ride booking platform using **Azure Cloud Services, Azure Data Factory, Event Hub, ADLS Gen2, and Databricks**.

This project demonstrates how streaming and batch data can be ingested, processed, transformed, and modeled into analytics-ready data using modern Data Engineering best practices.

---

## 📌 Project Overview

This project simulates an Uber ride-booking ecosystem where ride booking events are generated from a custom-built Python web application.

The system handles both:

- **Real-Time Streaming Data** → Ride booking events from Web Application  
- **Batch Data** → Historical bulk datasets from GitHub  

Both data sources are ingested into Azure and processed using a scalable data pipeline.

---

## ✨ Key Features

- ✅ Real-time data ingestion using Azure Event Hub  
- ✅ Batch data ingestion from GitHub using Azure Data Factory  
- ✅ Data storage in Azure Data Lake Storage Gen2  
- ✅ End-to-end ETL pipeline using Azure Databricks  
- ✅ Streaming + Batch data processing  
- ✅ Medallion Architecture (Bronze → Silver → Gold)  
- ✅ Star Schema Data Modeling  
- ✅ Fact & Dimension Table creation  
- ✅ Jinja-based reusable SQL templates  

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │  Python Web App     │
                    │  (Ride Booking UI)  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Azure Event Hub     │
                    │ (Streaming Data)    │
                    └──────────┬──────────┘
                               │
                               │
┌───────────────────┐          ▼
│ GitHub Datasets   │ ──► ┌───────────────┐
│ (Batch Data)      │     │ Azure Data    │
└───────────────────┘     │ Factory (ADF) │
                          └───────┬───────┘
                                  │
                                  ▼
                    ┌─────────────────────────┐
                    │ ADLS Gen2 (Raw Layer)   │
                    │ Bronze Storage          │
                    └──────────┬──────────────┘
                               │
                               ▼
                    ┌─────────────────────────┐
                    │ Azure Databricks        │
                    │ PySpark + Delta Lake    │
                    └──────────┬──────────────┘
                               │
               ┌───────────────┴───────────────┐
               ▼                               ▼
        ┌─────────────┐                 ┌─────────────┐
        │ Silver Layer│                 │ Gold Layer  │
        │ Cleaned Data│                 │ Star Schema │
        └─────────────┘                 └─────────────┘
```

---

## 🏗️ Architecture Diagram

<img width="1536" height="1024" alt="Architecture" src="https://github.com/user-attachments/assets/ea117452-e9a7-42e2-82f8-4a11e8a7319c" />

---

## 🔄 Data Flow

### Step 1: Ride Booking
Users book rides using a custom-built Python web application.

### Step 2: Streaming Ingestion
Booking events are pushed to **Azure Event Hub** in real time.

### Step 3: Batch Ingestion
Historical datasets are fetched from GitHub via **Azure Data Factory**.

### Step 4: Raw Storage (Bronze Layer)
Both streaming and batch data are stored in **Azure Data Lake Storage Gen2**.

### Step 5: Processing in Databricks
Data is processed using **PySpark notebooks** and **Delta Live Pipelines**.

### Step 6: Silver Layer
Data cleaning and transformations:
- Null handling  
- Deduplication  
- Schema validation  
- Data quality checks  

### Step 7: Gold Layer
Analytics-ready tables are created using **Star Schema Modeling**.

---

# 📸 Project Screenshots

## 🚖 Ride Booking Application (Home/Confirmation)

<p align="center">
  <img src="https://github.com/user-attachments/assets/77243a7a-91de-4d00-9cd7-50d9abb9e3a7" width="48%" />
  <img src="https://github.com/user-attachments/assets/9912fe4c-679b-4daf-b0c7-29bdd3553992" width="48%" />
</p>

## 🔄 Azure Data Factory Pipeline

<img width="1917" height="912" alt="ADF pipelines" src="https://github.com/user-attachments/assets/f80581f7-40d2-468b-852e-918ee4b7c387" />

## 📡 Event Hub Monitoring

<img width="1907" height="911" alt="EventHub Stream" src="https://github.com/user-attachments/assets/79a526dc-e892-482f-9ef0-49a3a143a437" />

## ⚡ Databricks Pipeline

<img width="1612" height="841" alt="pipeline" src="https://github.com/user-attachments/assets/ea74377a-6f76-472a-85e8-beb93c929d3a" />

## 🥇 Gold Layer

<img width="1536" height="1024" alt="Gold Layer" src="https://github.com/user-attachments/assets/ed7bd940-15d7-4985-989e-9fb2820a606f" />

## ⭐ Fact & Dimension Tables

<img width="244" height="277" alt="Fact   Dim table" src="https://github.com/user-attachments/assets/c506b389-cecd-4778-b885-c56d25a997ba" />

---

## 🧱 Medallion Architecture

### 🥉 Bronze Layer
Stores raw ingested data from:
- Event Hub
- GitHub datasets

No transformation is applied.

---

### 🥈 Silver Layer
Data cleansing and transformation layer.

Transformations include:
- Removing duplicates  
- Fixing null values  
- Type casting  
- Schema validation  
- Business logic implementation  

---

### 🥇 Gold Layer
Final analytics layer optimized for BI reporting and dashboards.

Contains:
- Fact Table  
- Dimension Tables  

---

## ⭐ Data Model (Star Schema)

### Fact Table
- fact

### Dimension Tables
- dim_booking  
- dim_driver  
- dim_passenger  
- dim_location  
- dim_vehicle  
- dim_payment  

---

## 🔄 Slowly Changing Dimensions (SCD)

This project implements Slowly Changing Dimensions (SCD) in the Gold Layer using **Databricks Auto CDC Flow**.

### SCD Configuration

| Dimension Table | SCD Type |
|----------------|----------|
| dim_location | Type 2 |
| dim_booking | Type 1 |
| dim_driver | Type 1 |
| dim_passenger | Type 1 |
| dim_vehicle | Type 1 |
| dim_payment | Type 1 |

---

### SCD Type 2 Implementation for dim_location

The `dim_location` table is implemented using **SCD Type 2** to preserve historical changes in location-related data.

This ensures that whenever city/location information changes, a new version of the record is created instead of overwriting the old record.

#### Databricks CDC Logic
```python
# dim_location

@dp.table
def dim_location_view():
    df = spark.readStream.table("silver_obt")
    df = df.select(
        "pickup_city_id",
        "pickup_city",
        "city_updated_at",
        "region",
        "state"
    )
    df = df.dropDuplicates(subset=["pickup_city_id", "city_updated_at"])
    return df

dp.create_streaming_table("dim_location")

dp.create_auto_cdc_flow(
  target="dim_location",
  source="dim_location_view",
  keys=["pickup_city_id"],
  sequence_by="city_updated_at",
  stored_as_scd_type=2
)
```

### Why SCD Type 2 for dim_location?
- Preserves historical location changes  
- Tracks changes based on `city_updated_at`  
- Enables historical analytics and auditing  

Example:
- Old Record → Las Vegas  
- Updated Record → New Las Vegas  

Instead of overwriting Las Vegas, a new New Las Vegas record is created with version tracking.

---

### SCD Type 1 for Other Dimensions

All remaining dimension tables use **SCD Type 1**, where old values are overwritten with the latest values.

This is used because historical tracking is not required for:
- Booking details  
- Driver details  
- Passenger details  
- Vehicle details  
- Payment details

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Cloud Platform | Microsoft Azure |
| Data Ingestion | Azure Event Hub, Azure Data Factory |
| Storage | Azure Data Lake Storage Gen2 |
| Processing | Azure Databricks |
| Big Data | Apache Spark |
| Data Format | Delta Lake |
| Programming | Python, SQL, PySpark |
| Modeling | Star Schema |
| Templating | Jinja |
| Version Control | GitHub |

---

## 📂 Project Structure

```bash
Uber_Project/
│
├── adf/
│   └── files_array.json
│
├── bulk-data/
│
├── databricks/
|   ├── uber_rides_ingest/
|   |   └── transformation
|   |       ├── ingest.py
|   |       ├── model.py
|   |       ├── silver.py
|   |       └── silver_obt.sql
│   ├── bronze_adls.py
│   └── silver_obt.py
│
├── web-app/
|   ├── pages/
|   |   ├── confirmation.html
|   |   └── home.html
|   ├── api.py
|   ├── connection.py
|   └── data.py 
│
├── .gitignore
|
├── .python-version
|
├── requirements.txt
|   
└── README.md
```

---

## 📊 Databricks Pipeline

The Databricks pipeline consists of:

### Ingestion Layer
- Raw ride booking data ingestion

### Silver Transformation
- Data cleansing
- Transformation logic

### Modeling Layer
- Fact & Dimension table creation

Pipeline files:
- `ingest.py`
- `silver.py`
- `model.py`

---

## 🔥 Important Concepts Implemented

- Streaming Data Pipeline  
- Batch Data Pipeline  
- ETL Pipeline  
- Medallion Architecture  
- Delta Lake  
- Star Schema  
- Fact & Dimension Modeling  
- Azure Data Engineering Workflow  

---

# 🚀 How to Run

## 1. Clone Repository
```bash
git clone <your-repository-url>
```

---

## 2. Setup Azure Resources
Create the following Azure resources:

- Resource Group  
- Event Hub Namespace  
- Azure Data Factory  
- Storage Account (ADLS Gen2)  
- Azure Databricks Workspace  

---

## 3. Run Ride Booking Website

### Create Virtual Environment
```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows
```bash
venv\Scripts\activate
```

#### Mac/Linux
```bash
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run FastAPI Server
```bash
uvicorn api:app --reload
```

Open browser:
```bash
http://127.0.0.1:8000
```

---

## 4. Generate Ride Booking Events
Book rides using the website to generate streaming events.

---

## 5. Run ADF Pipeline
Run Azure Data Factory pipeline to ingest:
- GitHub Batch Data
- Event Hub Streaming Data

---

## 6. Execute Databricks Pipeline
Run:
- Ingestion Layer  
- Silver Layer  
- Gold Layer  

---

## 7. Validate Final Output
Check:
- Gold Layer Tables  
- Fact Table  
- Dimension Tables    

---

## 📈 Business Use Cases

This architecture can be used in:

- Ride Booking Platforms  
- Logistics Platforms  
- Delivery Applications  
- Real-Time Analytics  
- Customer Behavior Analysis  

---

## 🎯 Learning Outcomes

Through this project, I gained hands-on experience in:

- Building end-to-end data pipelines  
- Working with Azure services  
- Processing streaming data  
- Implementing Medallion Architecture  
- Building Star Schema models  
- Creating production-grade ETL workflows  

---

## 👨‍💻 Author

**Sarthak Agarwal**  
Data Engineer | Azure | Databricks | PySpark | SQL  
