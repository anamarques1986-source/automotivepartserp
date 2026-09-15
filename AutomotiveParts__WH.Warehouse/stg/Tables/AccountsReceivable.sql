CREATE TABLE [stg].[AccountsReceivable] (
    [AccountsReceivableId] INT             NULL,
    [SalesDocumentId]      INT             NULL,
    [CustomerId]           INT             NULL,
    [DocumentNumber]       VARCHAR (8000)  NULL,
    [DocumentDate]         DATE            NULL,
    [DueDate]              DATE            NULL,
    [CurrencyCode]         VARCHAR (8000)  NULL,
    [DocumentAmount]       DECIMAL (18, 2) NULL,
    [OutstandingAmount]    DECIMAL (18, 2) NULL,
    [Status]               VARCHAR (8000)  NULL,
    [OutstandingPct]       DECIMAL (25, 2) NULL,
    [SilverLoadedAt]       DATETIME2 (6)   NULL
);


GO