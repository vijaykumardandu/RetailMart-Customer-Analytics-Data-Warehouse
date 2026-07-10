# Entity Relationship Diagram (ERD)

## Project Name

Customer Analytics Data Warehouse

---

# Overview

The Customer Analytics Data Warehouse uses a **Star Schema** to support fast analytical queries and reporting.

The central table is the **Sales Fact Table**, which stores transactional data. It is connected to four dimension tables that provide descriptive information about customers, products, stores, and dates.

This design simplifies reporting, improves query performance, and follows common data warehousing practices.

---

# Star Schema

```
                    +----------------------+
                    |    dim_customer      |
                    +----------------------+
                    | customer_id (PK)     |
                    | first_name           |
                    | last_name            |
                    | gender               |
                    | age                  |
                    | city                 |
                    | state                |
                    | join_date            |
                    | customer_segment     |
                    +----------------------+
                              |
                              |
                              |
+----------------------+      |      +----------------------+
|    dim_product       |------|------|      dim_store       |
+----------------------+      |      +----------------------+
| product_id (PK)      |      |      | store_id (PK)        |
| product_name         |      |      | store_name           |
| category             |      |      | city                 |
| sub_category         |      |      | state                |
| brand                |      |      | region               |
| unit_price           |      |      +----------------------+
+----------------------+      |
                              |
                              |
                     +----------------------+
                     |     fact_sales       |
                     +----------------------+
                     | sales_id (PK)        |
                     | customer_id (FK)     |
                     | product_id (FK)      |
                     | store_id (FK)        |
                     | date_key (FK)        |
                     | quantity             |
                     | unit_price           |
                     | discount             |
                     | sales_amount         |
                     | payment_method       |
                     +----------------------+
                              |
                              |
                              |
                     +----------------------+
                     |      dim_date        |
                     +----------------------+
                     | date_key (PK)        |
                     | full_date            |
                     | day                  |
                     | month                |
                     | month_name           |
                     | quarter              |
                     | year                 |
                     | weekday              |
                     +----------------------+
```

---

# Table Relationships

| Parent Table | Child Table | Relationship |
|--------------|-------------|--------------|
| dim_customer | fact_sales | One Customer → Many Sales |
| dim_product | fact_sales | One Product → Many Sales |
| dim_store | fact_sales | One Store → Many Sales |
| dim_date | fact_sales | One Date → Many Sales |

---

# Why Star Schema?

The Star Schema was selected because it:

- Simplifies SQL queries.
- Improves reporting performance.
- Works efficiently with Snowflake.
- Supports Power BI dashboards.
- Is easy for business users to understand.

---

# Fact Table

The **fact_sales** table stores measurable business events such as sales transactions.

Measures include:

- Quantity
- Unit Price
- Discount
- Sales Amount

---

# Dimension Tables

Dimension tables describe the business entities involved in each sale.

They include:

- Customer
- Product
- Store
- Date

These tables provide context for analysis while keeping the fact table optimized for reporting.