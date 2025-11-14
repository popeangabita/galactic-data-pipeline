# PS1 script to run the ETL
python src/setup_db.py

Write-Output "Extracting exoplanets..."
python src/extract_exoplanets.py

Write-Output "Extracting near-Earth objects..."
python src/extract_neo.py

Write-Output "Extracting HYG stars..."
python src/extract_hyg.py

Write-Output "Transforming data..."
python src/transform_pandas.py

Write-Output "Pipeline finished successfully!"
