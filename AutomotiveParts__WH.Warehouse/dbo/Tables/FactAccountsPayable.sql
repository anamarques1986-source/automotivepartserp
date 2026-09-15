CREATE TABLE [dbo].[FactAccountsPayable] (
    [AccountsPayableKey]    INT             NULL,
    [SupplierKey]           INT             NULL,
    [SupplierInvoiceNumber] VARCHAR (8000)  NULL,
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