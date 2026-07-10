# Data Dictionary

## Project Name

Customer Analytics Data Warehouse

---

# Overview

This document describes the structure of the datasets used in the Customer Analytics Data Warehouse project. It provides details about each table, its purpose, and the columns it contains. The data dictionary acts as a reference for developers, analysts, and business users to understand the data model.

---

# 1. Customer Dimension (dim_customer)

## Purpose

Stores customer profile information used for customer segmentation and sales analysis.

| Column Name | Data Type | Description |
|--------------|----------|-------------|
| customer_id | INTEGER | Unique identifier for each customer |
| first_name | VARCHAR | Customer first name |
| last_name | VARCHAR | Customer last name |
| gender | VARCHAR | Male or Female |
| age | INTEGER | Customer age |
| city | VARCHAR | Customer city |
| state | VARCHAR | Customer state |
| join_date | DATE | Customer registration date |
| customer_segment | VARCHAR | Regular, Premium or VIP |

---

# 2. Product Dimension (dim_product)

## Purpose

Stores product information used for sales reporting.

| Column Name | Data Type | Description |
|--------------|----------|-------------|
| product_id | INTEGER | Unique product identifier |
| product_name | VARCHAR | Product name |
| category | VARCHAR | Product category |
| sub_category | VARCHAR | Product subcategory |
| brand | VARCHAR | Product brand |
| unit_price | DECIMAL | Selling price of one unit |

---

# 3. Store Dimension (dim_store)

## Purpose

Stores information about retail stores.

| Column Name | Data Type | Description |
|--------------|----------|-------------|
| store_id | INTEGER | Unique store identifier |
| store_name | VARCHAR | Store name |
| city | VARCHAR | Store city |
| state | VARCHAR | Store state |
| region | VARCHAR | Business region |

---

# 4. Date Dimension (dim_date)

## Purpose

Provides calendar information for time-based reporting.

| Column Name | Data Type | Description |
|--------------|----------|-------------|
| date_key | INTEGER | Date in YYYYMMDD format |
| full_date | DATE | Complete calendar date |
| day | INTEGER | Day of month |
| month | INTEGER | Month number |
| month_name | VARCHAR | Month name |
| quarter | INTEGER | Quarter number |
| year | INTEGER | Calendar year |
| weekday | VARCHAR | Day name |

---

# 5. Sales Fact Table (fact_sales)

## Purpose

Stores sales transactions and connects all dimension tables.

| Column Name | Data Type | Description |
|--------------|----------|-------------|
| sales_id | INTEGER | Unique sales transaction ID |
| customer_id | INTEGER | References customer |
| product_id | INTEGER | References product |
| store_id | INTEGER | References store |
| date_key | INTEGER | References date dimension |
| quantity | INTEGER | Number of items sold |
| unit_price | DECIMAL | Price per unit |
| discount | DECIMAL | Discount amount |
| sales_amount | DECIMAL | Final sales amount after discount |
| payment_method | VARCHAR | Cash, Card or UPI |