# Welcome to My Tu Verras
## Task
The task was to carry out a simple linear regression task with the boston data.

- Challenges:
    the Challenges we experienced here was finding the right figure size for the scatter_matrix for all attributes 
    in the dataset considering the size of the dataset(14 columns). We opted for matplotlib over seaborn which 
    hada more apealing visualization as a consequence of the size of the data.

## Description
To solve the problem we have done the following using functions 
- downloaded the dataset used our defined function `load_data()` to load it into a dataframe.
- used our defined function `print_summary_data(dataset)` to print the  dimension, first 10 rows and the statistical
  summary of the dataset.
- used our function `print_histogram(dataset)` to print the histogram for all attributes of the dataset.
- used our defined function `compute_correlation_matrix(dataset)` to print correlation matrix of each table.
- used our defined function `print_scatter_matrix(dataset)` to plot the scatter matrix which is a visual representation of the 
    of the correlation matrix.
- used our defined functions `boston_fit_model(dataset)` and `boston_predict(estimator, dataset)` to fit the boston_fit_model
    and predict.
- used our defined function `print_model_evaluation(true_data, pred_data)` to print the evaluation of the model.


## Installation
The project does not need any form of Installation as it can be run from your local machine .

## Usage
Usage of these functions are done like how every other function is used. e.g 
- to load data you use `load_data(dataset)`
- to print summary of dataset you will use `print_summary_data(dataset)`
- to print histogram of all attributes you will use `print_histogram(dataset)`
- to print scatter_matrix you will use `print_scatter_matrix(dataset)`
- to fit data model and estimate you wil use `boston_fit_model(dataset)` and `boston_predict(dataset)`.

### The Core Team
Ajekwe Moses Zanzan(ajekwe_m)
Martha Akinlolu (akinlolu_m)

<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px'></span>
