# 🚀 ETL Batch Processing Pipeline (Bronze–Silver–Gold Architecture)

## 📌 Project Overview
This project implements a **modern batch ETL pipeline** using a **Bronze–Silver–Gold data architecture**.  
Synthetic data is generated using **Faker**, stored as CSV files, processed through **Google Cloud Storage** and **Cloud Data Fusion**, and finally loaded into **BigQuery** for analytics and querying.

This pipeline simulates a **real-world enterprise data engineering workflow**.

---

## 🧠 Pipeline Architecture (High-Level Flow)

```text
flowchart TD
    A[Faker Library<br/>Synthetic CSV Data] --> B[GCS – Bronze Layer<br/>Raw CSV Data Storage]
    B --> C[Data Fusion – Silver Layer<br/>Filtering • Masking • Data Validation]
    C --> D[BigQuery – Gold Layer<br/>Analytics-Ready Data]
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#d4af37,stroke:#333,stroke-width:2px
    style C fill:#c0c0c0,stroke:#333,stroke-width:2px
    style D fill:#ffd700,stroke:#333,stroke-width:2px

