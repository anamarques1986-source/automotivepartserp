# Automotive Parts ERP Analytics Platform

End-to-end Microsoft Fabric analytics solution simulating the modernization of a legacy automotive-parts ERP.

The platform implements a Medallion architecture using:

- Microsoft Fabric Data Factory
- OneLake / Lakehouse / Delta
- PySpark notebooks
- Fabric Warehouse and T-SQL
- Direct Lake semantic modelling
- Power BI
- GitHub source control
- DEV → TEST → PROD deployment pipelines

## Architecture

SQL Server / Synthetic ERP
        ↓
Data Factory
        ↓
Bronze Lakehouse
        ↓
PySpark transformations
        ↓
Silver Delta tables
        ↓
Silver-to-Gold Pipeline
        ↓
Fabric Warehouse
        ↓
Direct Lake Semantic Model
        ↓
Power BI Report

