to train a model we have choose a model acc to work::

cross validation :: 
- instead of training the model once and evaluting on a holdout set,k-fold cross-validation split the training data into k flods (typically 10), trains the model on k-1 folds and validatir it in the remaining fold.This process repeat k times.

We'll Use cross_val_score from sklearn.model_selection

90-10 recursively

data overfiting vyayla nko mhunun 