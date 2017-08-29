#!/opt/bin/python
text = "Python!"
tum = []
def reverse(text):
  for i in range(len(text)):
    tum.append(text[len(text) - i - 1])
  return "".join(tum)
print reverse(text)

#anti_vowel
def anti_vowel(text):
  test = []
  for i in text:
    if i in "aeiouAEIOU":
      print ""
    else:
      test.append(i)
  else:
    return "".join(test)

#lower case

word = "WordLETTER"
t = word.lower()
print t

#split

text = "this hack is wack hack"

text = text.split(' ' , 1 )
print text


#****
text = "this hack is wack hack"
word = "hack"

def censor(text, word):
  test = []
  text = text.split()
  for i in text:
    if i == word:
      test.append("*" * len(word))
    else:
      test.append(i)
  else:
    return " ".join(test)

print censor(text, word)

#median
li = [1, 34, 1, 6, 8, 0]

def median(li):
  for i in range(len(li)):
    so = sorted(li)
    print so
    a = so[len(li) / 2]
    b =  so[(len(li) / 2 - 1)]
    print a
    print b
    if len(li) == 1:
      return li[i]
    elif len(li) % 2 == 0:
      return (a + b) / 2.0
    else:
      return so[(len(li) - 1) / 2]
print median(li)
