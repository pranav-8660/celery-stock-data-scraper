CREATE TABLE lic_stock_prices(
    id SERIAL PRIMARY KEY,
    price DECIMAL(10,2),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);