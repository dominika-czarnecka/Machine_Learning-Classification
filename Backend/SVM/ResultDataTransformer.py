from sklearn.metrics import f1_score


class ResultDataTransformer:
    @staticmethod
    def transform_result_data(b_test_labels, prediction):
        f1_weighted = f1_score(b_test_labels, prediction, average='weighted')
        f1_macro = f1_score(b_test_labels, prediction, average='macro')
        f1_micro = f1_score(b_test_labels, prediction, average='micro')

        return [f1_weighted, f1_macro, f1_micro]

    @staticmethod
    def transform_result_data_select(b_test_labels, prediction, labels, to_test):

        index = {}
        false_positive = {}
        false_negative = {}
        true_positive = {}
        true_negative = {}

        precision = {}
        recall = {}
        f1 = {}

        for label in to_test:
            index[label] = labels.index(label)
            false_positive[label] = 0
            false_negative[label] = 0
            true_positive[label] = 0
            true_negative[label] = 0

        for label in to_test:
            ind = index[label]
            for i in range(len(b_test_labels)):
                if b_test_labels[i][ind] == 0:
                    if prediction[i][ind] == 0:
                        true_negative[label] += 1
                    elif prediction[i][ind] == 1:
                        false_positive[label] += 1
                elif b_test_labels[i][ind] == 1:
                    if prediction[i][ind] == 1:
                        true_positive[label] += 1
                    elif prediction[i][ind] == 0:
                        false_negative[label] += 1

        for label in to_test:
            precision[label] = true_positive[label] / (true_positive[label] + false_positive[label])
            recall[label] = true_positive[label] / (true_positive[label] + false_negative[label])
            f1[label] = (2*precision[label]*recall[label])/(precision[label]+recall[label])

        return 'PRECIS: ' + str(precision) + '\n' +\
            'RECALL: ' + str(recall) + '\n' +\
            'F1 SCO: ' + str(f1)