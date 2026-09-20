CREATE TABLE [stg].[Sales] (
    [SalesLineId]       BIGINT          NULL,
    [SalesDocumentId]   INT             NULL,
    [DocumentNumber]    VARCHAR (8000)  NULL,
    [DocumentType]      VARCHAR (8000)  NULL,
    [DocumentDate]      DATE            NULL,
    [DueDate]           DATE            NULL,
    [CustomerId]        INT             NULL,
    [ProductId]         INT             NULL,
    [WarehouseId]       INT             NULL,
    [SalespersonId]     INT             NULL,
    [LineNumber]        SMALLINT        NULL,
    [Quantity]          DECIMAL (18, 3) NULL,
    [UnitPrice]         DECIMAL (18, 2) NULL,
    [DiscountPct]       DECIMAL (8, 2)  NULL,
    [NetAmount]         DECIMAL (18, 2) NULL,
    [TaxRate]           DECIMAL (8, 2)  NULL,
    [TaxAmount]         DECIMAL (18, 2) NULL,
    [GrossAmount]       DECIMAL (18, 2) NULL,
    [UnitCost]          DECIMAL (18, 2) NULL,
    [CostAmount]        DECIMAL (18, 2) NULL,
    [GrossMarginAmount] DECIMAL (18, 2) NULL,
    [GrossMarginPct]    DECIMAL (25, 2) NULL,
    [DocumentYear]      INT             NULL,
    [DocumentMonth]     INT             NULL,
    [SilverLoadedAt]    DATETIME2 (6)   NULL
);


GO