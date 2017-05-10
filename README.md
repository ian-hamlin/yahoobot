# Yahoobot

Yahoobot scrapy bot to download symbol data.

# Usage
> pip install requirements.txt
> scrapy crawl yahoosymbols -o test.json

# Example ouput

```javascript
[
{"item_type": "N/A", "company_name": "Pepinnini Minerals Limited", "industry_category": "0.04", "last_price": "0.04", "symbol": "PEIMF", "exchange": "Stocks"},
{"item_type": "N/A", "company_name": "Apple Inc.", "industry_category": "148.96", "last_price": "148.96", "symbol": "AAPL", "exchange": "Stocks"},
{"item_type": "N/A", "company_name": "Aviva plc", "industry_category": "532.00", "last_price": "532.00", "symbol": "AV.L", "exchange": "Stocks"},
{"item_type": "N/A", "company_name": "AstraZeneca PLC", "industry_category": "4605.50", "last_price": "4605.50", "symbol": "AZN.L", "exchange": "Stocks"},
{"item_type": "N/A", "company_name": "Anglo American plc", "industry_category": "1030.50", "last_price": "1030.50", "symbol": "AAL.L", "exchange": "Stocks"},
{"item_type": "N/A", "company_name": "Amazon.com, Inc.", "industry_category": "934.15", "last_price": "934.15", "symbol": "AMZN", "exchange": "Stocks"},
{"item_type": "N/A", "company_name": "Alphabet Inc.", "industry_category": "927.13", "last_price": "927.13", "symbol": "GOOG", "exchange": "Stocks"},
{"item_type": "N/A", "company_name": "British American Tobacco p.l.c.", "industry_category": "5287.00", "last_price": "5287.00", "symbol": "BATS.L", "exchange": "Stocks"},
{"item_type": "N/A", "company_name": "ARM Holdings plc", "industry_category": "1701.90", "last_price": "1701.90", "symbol": "ARM.L", "exchange": "Stocks"},
{"item_type": "N/A", "company_name": "Aberdeen Asset Management PLC", "industry_category": "294.90", "last_price": "294.90", "symbol": "ADN.L", "exchange": "Stocks"},
{"item_type": "N/A", "company_name": "International Consolidated Airlines Group, S.A.", "industry_category": "603.50", "last_price": "603.50", "symbol": "IAG.L", "exchange": "Stocks"},
{"item_type": "N/A", "company_name": "Alexander Mining PLC", "industry_category": "0.13", "last_price": "0.13", "symbol": "AXM.L", "exchange": "Stocks"},
{"item_type": "N/A", "company_name": "Avanti Communications Group PLC", "industry_category": "9.38", "last_price": "9.38", "symbol": "AVN.L", "exchange": "Stocks"},
{"item_type": "N/A", "company_name": "Ascent Resources plc", "industry_category": "1.85", "last_price": "1.85", "symbol": "AST.L", "exchange": "Stocks"},
{"item_type": "N/A", "company_name": "AECOM", "industry_category": "33.81", "last_price": "33.81", "symbol": "ACM", "exchange": "Stocks"},
{"item_type": "N/A", "company_name": "Allianz SE", "industry_category": "173.90", "last_price": "173.90", "symbol": "ALV.DE", "exchange": "Stocks"},
{"item_type": "N/A", "company_name": "88 Energy Limited", "industry_category": "2.85", "last_price": "2.85", "symbol": "88E.L", "exchange": "Stocks"},
{"item_type": "N/A", "company_name": "Swisscom AG", "industry_category": "0.00", "last_price": "0.00", "symbol": "0QKI.L", "exchange": "Stocks"},
{"item_type": "N/A", "company_name": "Daimler AG", "industry_category": "68.52", "last_price": "68.52", "symbol": "DAI.DE", "exchange": "Stocks"},
{"item_type": "N/A", "company_name": "Airbus SE", "industry_category": "75.88", "last_price": "75.88", "symbol": "AIR.PA", "exchange": "Stocks"}
]
```
