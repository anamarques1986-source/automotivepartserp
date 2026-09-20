# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "209c2b7c-7be5-4549-911d-f9ff7f78b0f8",
# META       "default_lakehouse_name": "AutomotiveParts_Bronze_LH",
# META       "default_lakehouse_workspace_id": "50db6baa-a804-4159-9e33-fc8ed6d30af5",
# META       "known_lakehouses": [
# META         {
# META           "id": "209c2b7c-7be5-4549-911d-f9ff7f78b0f8"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
from pyspark.sql import functions as F

# ---------------------------------------
# PRODUCT - SUPPLIER
# ---------------------------------------

df_product_supplier = (
    spark.table("erp.ProductSupplier")
    .dropDuplicates(["ProductSupplierId"])
    .withColumn(
        "IsPreferredSupplier",
        F.col("IsPreferredSupplier").cast("boolean")
    )
    .withColumn("SilverLoadedAt", F.current_timestamp())
)

df_product_supplier.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("silver.ProductSupplier")


# ---------------------------------------
# PRODUCT PRICE LIST
# ---------------------------------------

df_price_list = (
    spark.table("erp.ProductPriceList")
    .dropDuplicates(["PriceListId"])
    .withColumn("PriceTier", F.trim("PriceTier"))
    .withColumn(
        "PriceSpread",
        F.round(
            F.col("ListPrice") -
            F.col("MinimumAllowedPrice"),
            2
        )
    )
    .withColumn(
        "MaximumDiscountPct",
        F.when(
            F.col("ListPrice") > 0,
            F.round(
                (
                    1 -
                    F.col("MinimumAllowedPrice") /
                    F.col("ListPrice")
                ) * 100,
                2
            )
        )
    )
    .withColumn("SilverLoadedAt", F.current_timestamp())
)

df_price_list.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("silver.ProductPriceList")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ---------------------------------------
# ACCOUNTS RECEIVABLE
# ---------------------------------------

df_ar = (
    spark.table("erp.AccountsReceivable")
    .dropDuplicates(["AccountsReceivableId"])
    .withColumn(
        "OutstandingPct",
        F.when(
            F.col("DocumentAmount") != 0,
            F.round(
                F.col("OutstandingAmount") /
                F.col("DocumentAmount") * 100,
                2
            )
        )
    )
    .withColumn("SilverLoadedAt", F.current_timestamp())
)

df_ar.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("silver.AccountsReceivable")


# ---------------------------------------
# ACCOUNTS PAYABLE
# ---------------------------------------

df_ap = (
    spark.table("erp.AccountsPayable")
    .dropDuplicates(["AccountsPayableId"])
    .withColumn(
        "OutstandingPct",
        F.when(
            F.col("DocumentAmount") != 0,
            F.round(
                F.col("OutstandingAmount") /
                F.col("DocumentAmount") * 100,
                2
            )
        )
    )
    .withColumn("SilverLoadedAt", F.current_timestamp())
)

df_ap.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("silver.AccountsPayable")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

tables = [
    "silver.ProductSupplier",
    "silver.ProductPriceList",
    "silver.AccountsReceivable",
    "silver.AccountsPayable"
]

for table in tables:
    print(table, spark.table(table).count())

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
