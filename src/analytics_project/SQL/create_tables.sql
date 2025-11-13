-- Turn on foreign key checking (SQLite needs this)
PRAGMA foreign_keys = ON;

-- Customers dimension
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    region TEXT,
    join_date TEXT,
    customer_type TEXT,       -- new column
    loyalty_points INTEGER,   -- new column
    preferred_contact TEXT    -- new column
);

-- Products dimension
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    brand TEXT,               -- new column
    supplier TEXT,            -- new column
    unit_price REAL,
    stock_level INTEGER        -- new column
);

-- Dates dimension
CREATE TABLE dates (
    date_id INTEGER PRIMARY KEY,
    date TEXT,
    month INTEGER,
    quarter INTEGER,
    year INTEGER
);

-- Sales fact table
CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY,
    date_id INTEGER,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    sales_amount REAL,
    discount_rate REAL,       -- new column
    payment_method TEXT,      -- new column
    sales_channel TEXT,       -- new column
    FOREIGN KEY (date_id) REFERENCES dates(date_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
