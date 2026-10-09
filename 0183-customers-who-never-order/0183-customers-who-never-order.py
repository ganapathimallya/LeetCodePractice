import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    new_df = pd.merge(customers, orders, left_on="id", right_on="customerId", how="left")
    
    no_orders = new_df[new_df['customerId'].isna()]    

    result = no_orders[['name']].rename(columns={'name': 'Customers'})
    return result