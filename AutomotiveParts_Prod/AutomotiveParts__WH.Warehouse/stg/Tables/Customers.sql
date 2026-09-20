CREATE TABLE [stg].[Customers] (
    [CustomerId]      INT             NULL,
    [CustomerCode]    VARCHAR (8000)  NULL,
    [CustomerName]    VARCHAR (8000)  NULL,
    [CountryCode]     VARCHAR (8000)  NULL,
    [City]            VARCHAR (8000)  NULL,
    [CustomerSegment] VARCHAR (8000)  NULL,
    [PriceTier]       VARCHAR (8000)  NULL,
    [CurrencyCode]    VARCHAR (8000)  NULL,
    [PaymentTermDays] SMALLINT        NULL,
    [CreditLimit]     DECIMAL (18, 2) NULL,
    [ActiveFlag]      BIT             NULL,
    [CreatedDate]     DATE            NULL,
    [SilverLoadedAt]  DATETIME2 (6)   NULL
);


GO