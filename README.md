# Quora Trend Analyzer
=================

## About

This repository is my response to the open-ended challenge for a Trend Analyzer by Quora. The goal is to design and implement a trend analysis engine. This engine should be able to take as input a table of raw data and present an interface for trend analysis. You are free to design this interface and choose the data analysis features that you wish to support. It is important that the engine only exposes to the user data that does not have any personal identifiers and protects sensitive attributes from being revealed. The full listing is available here: http://www.quora.com/challenges#trend_analyzer

This project is written in Python 2.7.6 and uses NumPy 1.8 and SciPy 0.13.2

## Getting Started

To get going, just clone this repository. To run just call:

```
python main.py <path to your csv file>
```

The program will begin by reading the entire .csv file and then ask a prompt on whether to include each column in the analysis or not. To assist with the prompts, some information will be given regarding what is stored in each column. After the initial processing is done, a list of possible commands will be listed. Each of these commands is a unique analysis module, which enables you to explore the data in different ways.

## The Modules

### SortR

The goal of SortR is to help someone find new trends in data. This is done by sorting the data according to certain columns. A prompt will ask which column you wish to sort and will list all of the options. Consecutive prompts will ask if you would like to do another sort within each sorted section such that.

For example, if the data has the columns City, State, and Action, sorting by State -> City -> Action would sort all data alphabetically by State name and then sort each entry by City. All entries with the same State and City would be further sorted by Action.

### Exporting

To get a .csv file of all processes run on the data, simply run the export command. In the exports/ folder, a new directory will appear named by the timestamp of generation. In this directory there will be a .csv file for every analysis run. This feature makes it easy to use results from this data engine in other visualization softwares.

## The Data

In data/csv/ you will find a few .csv files that were provided by Quora. The first two lines of these files indicate the titles for each column as well as the type of data that is in each column. Each remaining line is a unique row of data. Please refer to these examples and their website if you wish to use this engine for any other sources of data. The engine can accommodate virtually any variety of data as long as it follows the given format.

## Privacy

The organization of parse makes it easy to selectively cleanse the data from sensitive information. When assessing each column, parse indicates whether the data is sensitive and asks if it should be included in analysis.

## Additions

If you would like to add your own analysis module to this project, just add an elif statement for it and add a command for it in the set in main.py
