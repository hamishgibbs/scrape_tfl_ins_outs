import pytest
import pandas as pd

def test_data_has_no_missing_values(fn):
    df = pd.read_csv(fn)
    assert df.isnull().sum().sum() == 0

def test_ins_plus_outs_equal_taps(fn):
    df = pd.read_csv(fn)
    print(df[~(df['ins'] + df['outs'] == df['taps'])])
    assert (df['ins'] + df['outs'] == df['taps']).all()
