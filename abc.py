def is_gobins(height=120):
    if height >= 170:
        return("You are not a gobin")
    elif height >= 160:
        return("maybe you are a gobin")
    else:
        return("You are a gobin")

is_gobins()
is_gobins(150)
is_gobins(160)
is_gobins(170)
is_gobins(180)