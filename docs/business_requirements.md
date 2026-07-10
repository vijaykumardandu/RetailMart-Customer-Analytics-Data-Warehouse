# Business Requirements Document (BRD)

## Project Name

**Customer Analytics Data Warehouse**

---

# 1. Project Overview

RetailMart is a retail company that sells products through multiple physical stores and an online platform across different regions of India. Every day, thousands of sales transactions are generated from different sources. Since the data is stored in separate files and managed by different teams, preparing business reports has become a manual and time-consuming process.

The goal of this project is to design and build a centralized Customer Analytics Data Warehouse that collects, validates, and stores business data in a structured format. This solution will help management access reliable business insights through interactive dashboards instead of relying on manual reports.

---

# 2. Business Problem

The current reporting process has several challenges:

* Sales data is maintained in multiple CSV files without a centralized storage system.
* Different departments generate reports using different datasets, resulting in inconsistent business metrics.
* Manual report preparation consumes significant time and increases the possibility of errors.
* Management does not have access to real-time or reliable business insights for decision-making.
* There is no standard process for validating data before it is used for reporting.

These challenges make it difficult for the business to monitor performance and identify opportunities for improvement.

---

# 3. Project Objective

The primary objective of this project is to build a scalable analytics solution that:

* Consolidates sales data from multiple sources.
* Performs data validation and quality checks.
* Stores cleaned data in a Snowflake data warehouse.
* Supports analytical SQL queries for business reporting.
* Provides interactive dashboards for business users.
* Enables faster and more accurate business decision-making.

---

# 4. Expected Business Benefits

The proposed solution will provide the following benefits:

* Reduce manual effort involved in preparing business reports.
* Improve the accuracy and consistency of sales data.
* Enable faster access to important business KPIs.
* Help management identify sales trends and customer purchasing patterns.
* Support data-driven decision-making across departments.
* Create a scalable foundation for future analytics initiatives.

---

# 5. Stakeholders

| Stakeholder         | Responsibility                                             |
| ------------------- | ---------------------------------------------------------- |
| CEO                 | Monitor overall business performance and strategic growth  |
| Sales Manager       | Track sales performance and identify revenue opportunities |
| Marketing Manager   | Analyze customer behavior and campaign effectiveness       |
| Finance Team        | Monitor revenue, profitability, and financial reporting    |
| Operations Team     | Evaluate store performance and operational efficiency      |
| Data Analytics Team | Build, maintain, and enhance the analytics solution        |

---

# 6. Business Questions

The analytics platform should help answer the following business questions:

1. What is the total revenue generated during a selected period?
2. Which products contribute the highest revenue?
3. Which product categories perform the best?
4. Which cities and regions generate the most sales?
5. Which stores require business attention due to low performance?
6. Who are the top customers based on purchase value?
7. How do sales change month over month?
8. What is the average order value?
9. How many customers make repeat purchases?
10. Which product categories show declining sales trends?

---

# 7. Key Performance Indicators (KPIs)

The dashboard will focus on the following business metrics:

* Total Revenue
* Total Orders
* Total Customers
* Average Order Value
* Monthly Revenue Growth
* Customer Retention Rate
* Revenue by Product Category
* Revenue by Store
* Revenue by Region
* Top Selling Products
* Top Customers

---

# 8. Project Scope

### In Scope

* Customer data analysis
* Product information
* Store information
* Sales transaction analysis
* Data validation and cleansing
* Snowflake data warehouse implementation
* SQL-based reporting
* Interactive Power BI dashboard

### Out of Scope

* Machine Learning models
* Demand forecasting
* Product recommendation systems
* Inventory optimization
* Real-time streaming analytics

---

# 9. Data Sources

The project will initially use structured CSV files to simulate operational business data.

| Dataset   | Format    | Description                      |
| --------- | --------- | -------------------------------- |
| Customers | CSV       | Customer profile information     |
| Products  | CSV       | Product catalog                  |
| Stores    | CSV       | Store details                    |
| Sales     | CSV       | Sales transactions               |
| Date      | Generated | Calendar dimension for reporting |

In future enhancements, additional data sources such as REST APIs can be integrated into the ETL pipeline.

---

# 10. Business Assumptions

The following assumptions are considered during the project:

* Every customer has a unique Customer ID.
* Every product has a unique Product ID.
* Every store has a unique Store ID.
* Each sales transaction belongs to one customer and one store.
* Sales amount is calculated after applying any discounts.
* All transaction dates are valid and available for reporting.

---

# 11. Potential Risks

Possible data quality issues include:

* Missing customer information
* Duplicate sales transactions
* Invalid product IDs
* Incorrect pricing data
* Missing store records
* Invalid transaction dates

These issues will be identified and handled through the data validation process before loading data into the warehouse.

---

# 12. Success Criteria

The project will be considered successful when:

* All datasets are successfully loaded into Snowflake.
* Data quality validation rules execute without critical failures.
* Fact and dimension tables are created successfully.
* Business KPIs are calculated accurately.
* Interactive dashboards display correct and consistent information.
* Business reports match the validated source data.
* The overall reporting process becomes faster and easier compared to manual reporting.

---

# 13. Future Enhancements

This project can be extended in the future by adding:

* Automated API-based data ingestion
* Incremental ETL pipelines
* Scheduled data refresh using orchestration tools
* Advanced customer segmentation
* Sales forecasting using Machine Learning
* Real-time business dashboards
