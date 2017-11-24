import nltk
import json
import processing

# Variables
library = {"cnwiki.txt", summaryGutenburg}
bigCorpus = word_tokenize(summaryGutenburg)
sentenceBig = sent_tokenize(summaryGutenburg)
sentenceSmall = sent_tokenize("cnwiki.txt")
grammarBig = pos_tag(summaryGutenburg)
grammarSmall = pos_tag("cnwiki.txt")
deflatedBig = {("sentenceBig", "grammarBig")}
deflatedSmall = {("sentenceSmall", "grammarSmall")}
inflatedBig
{("bigCorpus"), ("grammarBig")}


# Processes

def export()
    bigCorpus.json
    sentenceBig.json
    grammarBig.json
    deflatedBig.json
    subjectList
    extSubject


def posAdder(received)
    tokens = word_tokenize(received)
    word_list = pos_tag(tokens)
    pos_dict = {(tokens, word_list)}
    return grammarSmall


def server()
    socket = server
    request = (grammarList, category)
    if receivedRequest=True
    toClient = processing(serverRequest(request))  # if not used now, add proccessing later for multicore support


receivedRequest = False
if receivedCorpus=True
category.write() = processing(serverCorpus(newCorpus))
receivedCorpus = False


def serverRequest(request)
    socket = server
    reply = findMatch(request)


def serverCorpus(newCorpus)
    socket = server
    reply = export(newCorpus)


def findMatch(grammarList, category)
    grammarList = posAdder(grammarList)
    bigCorpus = category.random()
    match = findClosest(grammarList, bigCorpus)
    paragraphText = sensicalMarkov(match, received, bigCorpus)
    return paragraphText


def findClosest(base, hugeGrammar)
    base = wordsList  # create list of words from base markov chain
    wordsList = grammarList  # convert words to grammar tokens
    for grammarList in hugeGrammar
        find
        match
        to
        accuracy  # find a grammatically similar sentence in the corpus. once the parts of speech are found they will tally and the highest score is the match. score will favor match with the most similar count of words as grammarList, then most number of identical pos tags. the goal is to increase the bigCorpus word count
    match = orderedList
    return match  # grammar structure


def sensicalMarkov(match, base, hugeCorpus)
    replace
    words
    from base into
    match  # extra words will be thrown out from original markov chain


replace
extra
words
from hugeCorpus into

match


# increased word count from hugeCorpus

def subjectCategory(newCorpus)
    librarysubjects = "most used words" + "most used successors"
    extSubject = markovChain(up
    to
    7
    words
    deep)
    subjectList = subject(newCorpus)
    subject = subject.match(subjectList)
    return subject


def generate(library)
    librarysubjects.sort(subject)
    scoreList = {(subject, sent_tokenize(subject).numberofmatches())}
    newCorpus = scoreList.top()

    server(receivedCorpus(True), newCorpus)


while online=True
process1(server())
process2(serverRequest())
process3(serverCorpus())

