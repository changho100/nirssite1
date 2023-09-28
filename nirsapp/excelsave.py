import pandas as pd

dfs = pd.read_table('sample.html')
# pd.read_html

df = dfs[0]

df.to_excel('output.xlsx', index=False)  # 'output.xlsx'는 저장할 Excel 파일의 이름입니다.
