lst = ["volvo", "ahlgrens", "toyota"]

# Experimentera med sep och end

# for loopar behöver något som går att "iterera" efter "in"
for bil in lst:
    print(bil, "bil", sep="")

namn = "karl-johan svensson"
for bokstav in namn:
    print(bokstav, end="")
