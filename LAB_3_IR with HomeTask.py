#!/usr/bin/env python
# coding: utf-8

# <h2> Exercise 1 </h2>

# In[48]:


import re


# In[49]:


txt = "Regular expression is a sequence of character(s) mainly used to find and replace patterns in a string or file"

#Check if the string starts with 'Regular and ends with file':

x = re.findall("^Regular", txt)
x = re.findall("file$", txt)
if x:
  print(txt)
else:
  print("No match")


# <h2> Exercise 2 </h2>

# In[64]:


replacement_patterns = [ 
(r'won\'t', 'will not'), 
(r'can\’t', 'cannot'), 
(r'i\'m', 'i am'), 
(r'ain\'t', 'is not'), 
(r'(\w+)\'ll', '\g<1> will'), 
(r'(\w+)n\'t', '\g<1> not'), 
(r'(\w+)\'ve', '\g<1> have'), 
(r'(\w+)\'s', '\g<1> is'), 
(r'(\w+)\'re', '\g<1> are'), 
(r'(\w+)\'d', '\g<1> would')]


# In[65]:


class RegexpReplacer:    
    
    def __init__(self, patterns=replacement_patterns): 
        self.patterns = [(re.compile(regex), repl) for (regex, repl)in patterns] 
    
    def replace(self, text): 
        s = text 
        for (pattern, repl) in self.patterns: 
            (s, count) = re.subn(pattern, repl, s) 
        return s


# In[66]:


Sentence1="We'll see how to replace words using regular expressions such doesn't, can’t and so on"


# In[67]:


b = RegexpReplacer(replacement_patterns)


# In[68]:


x = b.replace(Sentence1)
x


# <h2> Exercise 3 </h2>

# In[92]:


class RepeatReplacer(object): 
    
    def __init__(self): 
        self.repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)') 
        self.repl = r'\1\2\3'
            
        
    def replace(self, word): 
        repl_word = self.repeat_regexp.sub(self.repl, word) 
        if repl_word != word: 
            return self.replace(repl_word) 
        else: 
            return repl_word


# In[94]:


Sentence = "We likkkkkke python" 


# In[95]:


v = RepeatReplacer()


# In[100]:


z = v.replace(Sentence)
z


# <h2> Home Task 1 </h2>

# In[175]:


# beauty_soup.py

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")


# In[182]:


def convert_to_lower(match_obj):
    if match_obj.group() is not None:
        return match_obj.group().lower()


# In[184]:


res_str = re.sub(r"[A-Z]", convert_to_lower, soup.get_text())


# In[187]:



print(res_str)


# In[ ]:




