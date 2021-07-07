import twitterConnection
import pandas as pd
import numpy as np

tweetDict = twitterConnection.tweetDictionary
tweetSearch = twitterConnection.twitterSearch
tweetSearch('bitcoin', 100)


twitterDF = pd.DataFrame.from_dict(
    tweetDict, orient="index")
twitterDF.to_excel('twitterData.xlsx')
