p = print

words = {"burk", "bil", "kanot", "rep"}
words2 = {"burk", "spis", "hamburgare"}

p("bil in words?", "bil" in words)
p("cykel in words?", "cykel" in words)

p("words och words2 isdisjoint?", words.disjunct(words2))
