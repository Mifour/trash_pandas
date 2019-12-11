import pandas as pd
import numpy as np
from bashplotlib.scatterplot import plot_scatter
from bashplotlib.histogram import plot_hist
from scipy.stats import spearmanr

def spearman_correlation(df):
    """
    print the Spearman's correlation matrix for each pair of the dataframe columns
    """
    print("\nSpearman's correlation matrix\n")
    matrix = np.around(spearmanr(df.dropna())[0])
    l = max([len(col) for col in df])

    print( " "*(l+4) +"  ".join([str(n) for n in range(min(10,matrix.shape[0]))])
         +" "+" ".join([str(n) for n in range(10,matrix.shape[0])])
         )
    for line in range(matrix.shape[0]):
        print(
            str(line)+("  "if line < 10 else " ")+ (" "*l +df.columns[line])[-l:]+ " " +"  ".join(
                ['-' if c < -0.5 else '+' if c > 0.5 else '0' for c in matrix[line,:]]
            ) + "\n"
        )

def explore_col(df, col, histo=True, nb_uniques=10):
    print(f"{'-'*(len(col)+4)}")
    print(f"| {col} |")
    print(f"{'-'*(len(col)+4)}")
    print(f"type: {type(df[col][0])}")
    print(df[col][:10])
    print(f"\nmin: {df[col].min()}")
    print(f"max: {df[col].max()}")
    if (isinstance(df[col][0], int) 
        or isinstance(df[col][0], float)
        or np.issubdtype(type(df[col][0]), np.integer)
        or np.issubdtype(type(df[col][0]), np.floating)
       ):
        print(f"mean: {np.mean(df[col])}")
        print("\n---------------------------------")
        print("|  25%  |  50%  |  75%  |  std  |")
        print("---------------------------------")
        print("|" + "|".join([(str(val)+'       ')[:7] for val in df[col].quantile([.25, .5, .75])])
                + "|" + (str(df[col].std())+'       ')[:7] + "|"
        )
        print("---------------------------------")
        if histo:
            print("histogram:")
            if isinstance(df[col][0], bool):
                plot_hist(
                    df[col].apply(lambda row: 0 if row is False else 1 if row is True else -1),
                    bincount = 30,
                    pch = '.',
                    xlab=True
                )
            else:
                plot_hist(df[col],bincount = 30, pch = '.', xlab=True)

    uniques = sorted(df[col].unique())
    print(f"contains {len(uniques)} different values")
          
    if len(uniques) < nb_uniques:
          print("uniques values: ")
          columns = '| '+' | '.join([str(elem) for elem in uniques])+' |'
          print('-' * len(columns))
          print(columns)
          print('-' * len(columns))
          numbers = []
          print(
              '| '+'%| '.join([(str(
                  df[col].where(
                      df[col]==elem).dropna().count() /df[col].shape[0] *100
                  )+ ' '*len(str(elem)) )[:len(str(elem))] for elem in uniques
            ]) + '%|'
          )
          print('-' * len(columns))
          
    print(f"contains {df[col].shape[0]- df[col].dropna().shape[0]} NaN values\n")

def gen_wrapper(df, histo=True, nb_uniques=10):
    """
    wrapper function in order to yield over df's columns
    usage:
    df = pd.read_csv()
    gen = trash_pandas.explore(df, generator=True)
    next(gen)
    ...

    """
    for col in df.columns:
        yield explore_col(df[[col]], col, histo=histo, nb_uniques=nb_uniques)

def explore(df, histo=True, correlation=True, nb_uniques=10, generator=False):
    """
    WIP: please report feedbacks to Thomas Dufour (Mifour)

    A tool to help discovering dataset and the underlying biais using only print function.
    usage:
        from TrashPandas import explore
        explore(pandas.DataFrame)
    parameters:
        df: pandas.DataFrame.
        histo: bool, OPTIONNAL (default=True), display histogram for every column when possible.
        correlation: bool, OPTIONNAL (default=True), compute the spearman's correlation matrix between columns.
            only avalaible without generator parameter.
        nb_uniques: int, OPTIONNAL (default=10), the number of maximun unique value to compute distribution.
        generator: bool, OPTIONNAL (default=False), yield column by columb if True, all at once if False.
    """
    print(df.columns)
    print(df.shape)
    
    if generator:
        return gen_wrapper(df, histo=histo, nb_uniques=nb_uniques)
    else:
        for col in df.columns:
            explore_col(df[[col]], col, histo=histo, nb_uniques=nb_uniques)
        if correlation:
            spearman_correlation(df)
