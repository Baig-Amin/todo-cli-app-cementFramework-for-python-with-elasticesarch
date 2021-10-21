# Creating Index

```
index(index="test-my-index", doc_type="my-test-type", id=1, document=query)
```

# Data in index

```
{
    "_index" : "test-my-index",
    "_type" : "my-test-type",
    "_id" : "1",
    "_score" : 1.0,
    "_source" : {
        "author" : "kai",
        "text" : "Interesting content.",
        "timestamp" : "2021-10-17T01:51:46.487372"
    }
}
```
