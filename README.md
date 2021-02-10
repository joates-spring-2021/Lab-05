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

## Transcript
The transcript is in *debate.txt*. It has a particular format. Each time one of the candidates speaks, that line is marked, e.g ‘PRESIDENT OBAMA:’. Once encountered, all words are attributed to that speaker until another label occurs (sometimes it is a question from the moderator, MR. LEHRER, so you have to ignore those). Take a look at the file.  I will provide the code to read the contents of this file into one big string.

## Stopwords
Not all words are worth counting. ‘a’, ‘the’, ‘was’, etc. are just junk. A list of such words is provided as stopWords.txt. No word in the stop word list should be counted in the tag cloud. I will provide the code to read the contents of this file into one big string. Some problems arise because our program cannot tell the difference between ‘american’ and ‘americans’. This is called a "stemming" problem. There are ways to address this issue, but it is not required for this assignment. 

# Requirements
Using the contents of the debate file and the stop words, your code **shall** create two dictionaries. One dictionary will be for Senator Romney, and the other for President Obama.  The keys for each dictionary **shall** be the words spoken by that candidate, and the values **shall** be the number of times those words were used.  The dictionaries **shall** exclude all words that are in the stop words list.

Your code **shall** print to the screen the 40 most frequently used non-stopwords and their counts.  See the example output below for the exact formatting.

A function shell will be provided for you, _numWordsSpoken(candidate, word)_.  Your code **shall** provide a return value of the number of times the given word was spoken by the given candidate. Comments in the code will help you with what to do.

# Assignment Notes: 
There are a couple of problems here. Think about each one before you start to program. 
 
1. Parsing the debate string. You have to separate the lines according to who said them: Obama, Romney, etc. Use the transcript format described above to help you with this. Remember, once you see one of the speakers’ tags (‘MR ROMNEY:’) all lines/words belong to that speaker until you see another speaker’s tag.

2. Once you have the words separated, you must remove all stop words (using the provided stopWords string. You can do this while you are collecting the words as well.  Also, remember to remove punctuation from words, just because a word comes at the end of a sentence and has a period at the end of it doesn’t make it a different word. (Importing string and using string.punctuation is a useful way to specify punctuation.)

3. You must then count the word frequency in the candidate’s words. Use a dictionary, where the key is the word and the value is the count.

4. Once you have a dictionary for each candidate, you must extract the 40 most frequently used non-stopwords and their counts.   Since a dictionary is unordered you need to create (count,word) tuples, put them in a list, and then sort the list.  Put count first in the tuple because sorting (using either sort or sorted) will sort on the first item.

# Getting Started 
1. Do the normal startup stuff (download the Git repository and create a project on your hard drive) 
2. Write a high-level outline of what you want to do. Think before you code. 
3. Start by trying to parse the debate text into its three parts: Obama, Romney, everything else (junk). If it makes it easier you can extract a little bit of the file (copy/paste) and make a smaller string so you can see what’s going on with something more simple. Once done, try it out on the big string.
4. Try to do a count of one candidate’s words in a dictionary. Again, use a small string so you can look at the results.
5. Try to extract the top counts in a dictionary.
6. Take a list of words and counts (make some up to start with if you like) and test the function _numWordsSpoken()_.

# Sample Ouput:
The following is an example of what is printed to the shell. Note that the lists are sorted by count.  Gradescope will not consider capitalization or white space when it analyzes your output.  All that matters is the words, counts and their order
 
Obama  
48:governor       44:make           35:romney         26:people        
25:insurance      21:tax            19:plan           19:medicare      
18:money          18:care           17:health         16:years         
16:trillion       16:system         16:businesses     15:small         
15:deficit        15:cut            15:companies      14:jobs          
14:families       13:things         13:taxes          12:education     
12:cuts           12:back           11:revenue        11:reason        
11:opportunity    11:middleclass    11:middle         11:making        
11:folks          11:approach       11:american       10:states        
10:spending       10:fact            9:top             9:time          

Romney  
73:people         39:tax            36:president      35:plan          
33:government     32:cut            31:number         31:medicare      
23:taxes          22:state          22:percent        22:jobs          
22:care           22:america        20:work           19:make          
18:years          18:put            18:billion        17:health        
17:businesses     16:small          15:lower          15:cost          
15:bring          14:business       14:back           13:year          
13:time           13:rates          13:place          13:million       
13:idea           13:federal        13:economy        12:regulation    
12:rate           12:jim            12:insurance      11:trillion      
