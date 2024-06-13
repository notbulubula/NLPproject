import requests
import json
from typing import Any, List, Dict


def get_dataset_rows(dataset: str, config: str, split: str, num_rows: int) -> List[Dict[str, Any]]:
    """
    Get the first `num_rows` rows from a dataset split.
    
    Args:
        dataset (str): The dataset name.
        config (str): The dataset configuration.
        split (str): The dataset split.
        num_rows (int): The number of rows to extract.
        
    Returns:
        List[Dict[str, Any]]: The extracted rows.
    """
    url = f"https://datasets-server.huggingface.co/rows?dataset={dataset}&config={config}&split={split}&offset=0"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # The rows are under the 'rows' key
        rows = data.get("rows", [])
        # Extract the first `num_rows` rows
        return rows[:num_rows]
    else:
        response.raise_for_status()
        return []


def save_to_json_file(data: List[Dict[str, Any]], file_path: str) -> None:
    """
    Save data to a JSON file.

    Args:
        data (List[Dict[str, Any]]): The data to save.
        file_path (str): The file path to save the data to.
    """
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=2)


if __name__ == "__main__":
    dataset = "lucadiliello/STORIES"
    config = "default"
    split = "train"
    num_rows = 100
    file_path = "../data/data.json"

    rows = get_dataset_rows(dataset, config, split, num_rows)

    # Save rows to JSON file
    save_to_json_file(rows, file_path)

    print(f"Saved {len(rows)} rows to {file_path}")
