# FriendBuy

# Run
The code can simply run using 

```
python main.py
```

You will have to give all the inputs as stdin and the output will be printed on stdout as well.
If wrong commands are given, the code will throw a RuntimeError

# Algorithm

To store the current state of database and valueAnalytics, we use two different dictionaries.

To support transaction blocks, we have a list of transactionBlocks which keeps the current DB and valueAnalytics. 

When we rollback, we simply pop out the last transactionBlock

When we commit, we simply commit the last transactionBlock, as that has commits from all the previous transactions as well. We also clear out the list here so that we don't store extra space in memory

# UnitTests

The repo contains some unit tests as well, if you want to run them, just uncomment this line in main.py(right now line 46)
```
# UnitTests()
```
