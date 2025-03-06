p = print

words = {"burk", "bil", "kanot", "rep"}
words2 = {"burk", "spis", "hamburgare"}
words3 = {"röd", "blå"}

p("bil in words?", "bil" in words)
p("cykel in words?", "cykel" in words)

# Mängdoperation: "Disjunkt" på sv, om två mängder inte har några
# gemensamma element
p("words och words2 isdisjoint?", words.isdisjoint(words2))
p("words och words3 isdisjoint?", words.isdisjoint(words3))
