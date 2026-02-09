# 🚀 ETL Batch Processing Pipeline (Bronze–Silver–Gold Architecture)

## 📌 Project Overview
This project implements a **modern batch ETL pipeline** using a **Bronze–Silver–Gold data architecture**.  
Synthetic data is generated using **Faker**, stored as CSV files, processed through **Google Cloud Storage** and **Cloud Data Fusion**, and finally loaded into **BigQuery** for analytics and querying.

This pipeline simulates a **real-world enterprise data engineering workflow**.

---

## 🧠 Pipeline Architecture (High-Level Flow)

```text
┌───────────────┐
│ Faker Library │
│ (Synthetic    │
│  CSV Data)    │
└───────┬───────┘
        │
        ▼
┌────────────────────────┐
│   GCS – Bronze Layer   │
│ Raw CSV Data Storage   │
└──────────┬─────────────┘
           │
           ▼
┌────────────────────────┐
│ Data Fusion – Silver   │
│ Filtering              │
│ Masking (PII)          │
│ Data Validation        │
└──────────┬─────────────┘
           │
           ▼
┌────────────────────────┐
│ BigQuery – Gold Layer  │
│ Analytics-Ready Data   │
│ Query & Reporting      │
└────────────────────────┘
