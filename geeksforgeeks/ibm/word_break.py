def word_break(word, dict):
    n = len(word)
    wb = [False] * n

    print(dict)

    for i in range(n):
        if wb[i] is False and word[0:i + 1] in dict:
            wb[i] = True

        if wb[i] is True:
            if i == n - 1:
                return True

            # update if needed
            for j in range(i + 1, n):
                if wb[j] == False and word[i:j] in dict:
                    wb[j] = True
                    print("True for ", word[i:j])

                if j == n - 1 and wb[j] == True:
                    return True

    print(wb)

# test
dictionary = {"mobile" : 1,"samsung" : 1,"sam" : 1,"sung" : 1,"man" : 1,"mango" : 1,
    "icecream" : 1,"and" : 1,"go" : 1,"i" : 1,"like" : 1,"ice" : 1,"cream" : 1}

word = "ilikelike"

print(word_break(word, dictionary))
