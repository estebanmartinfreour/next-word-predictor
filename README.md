# Next Word Predictor

## Introduction
The aim of this project is to develop a tiny AI model which can predict the next word giving the previous words in the sentence. 
To do so, we will train our model with 1 or 2 OpenSource novels of a same author. So, the model will be a predictor for the given author and will not be able to predict exactly the next word of everyone. This limit is due tou our incapacities to treat the amout of data to do so.

To run ou project, we choose to work with the novel "Les Misérables" by Victor Hugo. The text we use is a copy of a .txt document that we found on the Project Gutenbergs' website.

## Key step of our project

### Tokeniser

First, we have created a Tokeniser class wich aim to transform the text in an integers list where each integer is the representation of a word of the text. 
In this class, there is two key methods : the .build_tables method which create two dictionnaries, one called word_to_index which link each word to is index integer in the book and one called index_to_word which allows to do the inverse path ; and the .text_to_sequences method which transform a text into an integer list following the index.

### Creation of the data set

