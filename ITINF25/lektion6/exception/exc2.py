def delat_med_ett(divisor):
    try:
        result = 1 / divisor
        return result
    # Vi fånger vilket undantag som helst, och kan komma åt dess info som variabeln e
    except Exception as e:
        print("DEBUG OUTPUT", e)
        return 0


res = delat_med_ett(0)
print(res)
