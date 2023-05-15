# Welcome to My Mobapp Studio
## Task
We analysed mobile Apps in Google play Store dataset sourced from Kaggle 

## Description
We used the following functions to carry out the analysis on the Google Play dataset:

def load_dataset(csvfile): which loads the dataset as csvfile

def print_summarize_dataset(dataset): which summarized the dimension/size of the data as 10841 rows and 13 columns 
                                    showing the names, non-null count and datatype of each column. 

def convert_size(size_str): which converted from kilobytes(K) to float in Megabytes(M)

def clean_dataset(dataset): which cleaned the dataset  by removing missing values, duplicate values of the App column, 
                            converting data types, and standardizing values in the 'Size', 'Installs', and 'Price' columns.
                            The resulting cleaned dataset was displayed with the first 10 rows.

def print_histograms(dataset): which displayed the visualizations(distribution of the numerical columns in the dataset) using print_histograms
                                where we compared 'Ratings', 'Review', 'Size', 'Installs' and 'Price'

def compute_correlations_matrix(dataset): which compared the coefficients of correlation between different features (or attributes) naming 
                                        'Ratings', 'Review', 'Size', 'Installs' and 'Price' displaying a strong positive correlation between 'Reviews' and 'installs' 

def print_scatter_matrix(dataset): which indicated how the changes in one feature affected the other explaining the pair-relationship of numerical columns

Other analysis were done showing the relative distribution of app ratings, the relationship 
between app installs and reviews, and the popularity of certain paid apps and genres namely;

Top 10 Most Popular Paid Apps in Family Category; 

Top 10 most popular genres according to the number of installations from paid family;

The mean price per category;

Most expensive apps per category;

Number of Installs per Content Rating;

All these information can also be found on our blog- https://medium.com/@marthaakinlolu/40c606c60a5d

## Installation
This project required some installations and the googleplaystore.csv was uploaded from the Kaggle dataset.

These installations include:

!pip install seaborn

!pip install plotly

## Usage
The code was run on a jupyter notebook whose http address can be gotten by running this in the terminal:

jupyter notebook --no-browser

Then the jupyter http address can be followed and the password: 'qwasar' inputed

### The Core Team
Martha Akinlolu

Bukola Veronica Oladele

<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px'></span>
