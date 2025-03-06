p = print

words = {"burk", "bil", "kanot", "rep"}
words2 = {"burk"}
words3 = {"röd", "blå"}

# p("words2 issubset i words?", words2.issubset(words))
# p("words issubset i words2?", words.issubset(words2))

# lst = ["a", "b", "c"]

# # auto typecast till set inuti issubset()
# p(words2.issubset(swords))

# allt som inte finns i den mängd som funktionen tar
# p("difference words och word2", words.difference(words2))
# p("difference words2 och words", words2.difference(words))

# lika
p("difference words och word2", words.symmetric_difference(words2))
p("difference words2 och words", words2.symmetric_difference(words))
