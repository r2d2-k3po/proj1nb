import pandas as pd
df = pd.read_csv('./data/1. 19년도-과정이수및평가점수.csv', encoding='euc-kr')
print(type(df))
print(df.shape)
print(df.columns)
print(df.head())
print(df.info)

from numpy import NaN, NAN, nan
df['D과목점수'] = NaN

print(df.count())

dept = df.학과.unique()
print(type(dept))
print(dept.size)

grouped_df = df.groupby(['학과'])
print(grouped_df['학생구분'].nunique())

grouped_df = df.groupby(['학과', '학생구분'])
print(grouped_df['학년'].count())

grouped_df.mean()

print(df.loc[df.A과목이수 == 1].shape)
print(df.loc[df.A과목이수 == 2].shape)

print(df.loc[df.B과목이수 == 1].shape)
print(df.loc[df.B과목이수 == 2].shape)

print(df['A과목점수'].info)


# //////////////////////////////////////////////////////////
df15 = pd.read_excel('./data/2. 15-19년전체집계.xlsx')
print(type(df15))
print(df15.shape)
print(df15.columns)
print(df15.head())
print(df15.info)

print(df15.count())


y2019 = df15.loc[(df15.연도 == 2019), :]
y2019 = df15.loc[(df15.A과목 == 0.000), :]
print(y2019.head())
