![Automotive Parts ERP Architecture](Docs/Architecture.png)


# Automotive Parts ERP — Microsoft Fabric Analytics Platform

End-to-end Microsoft Fabric analytics solution simulating the modernization of a legacy automotive-parts ERP.

The project demonstrates a complete analytics workflow, from operational data ingestion and transformation to dimensional modelling, Direct Lake semantic modelling, Power BI reporting, Git source control, and controlled deployment across DEV, TEST and PROD environments.

> All data used in this project is synthetic and was created exclusively for learning, demonstration and portfolio purposes.

---

### End-to-End Data Flow

```text
Synthetic SQL Server ERP
        ↓
Microsoft Fabric Data Factory
        ↓
Bronze Lakehouse
        ↓
PySpark Transformations
        ↓
Silver Delta Tables
        ↓
Silver-to-Gold Pipeline
        ↓
Warehouse STG
        ↓
T-SQL Transformations
        ↓
Gold Fabric Warehouse
        ↓
Direct Lake Semantic Model
        ↓
Power BI

The platform follows a Medallion-style architecture:

SQL Server → Bronze → Silver → Gold / Warehouse → Direct Lake → Power BI
```text
Business Scenario

The project simulates the analytics modernization of an automotive-parts company operating a traditional ERP environment.

The synthetic ERP dataset contains business entities related to:

Customers
Products
Suppliers
Warehouses
Salespeople
Sales transactions
Product pricing
Product-supplier relationships
Accounts receivable
Accounts payable

The objective is to transform operational ERP data into a modern cloud analytics platform using Microsoft Fabric.

Bronze Layer

The Bronze layer represents the raw ingestion area of the platform.

Operational ERP data is ingested into a Microsoft Fabric Lakehouse with minimal transformation, preserving the original source structure as much as possible.

Technologies
Microsoft Fabric Data Factory
Microsoft OneLake
Fabric Lakehouse
Delta tables
Purpose

The Bronze layer provides:

Raw source preservation
Centralized ingestion
Separation between source systems and transformation logic
A reliable starting point for downstream processing
Silver Layer

The Silver layer contains cleaned, standardized and business-ready intermediate datasets.

PySpark notebooks transform the Bronze data before it is consumed by the analytical Warehouse layer.

Main Notebooks
NB01_Silver_Sales
NB02_Silver_Commercial

Typical Transformations
Data type standardization
Column normalization
Data cleansing
Deduplication
Business-rule application
Schema normalization
Validation of key fields
Preparation of analytical entities

Silver data is stored as Delta tables in the Fabric Lakehouse.

Gold Layer

The Gold layer is implemented in Microsoft Fabric Warehouse.

It contains the curated, dimensional and analytics-ready data model used by the Power BI Semantic Model.

Data from the Silver layer is first loaded into staging tables and then transformed into final dimension, fact and supporting tables.

Gold Processing Flow
Silver Delta Tables
        ↓
Warehouse STG
        ↓
T-SQL Transformations
        ↓
Gold / dbo
        ↓
Direct Lake Semantic Model

The permanent pipeline responsible for the Silver-to-Gold process is:

PL_Silver_To_Gold
Purpose of the Gold Layer

The Gold layer provides:

Business-ready analytical data
Dimensional modelling
Stable reporting structures
Reusable facts and dimensions
A performant source for the Power BI Semantic Model
Dimensional Model

The Fabric Warehouse contains a star-schema-oriented analytical model.

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
Supporting Tables
ProductSupplier
ProductPriceList

The dimensional design separates descriptive business entities from transactional data and supports efficient analytical reporting.

Semantic Model

The analytical Warehouse is consumed through a Power BI Semantic Model using Direct Lake.

Direct Lake allows the semantic layer to access data stored in OneLake without relying on a traditional imported Power BI dataset.

The Semantic Model contains:

Table relationships
Business measures
DAX calculations
Date intelligence
KPIs
Reporting logic
Example Measures
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

The model provides a reusable semantic layer between the physical Warehouse and Power BI reporting.

Power BI

The final analytical experience is delivered through Power BI.

The report is connected to the Direct Lake Semantic Model and supports analysis across multiple business areas.

Examples include:

Revenue performance
Sales trends
Product performance
Customer analysis
Supplier analysis
Warehouse performance
Accounts receivable
Accounts payable
CI/CD Architecture

The project includes separate environments for development, testing and production.

GitHub
   ↕
Development
   ↓
Test
   ↓
Production
Environments
AutomotiveParts_DEV
AutomotiveParts_TEST
AutomotiveParts_PROD

Microsoft Fabric Deployment Pipelines are used to promote artifacts between environments:

DEV → TEST → PROD

This provides:

Environment isolation
Controlled deployments
Validation before production
Repeatable releases
Separation between development and production workloads
Git Source Control

GitHub is used as the source-control system for the project.

The Development workspace is connected to Git.

TEST and PROD are not maintained as duplicate folders in the repository. Instead, artifacts are promoted using Fabric Deployment Pipelines.

Source-Control Flow
GitHub
   ↕
DEV Workspace
   ↓
Deployment Pipeline
   ↓
TEST
   ↓
PROD

This keeps Git focused on development while Fabric Deployment Pipelines manage environment promotion.

Environment-Specific Direct Lake Connections

Each environment contains its own Fabric Warehouse and Semantic Model.

The Semantic Model in each environment is configured to access the Warehouse belonging to that same environment.

DEV Semantic Model  → DEV Warehouse
TEST Semantic Model → TEST Warehouse
PROD Semantic Model → PROD Warehouse

This prevents TEST or PROD reports from accidentally querying data from another environment.

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
Data Lake	Microsoft OneLake
Bronze Layer	Fabric Lakehouse
Silver Layer	Delta Lake + PySpark
Transformation	PySpark / T-SQL
Gold Layer	Microsoft Fabric Warehouse
Staging	Warehouse STG schema
Analytical Model	Star Schema
Semantic Layer	Power BI Semantic Model
Connectivity	Direct Lake
BI	Power BI
Source Control	GitHub
CI/CD	Fabric Deployment Pipelines
Environments	DEV / TEST / PROD
Key Concepts Demonstrated

The project demonstrates practical implementation of:

End-to-end Microsoft Fabric architecture
Medallion architecture
Lakehouse architecture
Delta Lake
PySpark transformations
Microsoft Fabric Warehouse
Staging-to-Gold processing
Dimensional modelling
Star schema design
T-SQL
DAX
Direct Lake
Power BI Semantic Models
Power BI reporting
Git source control
CI/CD
Deployment Pipelines
DEV / TEST / PROD separation
Environment-specific data connections
Data Flow Summary
1. Source

Synthetic ERP data represents a traditional SQL Server operational system.

2. Bronze

Raw source data is ingested into the Fabric Lakehouse.

3. Silver

PySpark notebooks cleanse, standardize and prepare the data.

4. Staging

Silver datasets are transferred into Warehouse staging structures.

5. Gold

T-SQL transformations create business-ready facts, dimensions and supporting tables.

6. Semantic Layer

A Direct Lake Semantic Model provides relationships, measures and analytical logic.

7. Reporting

Power BI delivers the final analytical experience.

Current Project Status

Completed:

 Synthetic ERP dataset
 Fabric Lakehouse
 Bronze ingestion layer
 PySpark Silver transformations
 Delta tables
 Fabric Warehouse
 Staging layer
 Gold dimensional model
 Dimension tables
 Fact tables
 T-SQL transformations
 Direct Lake Semantic Model
 DAX business measures
 Power BI report
 GitHub integration
 DEV environment
 TEST environment
 PROD environment
 Fabric Deployment Pipeline
 Environment-specific Direct Lake connections
Roadmap

Planned improvements include:

 Data quality framework
 Incremental loading
 Watermark-based processing
 Audit logging
 Pipeline monitoring
 Automated validation tests
 Improved observability
 Extended technical documentation
Planned Data Quality Framework

A future data-quality notebook can validate conditions such as:

Duplicate business keys
Null primary keys
Orphan foreign keys
Invalid dates
Negative quantities
Missing product references
Missing customer references
Unexpected row-count variations

The objective is to detect data issues before data reaches the Gold analytical layer.

Planned Incremental Processing

A future version of the project can introduce watermark-based incremental loading.

Example:

LastModifiedDate
        ↓
Read previous watermark
        ↓
Process only new / changed rows
        ↓
Write Delta changes
        ↓
Update watermark

This would reduce unnecessary full-load processing and better simulate a production data-engineering workload.

Planned Audit and Observability

An audit structure can be introduced to capture operational metadata such as:

RunId
ProcessName
Environment
StartTime
EndTime
RowsRead
RowsWritten
Status
ErrorMessage

This would improve troubleshooting, monitoring and operational visibility.

Data Privacy

No real ERP, customer, supplier or financial data is included in this repository.

All data used in the project is synthetic.

The project was created solely for:

Learning
Technical experimentation
Microsoft Fabric practice
Data Engineering demonstration
Power BI demonstration
Portfolio presentation
Project Purpose

This project demonstrates the design and implementation of a complete analytics platform rather than an isolated dashboard.

It covers the full lifecycle:

Source
  ↓
Data Ingestion
  ↓
Data Engineering
  ↓
Data Transformation
  ↓
Dimensional Modelling
  ↓
Semantic Modelling
  ↓
Business Intelligence
  ↓
CI/CD
  ↓
Production Deployment

The project showcases practical skills across:

Microsoft Fabric · Data Engineering · Analytics Engineering · PySpark · SQL · Direct Lake · Power BI · Git · CI/CD
