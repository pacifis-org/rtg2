import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi


def main():
    # We assume that the kaggle.json file is in the ~/.kaggle directory
    api = KaggleApi()
    api.authenticate()

    download_path = os.path.dirname(
        os.path.realpath(__file__)
    )  # directory that this script is in

    api.competition_download_files("titanic", path=download_path)

    with zipfile.ZipFile(os.path.join(download_path, "titanic.zip"), "r") as f:
        f.extractall(download_path)

    os.remove(os.path.join(download_path, "titanic.zip"))


if __name__ == "__main__":
    main()
