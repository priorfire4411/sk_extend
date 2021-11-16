from sk_extend.transformers.mean_center import MeanCenteredScaler
import pandas as pd

def test_mean_centered_scaler(get_dataframe):
	scaler = MeanCenteredScaler()
	new_df = scaler.fit_transform(get_dataframe)
	expected = pd.DataFrame({
		'col_a': [-50.0, 0.0, 50.0]
		})
	assert new_df.equals(expected)