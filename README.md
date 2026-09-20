![Automotive Parts ERP Architecture](Docs/Architecture.png)


# Automotive Parts ERP — Microsoft Fabric Analytics Platform

End-to-end Microsoft Fabric analytics solution simulating the modernization of a legacy automotive-parts ERP.

The project demonstrates a complete analytics workflow using Microsoft Fabric, from raw operational data ingestion to a production-ready Power BI semantic model and CI/CD across DEV, TEST and PROD environments.

> All data used in this project is synthetic and was created exclusively for demonstration and portfolio purposes.

---

## Architecture

The platform follows a Medallion-style architecture:

**SQL Server → Bronze → Silver → Gold/Warehouse → Direct Lake → Power BI**

The solution combines data engineering, dimensional modelling, semantic modelling, business intelligence and CI/CD within Microsoft Fabric.

---

## Business Scenario

The project simulates an automotive-parts company operating a traditional ERP containing data related to:

- Customers
- Products
- Suppliers
- Warehouses
- Salespeople
- Sales
- Purchasing
- Accounts receivable
- Accounts payable
- Product pricing
- Product-supplier relationships

The objective is to modernize this analytical workload using Microsoft Fabric and provide a scalable data platform for reporting and business analysis.

---

## Data Architecture

### Bronze Layer

Raw ERP data is ingested into a Microsoft Fabric Lakehouse.

The Bronze layer preserves source data with minimal transformation and provides the starting point for downstream processing.

**Technology:**

- Microsoft Fabric Data Factory
- OneLake
- Fabric Lakehouse
- Delta tables

---

### Silver Layer

PySpark notebooks transform the raw data into cleaned and standardized datasets.

Typical transformations include:

- Data type standardization
- Data cleansing
- Deduplication
- Business-rule application
- Schema normalization
- Column renaming
- Data validation

Main notebooks:

```text
NB01_Silver_Sales
NB02_Silver_Commercial

Gold Layer

Curated Silver data is loaded into a Fabric Warehouse.

The Gold layer contains analytics-ready dimensional structures designed for reporting and semantic modelling.

The main pipeline responsible for this process is:

PL_Silver_To_Gold


Dimensional Model

The analytical model includes dimensions, facts and relationship tables.

Dimensions

DimCustomer
DimDate
DimProduct
DimSalesperson
DimSupplier
DimWarehouse

Facts

FactSales
FactAccountsReceivable
FactAccountsPayable
Supporting tables
ProductSupplier
ProductPriceList

The model follows a star-schema-oriented design suitable for analytical workloads and Power BI.

Semantic Model

A Power BI Semantic Model is built over the Fabric Warehouse using Direct Lake.

Direct Lake allows Power BI to access data stored in OneLake without requiring a traditional Import refresh of the analytical dataset.

The semantic layer contains:

Relationships
Business measures
DAX calculations
Date intelligence
Business KPIs
Reporting logic

Examples of analytical measures include:

Net Revenue
Total Cost
Margin
Average Ticket
Return Rate
Cancelled Sales %
Previous Year Revenue
Revenue Growth %
Online Revenue %
Active Customers
Power BI

The final analytical layer is delivered through Power BI.

The report is connected to the Fabric Semantic Model and is designed to support analysis of areas such as:

Sales performance
Revenue trends
Product performance
Customers
Suppliers
Warehouses
Accounts receivable
Accounts payable
CI/CD

The project implements separate Microsoft Fabric environments:

GitHub
   │
   ▼
Development
   │
   ▼
Test
   │
   ▼
Production
Source Control

GitHub is connected to the Development workspace.

The repository represents the development source of truth.

TEST and PROD are intentionally not maintained as duplicate Git folders.

Deployment

Microsoft Fabric Deployment Pipelines are used to promote artifacts between environments:

DEV → TEST → PROD

This provides:

Environment isolation
Controlled releases
Repeatable deployments
Separation between development and production workloads
Safer validation before production deployment

Environment-specific connections are validated after deployment so that each semantic model references the Warehouse belonging to its own environment.

Repository Structure
automotivepartserp/
│
├── DEV/
│   ├── AutomotivePartsReport.Report/
│   ├── AutomotiveParts_Bronze_LH.Lakehouse/
│   ├── AutomotiveParts_SModel.SemanticModel/
│   ├── AutomotiveParts__WH.Warehouse/
│   ├── NB01_Silver_Sales.Notebook/
│   ├── NB02_Silver_Commercial.Notebook/
│   └── PL_Silver_To_Gold.DataPipeline/
│
├── docs/
│   └── architecture.png
│
├── LICENSE
└── README.md
Technology Stack
Area	Technology
Source	Synthetic SQL Server ERP
Data Integration	Microsoft Fabric Data Factory
Storage	Microsoft OneLake
Bronze / Silver	Fabric Lakehouse + Delta
Transformation	PySpark
Gold Layer	Fabric Warehouse
SQL	T-SQL
Semantic Layer	Power BI Semantic Model
Connectivity	Direct Lake
Visualization	Power BI
Source Control	GitHub
CI/CD	Fabric Deployment Pipelines
Environments	DEV / TEST / PROD
Key Concepts Demonstrated

This project demonstrates practical implementation of:

Microsoft Fabric architecture
Medallion architecture
Lakehouse and Warehouse integration
Delta Lake
PySpark transformations
Dimensional modelling
Star schema design
T-SQL
Direct Lake
DAX
Power BI semantic modelling
Git integration
Deployment Pipelines
DEV / TEST / PROD environment separation
End-to-end analytics engineering

Screenshots
Additional project screenshots can be added under the docs directory.

Roadmap

Completed:

 Synthetic ERP data source
 Bronze ingestion layer
 PySpark Silver transformations
 Fabric Warehouse Gold layer
 Dimensional model
 Direct Lake semantic model
 Power BI reporting
 GitHub integration
 DEV / TEST / PROD environments
 Fabric Deployment Pipeline

Planned improvements:

 Data quality framework
 Incremental loading / watermarking
 Pipeline audit logging
 Monitoring and observability
 Automated validation tests
 Extended Power BI documentation
Future Enhancements

Future versions of the project may include:

Data Quality

Automated tests for:

Duplicate business keys
Null key values
Referential integrity
Invalid dates
Invalid quantities
Missing customer/product references
Incremental Processing

Implementation of watermark-based ingestion using fields such as:

LastModifiedDate

to process only new or changed records.

Observability

Creation of audit structures to record:

RunId
ProcessName
StartTime
EndTime
RowsRead
RowsWritten
Status
ErrorMessage

This would provide operational monitoring of the platform.

Data Privacy

No real ERP or company data is included in this repository.

All entities, transactions, customers, suppliers, products and financial information used by the project are synthetic.

The project was created solely for learning, demonstration and portfolio purposes.

Purpose

This project was developed to demonstrate practical skills in:

Data Engineering · Analytics Engineering · Microsoft Fabric · Power BI · CI/CD

It represents an end-to-end implementation rather than an isolated dashboard, covering the complete lifecycle from source ingestion to production analytics.
The Warehouse uses a staging-to-dimensional approach before exposing business-ready tables.
