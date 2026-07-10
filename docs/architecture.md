# System Architecture

## Project Name

Customer Analytics Data Warehouse

---

# Overview

The Customer Analytics Data Warehouse is designed to collect retail sales data from multiple source files, validate the data, transform it into an analytics-ready format, load it into Snowflake, and provide business insights through Power BI dashboards.

The architecture follows a simple ETL (Extract, Transform, Load) workflow that is commonly used in analytics projects.

---

# Architecture Workflow

```
                    Source Data
                         │
                         ▼
                 CSV Data Files
                         │
                         ▼
              Python Extraction Layer
                         │
                         ▼
             Data Validation & Cleaning
                         │
                         ▼
                Processed CSV Files
                         │
                         ▼
                  Snowflake Stage
                         │
                         ▼
                 Snowflake Raw Tables
                         │
                         ▼
             SQL Transformations (ETL)
                         │
                         ▼
              Fact & Dimension Tables
                         │
                         ▼
                Business SQL Queries
                         │
                         ▼
                Power BI Dashboard
```

---

# Components

## 1. Source Layer

The source layer contains raw business data stored as CSV files.

Datasets include:

- Customers
- Products
- Stores
- Sales

---

## 2. Extraction Layer

Python scripts read the raw CSV files and prepare them for validation.

Responsibilities:

- Read source files
- Check file availability
- Standardize column names
- Log extraction process

---

## 3. Validation Layer

This layer ensures that the data is accurate before loading.

Validation includes:

- Missing values
- Duplicate records
- Invalid dates
- Negative quantities
- Invalid prices
- Data type validation

---

## 4. Processing Layer

The cleaned datasets are saved as processed files.

Tasks include:

- Remove duplicates
- Convert data types
- Standardize values
- Generate validation reports

---

## 5. Snowflake Layer

The processed files are loaded into Snowflake.

Snowflake components include:

- Database
- Schema
- Virtual Warehouse
- Internal Stage
- Raw Tables

---

## 6. Transformation Layer

SQL scripts transform raw tables into analytics-ready tables.

Outputs include:

- Customer Dimension
- Product Dimension
- Store Dimension
- Date Dimension
- Sales Fact Table

---

## 7. Analytics Layer

Business SQL queries generate KPIs such as:

- Revenue
- Orders
- Customers
- Monthly Sales
- Regional Sales
- Top Products

---

## 8. Reporting Layer

Power BI connects to Snowflake and provides interactive dashboards for business users.

Dashboard pages include:

- Executive Summary
- Sales Performance
- Customer Analytics
- Product Analysis
- Regional Performance

---

# Benefits of the Architecture

- Modular design
- Easy to maintain
- Supports data validation
- Optimized for analytics
- Scalable for future enhancements