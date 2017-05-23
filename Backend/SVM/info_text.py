svm_help = \
'c	        >= 0.0 \n\
kernel      \'rbf\', \'sigmoid\', \'linear\', \'poly\' \n\
degree      >= 0 (only poly kernel) \n\
gamma       >= 0.0 or \'auto\' (only rbf, poly, sigmoid kernels) \n\
coef0       >= 0.0 (only poly, sigmoid kernels) \n\
shrinking   bool \n\
tol         >= 0.0 \n\
max_iter    >= -1 (-1 is no limit)'