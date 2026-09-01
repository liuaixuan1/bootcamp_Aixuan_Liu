import pandas as pd

from src.config import RAW_DIR


def load_daily_data():

    files = [
        "RESSET_DRESSTK_2001_2010_1.xls",
        "RESSET_DRESSTK_2011_2015_1.xls",
        "RESSET_DRESSTK_2016_2020_1.xls",
        "RESSET_DRESSTK_2021__1.xls",
    ]

    frames = []

    for file in files:

        df = pd.read_excel(
            RAW_DIR / file,
            usecols=[2, 4, 6]
        )

        df.columns = [
            "date",
            "close",
            "day_r"
        ]

        frames.append(df)

    data = pd.concat(
        frames,
        ignore_index=True
    )

    return data


def load_monthly_data():

    monthly = pd.read_excel(
        RAW_DIR / "RESSET_MRESSTK_1.xls",
        usecols=[2,3,4,5,6,7,8,9,10]
    )

    monthly.columns = [
        "date",
        "Amount",
        "MTTR",
        "M_r",
        "M_rf",
        "PE",
        "EPS",
        "ROE",
        "IPS"
    ]

    beta = pd.read_excel(
        RAW_DIR /
        "RESSET_SMONRETBETA_BFDT24_1.xls",
        usecols=[2,3]
    )

    beta.columns = [
        "date",
        "Beta"
    ]

    return monthly, beta