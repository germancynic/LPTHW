class ParseError(Exception):
    pass

class Sentence(object):
    def __init__(self, subject, verb, object):
        """ Each argument 'subject', 'verb', 'object' is a tuple containing the code and word"""
        self.subject = subject
        self.verb = verb
        self.object = object

def peek(word_list):
    """ 
    word_list is a list of tuples in the form (code, word).
    This method returns the code of the first tuple in the list
    """
    if(word_list):
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting):
    """ 
    Returns the first word if it matches the expecting type, else returns None.
    In any case, the first word will be removed from the word_list
    """
    ret_val = None
    if(word_list):
        word_tuple = word_list.pop(0)
        if(word_tuple[0] == expecting):
            ret_val =  word_tuple
    
    return ret_val

def skip(word_list, word_type):
    if(word_list):
        while(peek(word_list) == word_type):
            match(word_list, word_type)

def parse_subject(word_list, subject):
    skip(word_list, 'stop')
    verb = match(word_list, 'verb')
    if(verb == None):
        raise ParseError("Expecting a verb")

    skip(word_list, 'stop')
    object = match(word_list, 'noun')
    if(object == None):
        raise ParseError("Expecting a noun")

    return Sentence(subject, verb, object)

def parse_sentence(word_list):
    """ Accepts a list of tuples, where each tuple contains (code, word)"""
    skip(word_list, 'stop')
    start = peek(word_list)
    if(start == 'noun'):
        subject = match(word_list, 'noun')
        return parse_subject(word_list, subject)
    elif(start == 'verb'):
        subject = ('noun', 'player')
        return parse_subject(word_list, subject)
    else:
        raise ParseError("Must start with either a noun or a verb ... not '%s'" % start)