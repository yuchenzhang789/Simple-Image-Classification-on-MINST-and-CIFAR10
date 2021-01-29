Author Name: Jeffrey Zhang
SID: 3034072916
email: yuchenzhang@berkeley.edu
The file "question_code.ipynb" contains all the code needed to replicate my work. The code can be opened by jupiter notebook and one could run through all blocks one by one. 
The spam kaggle score can be easily replicated by calling "q5_kaggle('spam', 'linear')" after the first block for question 5.
The mnist kaggle score should be replicated using block "[21]" on appendix with "pixels_per_cell=(4,4)" on line2 of mnist_hogging, then calling "q5_kaggle('mnist', 'rbf')"
The cifar kaggle score should be replicated using block "[21]" on appendix with "pixels_per_cell=(4,4)" on line2 of cifar_hogging, then calling "q5_kaggle('cifar', 'rbf')"