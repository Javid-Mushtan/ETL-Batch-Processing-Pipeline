# 🚀 Employee ETL Data Pipeline  
**Python • Faker • Google Cloud • Medallion Architecture**

This project showcases an **end-to-end Data Engineering ETL pipeline** that generates synthetic employee data using Python and Faker, processes it through a **Bronze–Silver–Gold (Medallion) architecture**, and stores analytics-ready data using **Google Cloud Platform**.  

The pipeline simulates a real-world enterprise data flow, focusing on **data quality, scalability, and cloud-native design**.

---

## 📌 Key Concepts Demonstrated

| Concept | Description |
|---------|-------------|
| ✅ **ETL Pipeline Design** | Complete flow from data generation to analytics |
| ✅ **Medallion Architecture** | Bronze (raw), Silver (cleaned), Gold (enriched) layers |
| ✅ **Cloud Object Storage** | Scalable storage with Google Cloud Storage |
| ✅ **Data Transformation & Validation** | Cleaning, typing, and standardization |
| ✅ **Analytics-Ready Data Modeling** | Optimized for querying in BigQuery |
| ✅ **Secure Cloud Authentication** | Service Account-based secure access |

---

## 📊 Architecture Overview

```mermaid
graph TD
    A[Python + Faker] --> B[GCS: Bronze Layer<br/>Raw CSV Data]
    B --> C[Data Fusion: Silver Layer<br/>Cleaned & Validated]
    C --> D[BigQuery: Gold Layer<br/>Analytics-Ready Tables]
    D --> E[📈 Analytics / Dashboards]
    D --> F[📋 HTML Table View]

## Key Concepts Demonstrated

| Concept | Description |
|---|---|
| ETL Pipeline Design | Complete flow from data generation to analytics |
| Medallion Architecture | Bronze (raw), Silver (cleaned), Gold (enriched) layers |
| Cloud Object Storage | Scalable storage with Google Cloud Storage |
| Data Transformation & Validation | Cleaning, typing, and standardization |
| Analytics-Ready Data Modeling | Optimized for querying in BigQuery |
| Secure Cloud Authentication | Service Account-based secure access |

---

| Employee Dataset Schema | | |
|---|---|---|
| Column Name | Description | Data Type |
| employee_id | Unique identifier for each employee | INTEGER |
| full_name | Employee full name | STRING |
| email | Official email address | STRING |
| phone_number | Contact number | STRING |
| department | Department name | STRING |
| job_title | Job designation | STRING |
| salary | Monthly salary | FLOAT |
| hire_date | Joining date | DATE |
| country | Country of employment | STRING |
| **Total Columns:** 9 | **Data Type:** Structured (CSV → Table) | |

---

| Tech Stack | |
|---|---|
| Category | Tools |
| Language | Python |
| Data Generation | Faker |
| Storage | Google Cloud Storage |
| Transformation | Google Data Fusion |
| Analytics | Google BigQuery |
| Querying | SQL |
| Visualization | HTML |

## ⚙️ Bronze Layer — Raw Data Storage

### ⭐ Description
Employee records are generated using Faker. Stored in raw CSV format. Uploaded directly to Google Cloud Storage. No transformations applied.

### 🎯 Purpose
- Maintain original source data
- Enable reprocessing & auditability

---

## 🛠️ Silver Layer — Data Cleaning & Transformation

### ⭐ Description
Data ingested from GCS Bronze layer. Transformed using Google Data Fusion. Operations performed:
- Schema enforcement
- Data type casting
- Null & invalid value handling
- Standardized column names

### 🎯 Purpose
- Improve data reliability
- Ensure consistency across datasets

---

## 🥇 Gold Layer — Analytics-Ready Data

### ⭐ Description
Cleaned data loaded into Google BigQuery. Stored in a structured, query-optimized format. Designed for fast analytical queries.

### 📊 Usage
- SQL analytics
- Business reporting
- HTML table visualization
- BI tools integration

---

## 🔐 Cloud Authentication & Security

### ⭐ Description
This project uses Google Cloud Service Account authentication for secure access.

### 🔑 Authentication Method
- Service Account with JSON key file
- Non-interactive, production-ready authentication
- Access controlled via IAM roles
