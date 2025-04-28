
-- Crear base de datos para campañas publicitarias
CREATE DATABASE IF NOT EXISTS ad_campaign_db;

USE ad_campaign_db;

CREATE TABLE ad_campaigns (
    campaign_id INT PRIMARY KEY,
    campaign_name VARCHAR(255),
    start_date DATE,
    end_date DATE,
    impressions INT,
    clicks INT,
    spend DECIMAL(10,2),
    revenue DECIMAL(10,2)
);
