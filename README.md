# trash_pandas
## analytic tool for pandas dataframe exploration

Trahs_pandas is an analytic tool designed for Pandas DataFrame exploration.  

It deliver fast statistical insights about the data of every column such as type, NaN values, unique values, distribution, mean, median, quartiles, correlations... and render with graphs using only print statements, making it suitable for both notebook and shell usage.  

It is intended to replace info() and describe().  

### usage
```python
from trash_pandas import explore

df = pandas.read_csv('file.csv')

explore(df)

```
----
### yield option  
It is possible to get a generator that display the result one column at a time. 

```python
from trash_pandas import explore

df = pandas.read_csv('file.csv')

gen = explore(df, generator=True)
next(gen)
...

```
----

I developed it initially for my own usage.  
Mifour.