def get_summary_stats(dataframe):
    """
    Return summary statistics for numeric columns
    in a pandas DataFrame.
    """
    return dataframe.describe()