## **SVM Documentation**
 **1. Public methods:**
* train_svm() - method to train classifier on all train documents from corpus reuters. Important to call this method before any other methods. Method can obtain following arguments:
    > - c - float, default 1.0
    > - kernel - ('rbf' or 'linear' or 'poly' or 'sigmoid'), default 'rbf'
    > - degree - int, default 3 (Used only when kernel is 'poly')
    > - gamma - float, default 'auto'
    > - coef0 - float, default 0.0
    > - shrinking - boolean, default True
    > - probability - boolean, default False
    > - tol - float, default 1e-3
    > - cache_size - float, default 200.0
    > - verbose - boolean, default False
    > - max_iter - int, default -1 (which mean unlimited)
    > - decision_function_shape - ('ovo', 'ovr', None), default None
    > - random_state - int, default None
    > **For more information look in official documentation at [sklearn svc documentation](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)**
* test_svm() - method to test before trained classifier. For tests are used all test documents from corpus reuters. Method return an array. If classifier is not trained then return one element array with string 'Classifier is not trained', otherwise return two elements. An array which contains:
    > - **f1_score is a weighted average of the precision and recall. For more information look in offical documentation at [sklearn f1_score documentation](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html)**
    > - f1_score_weighted
    > - f1_score_macro 
    > - f1_score_micro
* classify_single_document() - method to classify one document. Param is document - raw text to classify. If classifier is not trained then return one element array with string 'Classifier is not trained', otherwise method return:
    > - topic - name of the topic to which the text has been assigned