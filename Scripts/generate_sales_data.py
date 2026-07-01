import random
import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta

random.seed(42)

# ----------------------------------------------------
# Paths
# ----------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[1]

MASTER = BASE_DIR / "Data" / "Master"
RAW = BASE_DIR / "Data" / "Raw"

customers = pd.read_csv(MASTER / "customers.csv")
products = pd.read_csv(MASTER / "products.csv")
salespersons = pd.read_csv(MASTER / "salespersons.csv")

NUM_ORDERS = 100000

# ----------------------------------------------------
# Weights
# ----------------------------------------------------

payment_modes = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash",
    "EMI",
    "Net Banking"
]

payment_weights = [45,25,15,10,3,2]

channels = [
    "Retail Store",
    "Online"
]

channel_weights = [70,30]

statuses = [
    "Delivered",
    "Cancelled",
    "Returned"
]

status_weights = [94,3,3]

start = datetime(2023,1,1)
end = datetime(2024,12,31)

days = (end-start).days

sales = []

for i in range(NUM_ORDERS):

    customer = customers.sample().iloc[0]

    product = products.sample().iloc[0]

    salesperson = salespersons.sample().iloc[0]

    order_date = start + timedelta(days=random.randint(0,days))

    month = order_date.month

    category = product["Category"]

    subcategory = product["Sub_Category"]

    # -----------------------------
    # Quantity
    # -----------------------------

    if category == "Accessories":
        qty = random.randint(2,8)

    elif category == "Audio":
        qty = random.randint(1,5)

    else:
        qty = random.randint(1,2)

    # Diwali Boost

    if month in [10,11]:

        if category in ["Mobiles","Televisions","Accessories"]:

            qty += random.randint(1,2)

    # Summer

    if month in [4,5]:

        if category=="Appliances":

            qty += 1

    # -----------------------------
    # Discount
    # -----------------------------

    if subcategory=="iPhones":

        discount=random.choice([0,5])

    elif category=="Accessories":

        discount=random.choice([10,15,20,25])

    elif category=="Televisions":

        discount=random.choice([10,15,20])

    else:

        discount=random.choice([0,5,10,15])

    sales.append({

        "Order_ID":f"ORD{i+1:06d}",

        "Order_Date":order_date.strftime("%Y-%m-%d"),

        "Customer_ID":customer["Customer_ID"],

        "Product_ID":product["Product_ID"],

        "Salesperson_ID":salesperson["Salesperson_ID"],

        "Quantity":qty,

        "Discount_Percentage":discount,

        "Payment_Mode":random.choices(payment_modes,weights=payment_weights,k=1)[0],

        "Sales_Channel":random.choices(channels,weights=channel_weights,k=1)[0],

        "Order_Status":random.choices(statuses,weights=status_weights,k=1)[0]

    })

sales_df=pd.DataFrame(sales)

RAW.mkdir(exist_ok=True)

sales_df.to_csv(RAW/"sales.csv",index=False)

print("Done")
print(sales_df.head())