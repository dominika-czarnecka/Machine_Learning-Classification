from Backend.SVM import info_text

class ParametersParser:
    @staticmethod
    def assert_args(args):
        if 'c'      not in args or args['c'] < 0.0 \
        or 'kernel' not in args or args['kernel'] not in ['rbf', 'sigmoid', 'linear', 'poly'] \
        or 'degree' not in args or args['degree'] < 0 \
        or 'gamma'  not in args or (args['gamma'] !='auto' and args['gamma'] < 0.0) \
        or 'coef0'  not in args or args['coef0'] < 0.0 \
        or 'shrinking'not in args or args['shrinking'] not in [True, False] \
        or 'tol'    not in args or args['tol'] < 0 \
        or 'max_iter' not in args or args['max_iter'] < -1:
            raise ValueError(info_text.svm_help)
        for arg in args:
            if arg not in ['c', 'kernel', 'degree', 'gamma', 'coef0', 'shrinking', 'tol', 'max_iter']:
                raise ValueError(info_text.svm_help)
