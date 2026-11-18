import csv
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.request import urlopen

url = "https://jse.amstat.org/v19n3/decock/AmesHousing.txt"
data_dir = Path(__file__).resolve().parents[1] / "data"
raw_path = data_dir / "raw" / "AmesHousing.txt"
csv_path = data_dir / "processed" / "AmesHousing.csv"

with urlopen(url, timeout=30) as response:
    raw_bytes = response.read()

source = StringIO(raw_bytes.decode("utf-8-sig"), newline="")
rows = list(csv.reader(source, delimiter="\t"))

if (
    len(rows) != 2931
    or "SalePrice" not in rows[0]
    or any(len(row) != 82 for row in rows)
):
    raise ValueError("Expected Ames Housing data with 2,930 rows and 82 columns.")

raw_path.parent.mkdir(parents=True, exist_ok=True)
raw_path.write_bytes(raw_bytes)

csv_path.parent.mkdir(parents=True, exist_ok=True)
with TemporaryDirectory(dir=csv_path.parent) as temp_dir:
    temp_path = Path(temp_dir) / csv_path.name
    with temp_path.open("w", encoding="utf-8", newline="") as output:
        csv.writer(output).writerows(rows)
    temp_path.replace(csv_path)

print(f"Saved original download to {raw_path}")
print(f"Saved {len(rows) - 1} rows and {len(rows[0])} columns to {csv_path}")