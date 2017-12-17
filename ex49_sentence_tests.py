from nose.tools import *
from ex49 import sentence
from ex49 import lexicon

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_peek():
    #test a line with one word
    line1 = "princess"
    word_tuples1 = lexicon.scan(line1)
    word_type1 = sentence.peek(word_tuples1)
    assert_equal("noun", word_type1)

    #test a line with multiple words
    line2 = "princess ate the bear"
    word_tuples2 = lexicon.scan(line2)
    assert_equal("noun", sentence.peek(word_tuples2))

def test_match():
    #test a line with one word
    line1 = "princess"
    word_tuples1 = lexicon.scan(line1)
    assert_equal("princess", sentence.match(word_tuples1, 'noun')[1])
    #Here we should get a None for any type since there is nothing in the word_list
    assert_equal(None, sentence.match(word_tuples1, 'noun'))

    #test a line with multiple words
    line2 = "princess eat the bear"
    word_tuples2 = lexicon.scan(line2)
    assert_equals(4, len(word_tuples2))
    assert_equal("princess", sentence.match(word_tuples2, "noun")[1])
    assert_equal("eat", sentence.match(word_tuples2, "verb")[1])
    assert_equal("the", sentence.match(word_tuples2, 'stop')[1])
    assert_equal("bear", sentence.match(word_tuples2, 'noun')[1])

def test_skip():
    #test a line with one word
    line1 = "princess"
    word_tuples1 = lexicon.scan(line1)
    sentence.skip(word_tuples1, "verb")
    assert_equal(1, len(word_tuples1))
    sentence.skip(word_tuples1, 'noun')
    assert_equal(0, len(word_tuples1))

    #test a line with multiple words
    line2 = "princess eat the bear"
    word_tuples2 = lexicon.scan(line2)
    sentence.skip(word_tuples2, "verb")
    assert_equal(4, len(word_tuples2))
    sentence.skip(word_tuples2, "noun")
    assert_equal(3, len(word_tuples2))
    sentence.skip(word_tuples2, "verb")
    assert_equal(2, len(word_tuples2))
    
    
        

def test_parse_sentence():
    line = "princess eat the bear"
    word_list = lexicon.scan(line)
    parsed_sentence = sentence.parse_sentence(word_list)
    assert_equal("princess", parsed_sentence.subject[1])
    assert_equal("eat", parsed_sentence.verb[1])
    assert_equal("bear", parsed_sentence.object[1])