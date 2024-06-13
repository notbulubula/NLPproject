import requests
import json


def get_dataset_rows(dataset, config, split, num_rows):
    url = f"https://datasets-server.huggingface.co/rows?dataset={dataset}&config={config}&split={split}&offset=0"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # The rows are under the 'rows' key
        rows = data.get('rows', [])
        # Extract the first `num_rows` rows
        return rows[:num_rows]
    else:
        response.raise_for_status()


def save_to_json_file(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=2)


if __name__ == "__main__":
    dataset = "lucadiliello/STORIES"
    config = "default"
    split = "train"
    num_rows = 100
    file_path = "data/data.json"

    rows = get_dataset_rows(dataset, config, split, num_rows)

    # Save rows to JSON file
    save_to_json_file(rows, file_path)

    print(f"Saved {len(rows)} rows to {file_path}")
