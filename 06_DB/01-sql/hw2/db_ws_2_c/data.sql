SELECT SUM(Total) FROM invoices GROUP BY BillingCountry;
SELECT strftime('%Y', InvoiceDate) AS InvoiceYear, SUM(Total) AS TotalSales
FROM invoices
GROUP BY strftime('%Y', InvoiceDate);
SELECT BillingState, SUM(Total) FROM invoices WHERE BillingCountry = 'USA' AND InvoiceDate > '2010-01-01' GROUP BY BillingState;
SELECT BillingCountry, MAX(Total) 
FROM invoices WHERE BillingCountry = 'Germany' or BillingCountry = 'France' 
GROUP BY BillingCountry;