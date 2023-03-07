"""This module contains a few functions for cleaning data from US Census."""

import pandas as pd

def extract_rows(df, row_start, row_end, index_to_drop=None):
    '''
    Extract specified rows from a dataset. 
    It can be used to create a number of smaller DataFrames withdrawn from the original set.

    Parameters:
        df (pandas DataFrame): Original DataFrame
        row_start (int): Index of the first row of a new DataFrame
        row_end (int): Index of the last row of a new DataFrame
        index_to_drop(int, optional): Specify a row to drop from a copy (default: None)

    Returns:
        new_df (pandas DataFrame): A new frame with reset index
    '''
    new_df = df.iloc[row_start:row_end]
    if index_to_drop != None:
        new_df = new_df.drop(index_to_drop)
    return new_df.reset_index(drop=True)


def change_dtypes(df):
    '''Turn string values to NaN and change all data types to float. As a mutable object, DataFrame has its data types transformed directly within a function.'''
    for col in df.columns:
        if col == 'year':
            df[col] = df[col].apply(lambda x: str(x)[0:4])
        df[col] = pd.to_numeric(df[col], errors='coerce')
        
        
def get_df_name(df):
    '''Print the name of the current DataFrame to the title.'''
    return [x for x in globals() if globals()[x] is df][0]
