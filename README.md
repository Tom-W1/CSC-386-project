# CSC-386-project


Topic:
	The idea of our project is to look at the use of depressing words and see if the user gains Karma.
___
Process outline:
Scrape depression subreddits (top three being: depression, help for depression, and forever alone) for most common words used except for the common words as described in class, this or using a premade list such as the one found here:https://myvocabulary.com/word-list/depression-vocabulary/
Find the number of upvotes/ Karma for each post
Compare with the amount of depression language used
___
Libraries:

	Praw

	Pandas

	Date and time
___
Functions :

	Post_to_dictionary:
		Get post info into a dictionary so we can easily manage the data
	Depression_dictionary:
		Build the dictionary of depressing words
	Dictionary_to_pd:
		Takes the dictionary made to a pandas format for further analyst
	Commonality_of_words:
		This is if we decide to build a list of words from scraping that would exclude the
		Common words(and, but, that).
	Word_count:
		Uses a list to analyze a post to see how many depression words are found within
	Get_karma:
		Exactly what the name implies
	Get_author
		Record the author of the post.
___
Data structures:

	Dictionaries:  to hold the post and the values from what we scrape
	PD: used to give a little more structure to dictionaries to be able to analyze
	String: used when looking at the body or title to analyze the post
	List: used to show the post name with the coordinating values in order and ability to sort
them
___
Corpus:

	As stated in the description we will be using a large amount of post from depression
	Subreddits
___
End-use:

	We will be able to show a correlation between how the use of depressing
    words in these subreddits and it karma affects

