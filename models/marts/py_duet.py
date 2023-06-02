import pandas as pd


def model(dbt, session):
    dbt.config(enabled=True, materialized="table", packages=["pandas==1.5.2"])

    print('hihi============')

    data = [['tom', 10], ['nick', 15], ['juli', 14]]
    
    # Create the pandas DataFrame
    df = pd.DataFrame(data, columns=['Name', 'Age'])

    return df
