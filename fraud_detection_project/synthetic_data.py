import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Function to generate synthetic fraudulent transactions based on given patterns
def generate_fraudulent_data(num_samples=50):
    synthetic_fraud_data = []

    for _ in range(num_samples):
        # Generate a random date within a year range for the transaction
        random_date = datetime.strptime("2023-01-01", "%Y-%m-%d") + timedelta(days=random.randint(0, 364))
        date_str = random_date.strftime("%Y-%m-%d")
        
        # Randomly select details to simulate suspicious activities
        details = random.choice(["UNAUTHORIZED ACCESS", "SUSPICIOUS WITHDRAWAL", "HIGH-RISK TRANSFER"])
        
        # Set Debit, Credit, and Balance with high values to simulate fraudulent behavior
        debit = round(random.uniform(500, 10000), 2) if random.choice([True, False]) else 0.0
        credit = 0.0 if debit > 0 else round(random.uniform(500, 10000), 2)
        balance = round(random.uniform(0, 1000), 2)  # Lower balance after high transactions
        
        # Set high frequency for fraud-prone accounts
        transaction_frequency = random.randint(10, 50)
        
        # Randomize transaction time and hour of the day
        transaction_time = random_date + timedelta(hours=random.randint(0, 23))
        transaction_time_str = transaction_time.strftime("%Y-%m-%d %H:%M:%S")
        hour_of_day = transaction_time.hour
        
        # Choose from fraud-prone locations
        location = random.choice(["Offshore", "International", "Unknown Location", "Unusual ATM"])
        
        # Fraud-prone transaction types
        transaction_type = random.choice(["Card Payment", "Wire Transfer", "Online Purchase", "Money Transfer"])
        
        # Fraudulent flag
        fraudulent = 1
        
        # Append generated row to the list
        synthetic_fraud_data.append([date_str, details, debit, credit, balance, transaction_frequency, 
                                     transaction_time_str, hour_of_day, location, transaction_type, fraudulent])

    # Convert list to DataFrame
    synthetic_fraud_df = pd.DataFrame(synthetic_fraud_data, columns=[
        "Date", "Details", "Debit", "Credit", "Balance", "Transaction_Frequency", 
        "Transaction_Time", "Hour_of_Day", "Location", "Transaction_Type", "Fraudulent"
    ])
    
    return synthetic_fraud_df

# Generate 100 synthetic fraudulent samples
synthetic_fraud_df = generate_fraudulent_data(100)

# Display the first few rows of the generated fraudulent data
synthetic_fraud_df.head()
