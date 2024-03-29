# Soccer Intelligence - Knowledge Graph Approach
by Achin Gupta and Patavee Meemeng

## Introduction

The business intelligence is very prevalent these days. Many technologies can help make better
business decision. However, the soccer domain is quite conservative. They do not exploit much
technology. Instead, they rely a lot on human work. Below shows some example of the
questions that are normally asked in the soccer management team;

- Arsenal conceded a lot of goals and looking for a new defender. What are the
candidates?
- What is the media, commentator’s opinion on Ronaldo?
- Manchester United has just sold a forwarder. What is the best replacement?

This project ‘soccer intelligence’ aims to solve this problem. With knowledge graph, we can
integrate data from all many sources, build semantic relation between those, and provide much
more insight than that human can do. The project shall provide the following features;

- evaluate the performance of the player
- retrieve all the news, twitters related to the player
- evaluate the correlation between players
- pickup the candidate player with the specific query

The soccer club can benefit a lot from this project. It will help them make better decision, buying
and selling their player more efficiently, resulting in better strategy to win the title.

## Project Overview

This project can be organized into the following parts;

### Data Collection
This part will cover crawler (Python Scrapy) and Wrapper (Python BeautifulSoup)

### Information Extraction
This part will include Named Entity Recognition (Python CRFsuite) and relation extraction 

### Ontology-Based Semantic Modeling 
This part will include ontologies we use, and how to map the data to the ontologies using Karma.

### Graph Analytics
This part will include graph analytics using SPARQL and GraphDB.

### GUI
This part will include JAVA user interface using NetBeans.

