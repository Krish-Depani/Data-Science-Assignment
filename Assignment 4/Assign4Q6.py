# importing seaborn library.
import seaborn as sb

# loading dataset mpg.
x = sb.load_dataset('mpg')

# getting dataframe of cars belong to usa.
y = x[x['origin'] == 'usa']
# printing dataframe.
print(y)