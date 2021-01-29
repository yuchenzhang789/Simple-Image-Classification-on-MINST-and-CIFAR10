# Simple-Image-Classification-on-MINST-and-CIFAR10
This was a small project on CS189 at Berkeley. The code was able to reach 0.989 accuracy on MNIST dataset and 0.58 accuracy on CIFAR10 dataset with simple self-written parameter tuning code with SVM on Sklearn. The class rank was 8 and 14 respectively in size 400.
The file "question_code.ipynb" contains all the code needed to replicate my work. The code can be opened by jupiter notebook and one could run through all blocks one by one. 
The mnist kaggle score should be replicated using block "[21]" on appendix with "pixels_per_cell=(4,4)" on line2 of mnist_hogging, then calling "q5_kaggle('mnist', 'rbf')"
The cifar kaggle score should be replicated using block "[21]" on appendix with "pixels_per_cell=(4,4)" on line2 of cifar_hogging, then calling "q5_kaggle('cifar', 'rbf')"
