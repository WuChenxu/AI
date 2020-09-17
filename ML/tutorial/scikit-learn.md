# link
 [scikit-leran](https://scikit-learn.org/)
# install
```python
conda install scikit-learn
```
# check install status
```python
conda list scikit-learn # to see which scikit-learn version is installed
conda list # to see all packages installed in the active conda environment
python -c "import sklearn; sklearn.show_versions()"
```
# steps
* import dataset
  cross validation(交叉验证):seperate train and test dataset
* train a classifier
* predict label for new flower
* visualize the tree
* 
# Ideal features
* Informative
* Independent
* Simple

# pipeline
there are differents models(classifiers), the interface in high level keeps same.
(fit, predict)
```python
def classify(features):
    # do some logic
    return label
```
the body of the classify function is what we need to write algorithm.
but we don't start from scratch, we start from a model.
model is the prototype defines the rules of the function body.
typically, there are parameters for the model, we need to adjust the parameters for the moel.
one way to think of learning is using training data to adjust the parameters for a model.


# sklearn API
* datasets
* model_selection
* tree
* metrics

[playground](http://playground.tensorflow.org/)
