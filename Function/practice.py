def cheeseshop(kind, *arguments, **keywords):
    print("Do You Have Any ", kind, "?")
    print("I'm Sorry, we're all out of ",kind )


    for arg in arguments:
        print(arg)
    print("-" * 40)

    for kw in keywords:
        print(kw,": ", keywords[kw])

cheeseshop('Variable Length', "it's very runny, sir",
            "it's really very, very, very runny, sir",
            shopkeeper="Sarwar mithu",
            clint="Sadiya",
            sketch="cheese shop sketch")


    