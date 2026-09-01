import argparse
import logging

from src.ingestion import (
    load_daily_data,
    load_monthly_data
)

from src.cleaning import (
    clean_daily_data,
    clean_monthly_data
)

from src.features import (
    build_features
)


logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s "
        "%(levelname)s "
        "%(message)s"
    )
)


def run_features():

    logging.info(
        "Loading raw data"
    )

    daily = load_daily_data()

    monthly, beta = (
        load_monthly_data()
    )

    logging.info(
        "Cleaning data"
    )

    daily = (
        clean_daily_data(
            daily
        )
    )

    monthly = (
        clean_monthly_data(
            monthly,
            beta
        )
    )

    logging.info(
        "Building features"
    )

    data = build_features(
        daily,
        monthly
    )

    path = (
        "data/processed/"
        "factor_data.csv"
    )

    data.to_csv(
        path,
        index=False
    )

    logging.info(
        "Saved %s",
        path
    )


if __name__ == "__main__":

    parser = (
        argparse.ArgumentParser()
    )

    parser.add_argument(
        "--step",
        required=True
    )

    args = (
        parser.parse_args()
    )

    if (
        args.step
        == "features"
    ):

        run_features()