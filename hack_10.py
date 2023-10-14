"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    txt = "fooziman"

    change = txt.replace("o","0").replace("i","1").replace("a","@").upper()
    split = list(change)
    return split  