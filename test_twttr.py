from twttr import shorten

#run test for twttr problem set
def test_twttr():
    assert shorten("My twitter is popular! Ha ha!") == "My twttr s pplr! H h!"