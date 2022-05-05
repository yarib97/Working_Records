import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define seaborn color pallete
sns.set(palette='Dark2')

# Importing excel file sheet into pandas data frame
path_file = 'D:\Python_Files\Working_Records\Working Records.xlsx'
wr = pd.read_excel(path_file, sheet_name='Sample')

# Create data frame with only the columns 'Month', 'Type' and 'Amount'
df = pd.DataFrame(wr,columns=['Year','Month','Type','Amount'])

# Making pivot table to get the different type labels 
pivot = pd.pivot_table(df,index=['Year', 'Month', 'Type'],values='Amount',aggfunc=np.sum)

# Converting pivot data frame indexes to list
pivot_list= list(pivot.index)

# Converting pivot data frame index 'Year' to list
year = [i[0] for i in pivot_list]

# Converting pivot data frame index 'Month' to list
month = [i[1] for i in pivot_list]

# Converting pivot data frame index 'Type' to list
type = [i[2] for i in pivot_list]

# Converting pivot data frame column 'Amount' to list
amount = list(pivot['Amount'])

# Create table with pivot table data
table = pd.DataFrame(list(zip(year,month,type,amount)),
columns=['Year','Month','Type','Amount'])

# Creating 2022 table:
table_2022 = table[table['Year']==2022]

# Sorting months chronologically
order_months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dic']
table_2022['Month']=pd.Categorical(table_2022['Month'],categories=order_months,ordered=True)
table_2022.sort_values(by='Month',inplace=True)
set_months = list(dict.fromkeys(table_2022['Month']))

# Creating pie chart
rows = 2
cols = 3
fig, axes = plt.subplots(rows,cols,facecolor='#fff6eb', figsize=(10,6))
fig.delaxes(ax = axes[1,2])

for i,month in enumerate(set_months):
    ax = axes[i//3,i%3]
    month_df = table_2022.loc[table_2022['Month']==month]
    month_amount = list(month_df['Amount'])
    ax.pie(x=month_amount,labels=month_df['Amount'], startangle=45,
    textprops={'fontsize': 9,'fontname':'Century Gothic'},
    wedgeprops={'width':.5,'edgecolor':'#fff6eb'})
    ax.set_title(month,fontsize=14,fontname='Bell MT',fontweight='bold')

# Creating figure title
fig.suptitle("2022 Spending", fontsize=18, fontname='Century Gothic', fontweight='bold')

# Creating legend to show color for each type
legend = plt.legend(set([x for x in table['Type']]))
for text in legend.get_texts():
    plt.setp(text)
plt.show()

# Saving figure
# plt.savefig('2022_spending.jpg')