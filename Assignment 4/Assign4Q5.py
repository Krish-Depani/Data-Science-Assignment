# importing seaborn library.
import seaborn as sb

# loading mpg dataset.
x = sb.load_dataset('mpg')

# getting country's name of origin.
y = x['origin'].unique()
# printing country's name of origin.
print(y)