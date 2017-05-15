from sklearn.metrics import f1_score


class ResultDataTransformer:
    @staticmethod
    def transform_result_data(b_test_labels, prediction):
        f1_weighted = f1_score(b_test_labels, prediction, average='weighted')
        f1_macro = f1_score(b_test_labels, prediction, average='macro')
        f1_micro = f1_score(b_test_labels, prediction, average='micro')

        return [f1_weighted, f1_macro, f1_micro]
