CREATE TABLE [stg].[Suppliers] (
    [SupplierId]          INT            NULL,
    [SupplierCode]        VARCHAR (8000) NULL,
    [SupplierName]        VARCHAR (8000) NULL,
    [CountryCode]         VARCHAR (8000) NULL,
    [City]                VARCHAR (8000) NULL,
    [CurrencyCode]        VARCHAR (8000) NULL,
    [PaymentTermDays]     SMALLINT       NULL,
    [DefaultLeadTimeDays] SMALLINT       NULL,
    [ActiveFlag]          BIT            NULL,
    [CreatedDate]         DATE           NULL,
    [SilverLoadedAt]      DATETIME2 (6)  NULL
);


GO