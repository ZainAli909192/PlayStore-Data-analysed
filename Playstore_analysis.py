import pandas as pd

path="E:\\All python\\Data Analysis\\Data sets\\googleplaystore.csv"
data = pd.read_csv(path)
# print(data)

# print(data.head(5))
# print(data.tail(5))
# print(data.shape)
# print(data.info())
# print(data.describe(include='all'))
# print(data.columns)

# print(data[data['App'].str.contains('Astrology')]['App'])
# print(data['Rating'].mean())
# print(data['Category'].unique())
# data.groupby('Category')['Rating'].mean()
# data.groupby('Category')['Rating'].mean().max()
# data.groupby('Category')['Rating'].mean().sort_values()
# print(len(data[data['Rating']==5.0]))

# Find average of reviews 
# data['Reviews']=data['Reviews'].replace('3.0M',3.0)
# data['Reviews'].dtype
# data['Reviews']=data['Reviews'].astype('float')
# data['Reviews'].dtype
# data['Reviews'].mean()

# which app has maximum reviews
# data['Reviews'].max()==data['App'] 
# data[data['Reviews'].max()==data['Reviews']]['App']

# display top 5 apps having highest reviews 
# index=data['Reviews'].sort_values(ascending=False).head().index
# print(data.iloc[index]['App'])

# Find average rating of free and paid apps 
# print(data.groupby('Type')['Rating'].mean())
# print(data.groupby('Type')['Rating'].sum())
# print(data.groupby('Type')['Genres'].value_counts())
# print(data.groupby('Type')['Rating'].value_counts())

# print(data['Installs'].dtype)
data['Installs_1']=data['Installs'].str.replace(',','')
data['Installs_1']=data['Installs_1'].str.replace('+','')
# print(data['Installs_1'].head())
# print(data['Installs_1'].astype('int'))
# print(data[data['Installs_1']=='Free'])
data['Installs_1']=data['Installs_1'].str.replace('Free','0')
data['Installs_1']=data['Installs_1'].astype('int')
# print(data['Installs_1'].sort_values(ascending=False))
ind=data['Installs_1'].sort_values(ascending=False).head().index
print(data.iloc[ind]['App'])