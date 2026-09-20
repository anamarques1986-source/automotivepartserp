# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "f7dd775c-1a23-4af8-98bf-8a4b59090787",
# META       "default_lakehouse_name": "AutomotiveParts_Bronze_LH",
# META       "default_lakehouse_workspace_id": "ca6eeb3e-afa8-4c03-81ca-19d7115d6e7a",
# META       "known_lakehouses": [
# META         {
# META           "id": "f7dd775c-1a23-4af8-98bf-8a4b59090787"
# META         }
# META       ]
# META     },
# META     "warehouse": {}
# META   }
# META }

# CELL ********************

from pyspark.sql import functions as F

# Create Silver schema
spark.sql("CREATE SCHEMA IF NOT EXISTS silver")

# Read Bronze/source tables
df_header = spark.table("erp.SalesDocumentHeader")
df_line = spark.table("erp.SalesDocumentLine")

print("SalesDocumentHeader:", df_header.count())
print("SalesDocumentLine:", df_line.count())

display(df_header.limit(5))
display(df_line.limit(5))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_sales = (
    df_line.alias("l")
    .join(
        df_header.alias("h"),
        F.col("l.SalesDocumentId") == F.col("h.SalesDocumentId"),
        "inner"
    )
    .select(
        F.col("l.SalesLineId"),
        F.col("l.SalesDocumentId"),
        F.col("h.DocumentNumber"),
        F.col("h.DocumentType"),
        F.col("h.DocumentDate"),
        F.col("h.DueDate"),
        F.col("h.CustomerId"),
        F.col("l.ProductId"),
        F.col("l.WarehouseId"),
        F.col("h.SalespersonId"),
        F.col("l.LineNumber"),
        F.col("l.Quantity"),
        F.col("l.UnitPrice"),
        F.col("l.DiscountPct"),
        F.col("l.NetAmount"),
        F.col("l.TaxRate"),
        F.col("l.TaxAmount"),
        F.col("l.GrossAmount"),
        F.col("l.UnitCost"),
        F.col("l.CostAmount"),
        F.col("l.GrossMarginAmount")
    )
    .withColumn(
        "GrossMarginPct",
        F.when(
            F.col("NetAmount") != 0,
            F.round(
                F.col("GrossMarginAmount") / F.col("NetAmount") * 100,
                2
            )
        )
    )
    .withColumn("DocumentYear", F.year("DocumentDate"))
    .withColumn("DocumentMonth", F.month("DocumentDate"))
    .withColumn("SilverLoadedAt", F.current_timestamp())
)

print("Silver Sales rows:", df_sales.count())

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

print("Duplicate SalesLineId:",
      df_sales.groupBy("SalesLineId")
              .count()
              .filter(F.col("count") > 1)
              .count())

print("Null ProductId:",
      df_sales.filter(F.col("ProductId").isNull()).count())

print("Null CustomerId:",
      df_sales.filter(F.col("CustomerId").isNull()).count())

print("Null DocumentDate:",
      df_sales.filter(F.col("DocumentDate").isNull()).count())

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(
    df_sales
    .groupBy("DocumentType")
    .agg(
        F.count("*").alias("Rows"),
        F.round(F.sum("NetAmount"), 2).alias("NetAmount"),
        F.round(F.sum("GrossMarginAmount"), 2).alias("GrossMargin")
    )
    .orderBy("DocumentType")
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

(
    df_sales
    .write
    .format("delta")
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .saveAsTable("silver.Sales")
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.table("silver.Sales").count()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql import functions as F

# -------------------------
# CUSTOMERS
# -------------------------
df_customers = (
    spark.table("erp.Customers")
    .dropDuplicates(["CustomerId"])
    .withColumn("CustomerName", F.trim("CustomerName"))
    .withColumn("City", F.trim("City"))
    .withColumn("ActiveFlag", F.col("ActiveFlag").cast("boolean"))
    .withColumn("SilverLoadedAt", F.current_timestamp())
)

df_customers.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("silver.Customers")


# -------------------------
# PRODUCTS
# -------------------------
df_products = (
    spark.table("erp.Products")
    .dropDuplicates(["ProductId"])
    .withColumn("ProductName", F.trim("ProductName"))
    .withColumn("Category", F.trim("Category"))
    .withColumn("Subcategory", F.trim("Subcategory"))
    .withColumn("Brand", F.trim("Brand"))
    .withColumn("ActiveFlag", F.col("ActiveFlag").cast("boolean"))
    .withColumn("SilverLoadedAt", F.current_timestamp())
)

df_products.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("silver.Products")


# -------------------------
# SUPPLIERS
# -------------------------
df_suppliers = (
    spark.table("erp.Suppliers")
    .dropDuplicates(["SupplierId"])
    .withColumn("SupplierName", F.trim("SupplierName"))
    .withColumn("City", F.trim("City"))
    .withColumn("ActiveFlag", F.col("ActiveFlag").cast("boolean"))
    .withColumn("SilverLoadedAt", F.current_timestamp())
)

df_suppliers.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("silver.Suppliers")


# -------------------------
# WAREHOUSES
# -------------------------
df_warehouses = (
    spark.table("erp.Warehouses")
    .dropDuplicates(["WarehouseId"])
    .withColumn("WarehouseName", F.trim("WarehouseName"))
    .withColumn("City", F.trim("City"))
    .withColumn("ActiveFlag", F.col("ActiveFlag").cast("boolean"))
    .withColumn("SilverLoadedAt", F.current_timestamp())
)

df_warehouses.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("silver.Warehouses")


# -------------------------
# SALESPERSONS
# -------------------------
df_salespersons = (
    spark.table("erp.Salespersons")
    .dropDuplicates(["SalespersonId"])
    .withColumn("SalespersonName", F.trim("SalespersonName"))
    .withColumn("ActiveFlag", F.col("ActiveFlag").cast("boolean"))
    .withColumn("SilverLoadedAt", F.current_timestamp())
)

df_salespersons.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("silver.Salespersons")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

tables = [
    "silver.Customers",
    "silver.Products",
    "silver.Suppliers",
    "silver.Warehouses",
    "silver.Salespersons",
    "silver.Sales"
]

for table in tables:
    print(table, spark.table(table).count())

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
