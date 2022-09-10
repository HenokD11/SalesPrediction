CREATE TABLE Sales
(
    id serial NOT NULL primary key,
    store_id NOT NULL,
    sales_date DATE DEFAULT NULL,
    state_holiday TEXT DEFAULT NULL,
);
