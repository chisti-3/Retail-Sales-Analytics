import random
import pandas as pd
from faker import Faker
from pathlib import Path

fake = Faker("en_IN")
random.seed(42)

# --------------------------------------------------
# OUTPUT PATHS
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[1]

MASTER_DIR = BASE_DIR / "Data" / "Master"

MASTER_DIR.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# CONFIG
# --------------------------------------------------

NUM_CUSTOMERS = 10000
NUM_PRODUCTS = 100
NUM_SALESPERSONS = 20

# --------------------------------------------------
# REGIONS
# --------------------------------------------------

locations = {
    "Karnataka": ("South", ["Bengaluru","Mysuru","Mangaluru"]),
    "Tamil Nadu": ("South", ["Chennai","Coimbatore","Madurai"]),
    "Telangana": ("South", ["Hyderabad","Warangal","Karimnagar"]),
    "Kerala": ("South", ["Kochi","Thiruvananthapuram","Kozhikode"]),
    "Maharashtra": ("West", ["Mumbai","Pune","Nagpur"]),
    "Gujarat": ("West", ["Ahmedabad","Surat","Vadodara"]),
    "Delhi": ("North", ["New Delhi"]),
    "Punjab": ("North", ["Ludhiana","Amritsar"]),
    "West Bengal": ("East", ["Kolkata","Siliguri"]),
    "Madhya Pradesh": ("Central", ["Indore","Bhopal"])
}

segments = [
    "Retail",
    "Corporate",
    "SME",
    "Education",
    "Government"
]

payment_modes = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash",
    "EMI",
    "Net Banking"
]

customers = []

states = list(locations.keys())

for i in range(1, NUM_CUSTOMERS + 1):

    state = random.choice(states)

    region, cities = locations[state]

    city = random.choice(cities)

    customers.append({

        "Customer_ID": f"CUST{i:05d}",

        "Customer_Name": fake.name(),

        "Gender": random.choice(["Male","Female"]),

        "Age": random.randint(18,65),

        "Segment": random.choice(segments),

        "Join_Date": fake.date_between("-5y","today"),

        "City": city,

        "State": state,

        "Region": region

    })

customers_df = pd.DataFrame(customers)

customers_df.to_csv(
    MASTER_DIR / "customers.csv",
    index=False
)

print("Customers Created")

# --------------------------------------------------
# PRODUCT CATALOG
# --------------------------------------------------

products_catalog = {

    "Mobiles":{

        "Android Phones":{
            "brands":["Samsung","OnePlus","Xiaomi","Nothing","Realme"],
            "cost_range":(8000,45000)
        },

        "iPhones":{
            "brands":["Apple"],
            "cost_range":(45000,120000)
        }

    },

    "Laptops":{

        "Business":{
            "brands":["Dell","HP","Lenovo"],
            "cost_range":(35000,90000)
        },

        "Gaming":{
            "brands":["Asus","MSI","Acer"],
            "cost_range":(60000,150000)
        }

    },

    "Televisions":{

        "LED TVs":{
            "brands":["LG","Samsung","Sony"],
            "cost_range":(18000,70000)
        },

        "OLED TVs":{
            "brands":["LG","Sony"],
            "cost_range":(70000,200000)
        }

    },

    "Audio":{

        "Earbuds":{
            "brands":["Boat","Sony","JBL"],
            "cost_range":(800,12000)
        },

        "Bluetooth Speakers":{
            "brands":["Boat","JBL","Sony"],
            "cost_range":(1500,25000)
        }

    },

    "Accessories":{

        "Chargers":{
            "brands":["Boat","Ambrane"],
            "cost_range":(300,2000)
        },

        "Power Banks":{
            "brands":["Mi","Ambrane"],
            "cost_range":(700,4000)
        }

    }

}

products = []

product_counter = 1

for category, subcategories in products_catalog.items():

    for subcategory, details in subcategories.items():

        brands = details["brands"]

        min_cost, max_cost = details["cost_range"]

        for brand in brands:

            for model in range(1,11):

                cost = random.randint(min_cost,max_cost)

                markup = random.uniform(1.12,1.30)

                selling = round(cost*markup,2)

                products.append({

                    "Product_ID":f"PROD{product_counter:04d}",

                    "Product_Name":f"{brand} {subcategory} Model {model}",

                    "Brand":brand,

                    "Category":category,

                    "Sub_Category":subcategory,

                    "Cost_Price":cost,

                    "Selling_Price":selling

                })

                product_counter += 1

products_df = pd.DataFrame(products)

products_df.to_csv(
    MASTER_DIR/"products.csv",
    index=False
)

print(f"{len(products_df)} Products Created")


salespersons=[]

managers=["Rahul Sharma","Priya Nair","Amit Verma"]

regions=["North","South","East","West","Central"]

for i in range(1,NUM_SALESPERSONS+1):

    salespersons.append({

        "Salesperson_ID":f"EMP{i:03d}",

        "Employee_Name":fake.name(),

        "Gender":random.choice(["Male","Female"]),

        "Region":random.choice(regions),

        "Manager":random.choice(managers),

        "Monthly_Target":random.randint(800000,2000000)

    })

salespersons_df=pd.DataFrame(salespersons)

salespersons_df.to_csv(

    MASTER_DIR/"salespersons.csv",

    index=False

)

print("Salespersons Created")

