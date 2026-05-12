python<br>import pandas as pd<br><br>def parse_budget_excel(file_path):<br> df = pd.read_excel(file_path)<br> return {'rows': len(df), 'columns': list(df.columns)}<br>
