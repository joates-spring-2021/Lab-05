# Lab-05 - Dictionaries
Now our labs will begin to get a little more interesting. This lab focuses on using dictionaries, but it will include many other elements.  Some will be done for you, but you will be responsible for the majority of the logic.

# Overview
A common element seen on web pages these days are [tag clouds](http://en.wikipedia.org/wiki/Tag_cloud). A tag cloud is a visual representation of frequency of words, where more frequent words are represented in larger font. One can also use colors and placement.

We are going to analyze the 2012 presidential debate transcript and create a Python dictionary that can be used for a tag cloud for each candidate of the words they used, where the frequency of the words indicates the size of the font in the cloud. We will focus only on organizing the data and not dipictingi the tag cloud itself at this time.

# Background
I'll provide a number of elements to help with this task:
- a transcript of the debate
- a list of "stopwords"
- some functions

##Transcript
The transcript is in *debate.txt*. It has a particular format. Each time one of the candidates speaks, that line is marked, e.g ‘PRESIDENT OBAMA:’. Once encountered, all words are attributed to that speaker until another label occurs (sometimes it is a question from the moderator, MR. LEHRER, so you have to ignore those). Take a look at the file.  I will provide the code to read the contents of this file into one big string

##Stopwords
Not all words are worth counting. ‘a’, ‘the’, ‘was’, etc. are just junk. A list of such words is provided as stopWords.txt Each line has a single word. No word in the stop word list should be counted in the tag cloud.



