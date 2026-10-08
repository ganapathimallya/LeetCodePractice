import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    filter_df=(products['low_fats']=='Y') & (products['recyclable']=='Y')
    return products.loc[filter_df,['product_id']]