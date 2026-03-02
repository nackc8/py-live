def delat_med_ett(divisor):
    return 1 / divisor


try:
    delat_med_ett(0)
    # Vi skriver bara except, kan inte se vilket exception det var eller dess info
except:
    print("Nu gick det åt pipan")
