# Data Dictionary

## Sales Table

| Column | Data Type | Description |
|---------|-----------|-------------|
| Order_ID | Integer | Unique order identifier |
| Order_Date | Date | Date of order |
| Customer_ID | Integer | Customer reference |
| Product_ID | Integer | Product reference |
| Salesperson_ID | Integer | Sales representative |
| Quantity | Integer | Units sold |
| Unit_Price | Decimal | Selling price per unit |
| Discount | Decimal | Discount percentage |
| Revenue | Decimal | Total sales amount |
| Cost | Decimal | Total product cost |
| Profit | Decimal | Revenue - Cost |
| Payment_Mode | Text | UPI, Card, Cash, EMI, Net Banking |
| State | Text | State where the sale occurred |
| City | Text | City where the sale occurred |

---

## Customers Table

| Column | Data Type | Description |
|---------|-----------|-------------|
| Customer_ID | Integer | Unique customer identifier |
| Customer_Name | Text | Full customer name |
| Gender | Text | Male/Female |
| Age | Integer | Customer age |
| Segment | Text | Retail, Corporate, SME, Government |
| State | Text | Customer state |
| City | Text | Customer city |
| Join_Date | Date | Customer registration date |

---

## Products Table

| Column | Data Type | Description |
|---------|-----------|-------------|
| Product_ID | Integer | Unique product identifier |
| Product_Name | Text | Product name |
| Brand | Text | Brand name |
| Category | Text | Product category |
| Sub_Category | Text | Product sub-category |
| Cost_Price | Decimal | Cost price |
| Selling_Price | Decimal | Selling price |

---

## Salespersons Table

| Column | Data Type | Description |
|---------|-----------|-------------|
| Salesperson_ID | Integer | Employee ID |
| Employee_Name | Text | Salesperson name |
| Region | Text | Sales region |
| Manager | Text | Reporting manager |
| Target | Decimal | Monthly sales target |

---

## Relationships

| Parent Table | Child Table | Key |
|--------------|-------------|-----|
| Customers | Sales | Customer_ID |
| Products | Sales | Product_ID |
| Salespersons | Sales | Salesperson_ID |

---

## Dataset Summary

| Table | Estimated Records |
|--------|------------------:|
| Sales | 100,000 |
| Customers | 10,000 |
| Products | 500 |
| Salespersons | 30 |