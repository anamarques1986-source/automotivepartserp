CREATE TABLE [dbo].[ProducSupplier] (
    [ProductSupplierId]   INT             NULL,
    [ProductId]           INT             NULL,
    [SupplierId]          INT             NULL,
    [SupplierProductCode] VARCHAR (8000)  NULL,
    [IsPreferredSupplier] BIT             NULL,
    [PurchasePrice]       DECIMAL (18, 2) NULL,
    [LeadTimeDays]        SMALLINT        NULL,
    [MinimumOrderQty]     INT             NULL,
    [ActiveFrom]          DATE            NULL,
    [ActiveTo]            DATE            NULL,
    [SilverLoadedAt]      DATETIME2 (6)   NULL
);


GO