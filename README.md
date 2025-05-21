# F1 2025 Data Pipeline

This project demonstrates a basic ETL (Extract, Transform, Load) pipeline for Formula 1 race results from the 2025 season. It takes raw race data in CSV format, performs cleaning and transformation using Python and pandas, and outputs a structured JSON file ready for analysis, dashboards, or API consumption.

## Features

- Cleans and standardizes raw F1 race result data
- Adds useful features like:
  - `IsWin`: whether the driver won the race
  - `IsPodium`: whether the driver finished in top 3
- Outputs data as a JSON array (compatible with dashboards, APIs, and ML pipelines)

## Getting Started

### 1. Install Dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
```

```
source venv/bin/activate
```

```
pip install -r requirements.txt
```

### 2. Run the Pipeline

```
python pipeline.py
```

- This will create a f1_cleaned.json file inside cleaned_data/.

### 3. Sample Output

```
[
  {
    "Driver": "Oscar Piastri",
    "Team": "McLaren",
    "Race": "Australian Gp",
    "Points": 25,
    "Position": 1,
    "IsWin": true,
    "IsPodium": true
  },
]
```

## License

MIT License
