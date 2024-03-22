from pathlib import Path
from paths import ROOT_PATH

from datetime import datetime

from ressources import Ressources

from pandas import DataFrame, read_csv


def save_csv(frame: DataFrame, ressource: Ressources, desc: str = "") -> None:
    if desc:
        desc = f"{desc}_"

    ressource_folder = ROOT_PATH / Path(ressource)

    if not ressource_folder.is_dir():
        ressource_folder.mkdir()

    file_version = 1
    csv_files: list[str] = [path.name for path in ressource_folder.glob("*.csv")]

    if csv_files:
        file_version = len(csv_files) + 1

    file_name = Path(f"{datetime.utcnow().strftime("%y%m%d-%H%M")}_{ressource}_{desc}{file_version}.csv")
    file_path = ressource / file_name
    
    frame.to_csv(file_path)

def load_csv(ressource: Ressources, version: int = -1) -> DataFrame:

    ressource_folder = ROOT_PATH / Path("ressource")

    if not ressource_folder.is_dir():
        raise FileNotFoundError(f"Folder for ressource {ressource} does not exist")
    
    csv_files = list(ressource_folder.glob("*.csv"))
    
    assert version != 0
    if len(csv_files) == 0:
        raise FileNotFoundError(f"Couldn't find any files for ressource {ressource}")
    elif version > 0 and len(csv_files) > version:
        raise FileNotFoundError(f"Version {version} does not exist for ressource {ressource}")

    if version < 0:
        file_path = csv_files[-1]
    else:
        file_path = csv_files[version - 1]

    df = load_csv(file_path)

    return df
        


    df = read_csv()


    