CREATE TABLE [dbo].[FactAccountsReceivable] (
    [AccountsReceivableKey] INT             NULL,
    [SalesDocumentId]       INT             NULL,
    [DocumentNumber]        VARCHAR (8000)  NULL,
    [CustomerKey]           INT             NULL,
    [DocumentDateKey]       INT             NULL,
    [DueDateKey]            INT             NULL,
    [SnapshotDateKey]       INT             NOT NULL,
    [CurrencyCode]          VARCHAR (8000)  NULL,
    [DocumentAmount]        DECIMAL (18, 2) NULL,
    [OutstandingAmount]     DECIMAL (18, 2) NULL,
    [OutstandingPct]        DECIMAL (25, 2) NULL,
    [Status]                VARCHAR (8000)  NULL,
    [DaysPastDue]           INT             NULL,
    [AgingBucket]           VARCHAR (10)    NOT NULL
);


GO