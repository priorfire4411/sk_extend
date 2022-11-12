from sklearn.base import TransformerMixin, BaseEstimator

class MeanCenteredScaler(BaseEstimator, TransformerMixin):
    """
    Update the comments.
    added comment from new branch
    """
    
    def __init__(self, **fit_params):
        # added a comment to make this way better
        super().__init__(**fit_params)
    
    def fit(self, X):
        '''
        Learns column means of x
        
        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Input samples.

        Returns
        -------
        self : self
        '''
        self.means = X.mean(axis = 0)
        return self
        
    def transform(self, X):
        '''
        Learns column means of x
        
        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Input samples.

        Returns
        -------
        X_new : ndarray array of shape (n_samples, n_features_new)
            Transformed array.
        '''
        return X - self.means

    def printer(self):
        print('some function without coverage.')