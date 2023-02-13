import numpy as np
import pandas as pd

# Extract specified rows from the dataset. It will be used to create a number of smaller DataFrames withdrawn from the original set.
def extract_rows(df, row_start, row_end, index_to_drop=None):
    new_df = df.iloc[row_start:row_end]
    if index_to_drop != None:
        new_df = new_df.drop(index_to_drop)
    return new_df.reset_index(drop=True)


# Turn string values to NaNs and change all data types to float. As soon as all data in three of five original tables are numeric, but the values are read as objects for some reason, this function turns every numeric to float and strings to NaN.
def change_dtypes(df):
    for col in df.columns:
        if col == 'year':
            df[col] = df[col].apply(lambda x: str(x)[0:4])
        df[col] = pd.to_numeric(df[col], errors='coerce')
        
        
# Print the name of the current DataFrame to the title. It would help us to print out some parts of the DataFrame name to the plot title.
def get_df_name(df):
    return [x for x in globals() if globals()[x] is df][0]