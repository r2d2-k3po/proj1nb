import pandas as pd
df = pd.read_csv('./data/1. 19년도-과정이수및평가점수.csv', encoding='euc-kr')
print(type(df))
print(df.shape)
print(df.columns)