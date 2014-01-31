# Quora Data Engine
=================

## About

This repository is my response to the open-ended challenge for a Trend Analyzer by Quora. The goal is to design and implement a trend analysis engine. This engine should be able to take as input a table of raw data and present an interface for trend analysis. You are free to design this interface and choose the data analysis features that you wish to support. It is important that the engine only exposes to the user data that does not have any personal identifiers and protects sensitive attributes from being revealed. The full listing is available here: http://www.quora.com/challenges#trend_analyzer

This project is written in Python 2.7.6 and uses NumPy 1.8 and SciPy 0.13.2

## Getting Started

To get going, just clone this repository. To run just call:

```
python main.py <path to your csv file>
```

The program will begin by reading the entire .csv file and then ask a prompt on whether to include each column in the analysis or not. To assist with the prompts, some information will be given regarding what is stored in each column.

## The Data

In data/csv/ you will find a few .csv files that were provided by Quora. The first two lines of these files indicate the titles for each column as well as the type of data that is in each column. Each remaining line is a unique row of data. Please refer to these examples and their website if you wish to use this engine for any other sources of data. The engine can accommodate virtually any variety of data as long as it follows the given format.


