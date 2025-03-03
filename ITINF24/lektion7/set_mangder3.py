p = print

words = {"burk", "bil", "kanot", "rep"}
words2 = {"burk"}
words3 = {"röd", "blå"}

p("words2 issubset i words?", words2.issubset(words))
p("words issubset i words2?", words.issubset(words2))
