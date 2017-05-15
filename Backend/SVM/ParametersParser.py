class ParametersParser:
    @staticmethod
    def parse_params(c, kernel, degree, gamma, coef0, shrinking, probability, tol, cache_size, verbose, max_iter,
                     decision_function_shape, random_state):
        parse_result = True
        parse_result_messages = []

        if c != 1.0:
            result, message = ParametersParser.parse_c_param(c)
            if not result:
                parse_result = False
                parse_result_messages.append(message)

        if kernel != 'rbf':
            result, message = ParametersParser.parse_kernel_param(kernel)
            if not result:
                parse_result = False
                parse_result_messages.append(message)

        if degree != 3:
            result, message = ParametersParser.parse_degree_param(degree)
            if not result:
                parse_result = False
                parse_result_messages.append(message)

        if gamma != 'auto':
            result, message = ParametersParser.parse_gamma_param(gamma)
            if not result:
                parse_result = False
                parse_result_messages.append(message)

        if coef0 != 0.0:
            result, message = ParametersParser.parse_coef0_param(coef0)
            if not result:
                parse_result = False
                parse_result_messages.append(message)

        if not shrinking:
            result, message = ParametersParser.parse_coef0_param(coef0)
            if not result:
                parse_result = False
                parse_result_messages.append(message)

        if probability:
            result, message = ParametersParser.parse_probability_param(probability)
            if not result:
                parse_result = False
                parse_result_messages.append(message)

        if tol != 1e-3:
            result, message = ParametersParser.parse_tol_param(tol)
            if not result:
                parse_result = False
                parse_result_messages.append(message)

        if cache_size != 200.0:
            result, message = ParametersParser.parse_cache_size_param(cache_size)
            if not result:
                parse_result = False
                parse_result_messages.append(message)

        if verbose:
            result, message = ParametersParser.parse_verbose_param(verbose)
            if not result:
                parse_result = False
                parse_result_messages.append(message)

        if max_iter != -1:
            result, message = ParametersParser.parse_max_iter_param(max_iter)
            if not result:
                parse_result = False
                parse_result_messages.append(message)

        if decision_function_shape is not None:
            result, message = ParametersParser.parse_decision_function_shape_param(decision_function_shape)
            if not result:
                parse_result = False
                parse_result_messages.append(message)

        if random_state is not None:
            result, message = ParametersParser.parse_random_state_param(random_state)
            if not result:
                parse_result = False
                parse_result_messages.append(message)

        return parse_result, parse_result_messages

    @staticmethod
    def parse_c_param(c):
        if c < 0.0:
            return False, "C should be greater than or equal 0.0"
        elif not isinstance(c, float):
            return False, "C should be type float."
        return True, any

    @staticmethod
    def parse_kernel_param(kernel):
        if kernel not in ['rbf', 'sigmoid', 'linear', 'poly']:
            return False, "Kernel should be rbf, sigmoid, linear or poly."
        return True, any

    @staticmethod
    def parse_degree_param(degree):
        if degree < 0:
            return False, "Degree should be greater than or equal 0."
        elif not isinstance(degree, int):
            return False, "Degree should be type Integer."
        return True, any

    @staticmethod
    def parse_gamma_param(gamma):
        if gamma < 0.0:
            return False, "Gamma should be greater than or equal 0.0"
        elif not isinstance(gamma, float):
            return False, "Gamma should be type float."
        return True, any

    @staticmethod
    def parse_coef0_param(coef0):
        if coef0 < 0.0:
            return False, "Coef0 should be greater than or equal 0.0"
        elif not isinstance(coef0, float):
            return False, "Coef0 should be type float."
        return True, any

    @staticmethod
    def parse_shrinking_param(shrinking):
        if not isinstance(shrinking, bool):
            return False, "Shrinking should be type boolean."
        return True, any

    @staticmethod
    def parse_probability_param(probability):
        if not isinstance(probability, bool):
            return False, "Probability should be type boolean."
        return True, any

    @staticmethod
    def parse_tol_param(tol):
        if tol < 0.0:
            return False, "Tol should be greater than or equal 0.0"
        elif not isinstance(tol, float):
            return False, "Tol should be float type."
        return True, any

    @staticmethod
    def parse_cache_size_param(cache_size):
        if cache_size < 0.0:
            return False, "Cache_size should be greater than 0.0"
        elif not isinstance(cache_size, float):
            return False, "Cache_size should be float type."
        return True, any

    @staticmethod
    def parse_verbose_param(verbose):
        if not isinstance(verbose, bool):
            return False, "Verbose should be boolean type"
        return True, any

    @staticmethod
    def parse_max_iter_param(max_iter):
        if max_iter < -1:
            return False, "Max_iter should be greater than or equal -1."
        elif not isinstance(max_iter, int):
            return False, "Max_iter should be integer type."
        return True, any

    @staticmethod
    def parse_decision_function_shape_param(decision_function_shape):
        if decision_function_shape not in ['ovo', 'ovr', None]:
            return False, "Decision_function_shape should be equal ovo, ovr or None"
        return True, any

    @staticmethod
    def parse_random_state_param(random_state):
        if random_state < 0:
            return False, "Random_state should be greater than or equal 0."
        elif not isinstance(random_state, int):
            return False, "Random_state should be integer type."
        return True, any
