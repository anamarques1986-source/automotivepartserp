# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "74123873-22bf-4d00-8922-f8133e9f6edb",
# META       "default_lakehouse_name": "AutomotiveParts_Bronze_LH",
# META       "default_lakehouse_workspace_id": "0f402b3f-4811-4196-947d-2bb078c8cffe",
# META       "known_lakehouses": [
# META         {
# META           "id": "74123873-22bf-4d00-8922-f8133e9f6edb"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql import functions as F

# Lotes incrementais da execução atual
header_df = spark.table("erp.sales_document_header_incremental")
line_df = spark.table("erp.sales_document_line_incremental")

# Tabela completa de Header usada como referência para descobrir o DocumentType
header_ref_df = (
    spark.table("erp.SalesDocumentHeader")
    .select("SalesDocumentId", "DocumentType")
)

results = []

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ==========================================
# DATA QUALITY - SalesDocumentHeader
# ==========================================

header_rows = header_df.count()

header_null_id = (
    header_df
    .filter(F.col("SalesDocumentId").isNull())
    .count()
)

header_duplicates = (
    header_df
    .groupBy("SalesDocumentId")
    .count()
    .filter(F.col("count") > 1)
    .count()
)

header_null_customer = (
    header_df
    .filter(F.col("CustomerId").isNull())
    .count()
)

header_invalid_document_type = (
    header_df
    .filter(
        F.col("DocumentType").isNull()
        | ~F.col("DocumentType").isin("INV", "DBN", "CRN")
    )
    .count()
)

header_null_gross_amount = (
    header_df
    .filter(F.col("GrossAmount").isNull())
    .count()
)


def status(failed, rows):
    if rows == 0:
        return "SKIP"
    return "PASS" if failed == 0 else "FAIL"


results.extend([
    {
        "SourceTable": "SalesDocumentHeader",
        "RuleName": "SalesDocumentId not null",
        "Severity": "CRITICAL",
        "RowsChecked": header_rows,
        "FailedRows": header_null_id,
        "Status": status(header_null_id, header_rows)
    },
    {
        "SourceTable": "SalesDocumentHeader",
        "RuleName": "SalesDocumentId unique",
        "Severity": "CRITICAL",
        "RowsChecked": header_rows,
        "FailedRows": header_duplicates,
        "Status": status(header_duplicates, header_rows)
    },
    {
        "SourceTable": "SalesDocumentHeader",
        "RuleName": "CustomerId not null",
        "Severity": "HIGH",
        "RowsChecked": header_rows,
        "FailedRows": header_null_customer,
        "Status": status(header_null_customer, header_rows)
    },
    {
        "SourceTable": "SalesDocumentHeader",
        "RuleName": "Valid DocumentType",
        "Severity": "HIGH",
        "RowsChecked": header_rows,
        "FailedRows": header_invalid_document_type,
        "Status": status(header_invalid_document_type, header_rows)
    },
    {
        "SourceTable": "SalesDocumentHeader",
        "RuleName": "GrossAmount not null",
        "Severity": "HIGH",
        "RowsChecked": header_rows,
        "FailedRows": header_null_gross_amount,
        "Status": status(header_null_gross_amount, header_rows)
    }
])

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ==========================================
# DATA QUALITY - SalesDocumentLine
# ==========================================

line_rows = line_df.count()

line_null_id = (
    line_df
    .filter(F.col("SalesLineId").isNull())
    .count()
)

line_duplicates = (
    line_df
    .groupBy("SalesLineId")
    .count()
    .filter(F.col("count") > 1)
    .count()
)

line_null_document = (
    line_df
    .filter(F.col("SalesDocumentId").isNull())
    .count()
)

line_negative_price = (
    line_df
    .filter(F.col("UnitPrice") < 0)
    .count()
)

# Junta as linhas ao Header para conhecer o tipo de documento
line_with_type_df = (
    line_df.alias("l")
    .join(
        header_ref_df.alias("h"),
        F.col("l.SalesDocumentId") == F.col("h.SalesDocumentId"),
        "left"
    )
)

# Linha sem Header correspondente
line_orphan_document = (
    line_with_type_df
    .filter(F.col("h.SalesDocumentId").isNull())
    .count()
)

# Regra de negócio:
# INV / DBN -> Quantity tem de ser > 0
# CRN       -> Quantity tem de ser < 0
# Quantity 0 -> sempre inválida
line_invalid_quantity = (
    line_with_type_df
    .filter(
        (F.col("l.Quantity") == 0)
        |
        (
            F.col("h.DocumentType").isin("INV", "DBN")
            & (F.col("l.Quantity") < 0)
        )
        |
        (
            (F.col("h.DocumentType") == "CRN")
            & (F.col("l.Quantity") > 0)
        )
    )
    .count()
)

results.extend([
    {
        "SourceTable": "SalesDocumentLine",
        "RuleName": "SalesLineId not null",
        "Severity": "CRITICAL",
        "RowsChecked": line_rows,
        "FailedRows": line_null_id,
        "Status": status(line_null_id, line_rows)
    },
    {
        "SourceTable": "SalesDocumentLine",
        "RuleName": "SalesLineId unique",
        "Severity": "CRITICAL",
        "RowsChecked": line_rows,
        "FailedRows": line_duplicates,
        "Status": status(line_duplicates, line_rows)
    },
    {
        "SourceTable": "SalesDocumentLine",
        "RuleName": "SalesDocumentId not null",
        "Severity": "CRITICAL",
        "RowsChecked": line_rows,
        "FailedRows": line_null_document,
        "Status": status(line_null_document, line_rows)
    },
    {
        "SourceTable": "SalesDocumentLine",
        "RuleName": "SalesDocumentId exists in Header",
        "Severity": "CRITICAL",
        "RowsChecked": line_rows,
        "FailedRows": line_orphan_document,
        "Status": status(line_orphan_document, line_rows)
    },
    {
        "SourceTable": "SalesDocumentLine",
        "RuleName": "Quantity sign matches DocumentType",
        "Severity": "HIGH",
        "RowsChecked": line_rows,
        "FailedRows": line_invalid_quantity,
        "Status": status(line_invalid_quantity, line_rows)
    },
    {
        "SourceTable": "SalesDocumentLine",
        "RuleName": "UnitPrice >= 0",
        "Severity": "HIGH",
        "RowsChecked": line_rows,
        "FailedRows": line_negative_price,
        "Status": status(line_negative_price, line_rows)
    }
])

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

results_df = spark.createDataFrame(results)

display(results_df)

failed_rules = [
    r for r in results
    if r["Status"] == "FAIL"
]

dq_status = "FAIL" if len(failed_rules) > 0 else "PASS"

print("Data Quality Status:", dq_status)
print("Failed rules:", len(failed_rules))

notebookutils.notebook.exit(dq_status)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
