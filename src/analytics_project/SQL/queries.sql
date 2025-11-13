-- Total sales per customer
SELECT c.customerid, c.preferredcontact, COUNT(s.transactionid) AS num_sales
FROM sales_prepared s
JOIN customers_prepared c ON s.customerid = c.customerid
GROUP BY c.customerid, c.preferredcontact
ORDER BY num_sales DESC;

-- Total sales per product
SELECT p.productid, p.category_1, COUNT(s.transactionid) AS num_sales
FROM sales_prepared s
JOIN products_prepared p ON s.productid = p.productid
GROUP BY p.productid, p.category_1
ORDER BY num_sales DESC;

-- Sales over time
SELECT saledate, COUNT(transactionid) AS num_sales
FROM sales_prepared
GROUP BY saledate
ORDER BY saledate;
