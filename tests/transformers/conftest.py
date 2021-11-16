import pandas as pd
import pytest

@pytest.fixture(scope = 'session')
def get_dataframe():
	return pd.DataFrame({
		'col_a': [0, 50, 100]
		})