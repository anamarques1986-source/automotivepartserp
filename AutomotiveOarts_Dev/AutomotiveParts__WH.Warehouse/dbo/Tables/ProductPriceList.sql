CREATE TABLE [dbo].[ProductPriceList] (
    [PriceListId]         INT             NULL,
    [ProductId]           INT             NULL,
    [PriceTier]           VARCHAR (8000)  NULL,
    [EffectiveFrom]       DATE            NULL,
    [EffectiveTo]         DATE            NULL,
    [ListPrice]           DECIMAL (18, 2) NULL,
    [MinimumAllowedPrice] DECIMAL (18, 2) NULL,
    [PriceSpread]         DECIMAL (20, 2) NULL,
    [MaximumDiscountPct]  DECIMAL (26, 2) NULL,
    [SilverLoadedAt]      DATETIME2 (6)   NULL
);


GO