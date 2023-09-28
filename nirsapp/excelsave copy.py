# Python을 사용하여 HTML 표를 Excel 파일로 저장하려면 `pandas` 라이브러리를 사용하는 것이 편리합니다. 아래는 간단한 예제입니다:

# 먼저, `pandas` 라이브러리를 설치합니다:

# pip install pandas

'''그런 다음, HTML 표를 DataFrame으로 변환하고 Excel 파일로 내보냅니다:'''

import pandas as pd

# HTML 표를 DataFrame으로 읽어옵니다.
#url = 'https://example.com/sample.html'  # HTML 표의 URL을 지정합니다.
dfs = pd.read_html('sample.html')

# 웹페이지에서 표를 찾은 후, DataFrame을 선택합니다.
# 여러 표가 있다면, 적절한 DataFrame을 선택해야 합니다.
df = dfs[0]

# DataFrame을 Excel 파일로 내보냅니다.
df.to_excel('output.xlsx', index=False)  # 'output.xlsx'는 저장할 Excel 파일의 이름입니다.

'''

이 코드는 웹에서 HTML 표를 읽어와 `pandas` DataFrame으로 변환하고, 그 DataFrame을 Excel 파일로 저장합니다. `read_html` 함수는 웹페이지에서 모든 HTML 표를 찾아서 DataFrame의 리스트로 반환하므로, 필요에 따라 원하는 표를 선택하세요.

또한, 이 코드는 `to_excel` 메서드를 사용하여 DataFrame을 Excel 파일로 내보냅니다. `index=False`를 사용하면 DataFrame의 인덱스를 Excel 파일에 포함시키지 않습니다.

이 코드를 적절하게 수정하여 원하는 웹페이지의 HTML 표를 읽어와 Excel 파일로 저장할 수 있습니다.
'''


# HTML 표를 DataFrame으로 읽어옵니다.
#url = 'https://example.com/sample.html'  # HTML 표의 URL을 지정합니다.
#dfs = pd.read_html(url)
dfs = pd.read_html('sample.html')

# 웹페이지에서 표를 찾은 후, DataFrame을 선택합니다.
# 여러 표가 있다면, 적절한 DataFrame을 선택해야 합니다.
df = dfs[0]

# DataFrame을 Excel 파일로 내보냅니다.
df.to_excel('output.xlsx', index=False)  # 'output.xlsx'는 저장할 Excel 파일의 이름입니다.

