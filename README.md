# How to use
```
python3 -m venv venv
source venv/bin/activate
pip install -r config/pip-requirements.txt
python stock_options.py --input-file example_options.csv
```

The `--input-file` file should describe the various grants being purchased.
Required headers:

| Column Name | Description |
| ----------- | ----------- |
| start | When the grant date started |
| quantity | How many options in the grant |
| strike_price | The price each option can be purchased |
