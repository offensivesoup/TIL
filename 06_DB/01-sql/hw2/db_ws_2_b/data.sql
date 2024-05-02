SELECT InvoiceId, InvoiceDate FROM invoices;
SELECT * FROM invoices WHERE BillingCountry = 'USA' AND Total > 10;
SELECT * FROM invoices WHERE BillingCity IN ('London', 'Berlin');
SELECT * FROM invoices WHERE Total = (SELECT MAX(Total) FROM invoices);
SELECT * FROM invoices WHERE InvoiceDate > '2013-03-31' AND Total > 3;
SELECT * FROM invoices WHERE BillingCountry = 'USA' AND BillingState = 'CA' AND Total > 10;
SELECT * FROM invoices WHERE BillingCountry = 'Canada' AND BillingState = 'ON' AND BillingCity = 'Toronto';
SELECT * FROM invoices WHERE InvoiceDate < '2023-01-01' AND (Total >= 50 OR BillingCountry = 'Brazil');