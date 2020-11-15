# importing seaborn library.
import seaborn as sb

# getting list of all available data sets in seaborn library.
a = sb.get_dataset_names()
# printing list of all data sets
print(a)

# loading mpg dataset.
b = sb.load_dataset('mpg')
# printing dataset
print(b)