from model import get_data, tt_split

#random tests to showcase how pytest works
#basically, assert takes in boolean logic. so, to test if something works,
#you'd put something to get a 'True' or a 'False'. the rest is self explanatory. 
def test_get_data():
    df = get_data("../dataset.csv")
    assert df[['Hours']].shape == df['Scores'].shape

def test_tt_split():
    x_tr, x_te, y_tr, y_te = tt_split(get_data("../dataset.csv"))
    assert x_tr.shape == y_tr.shape
    assert x_te.shape == y_te.shape
