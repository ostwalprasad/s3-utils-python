# s3-utils-python


Collection of S3 utilites to load/store/delete data files and pickled python files from Python. To use this module please store your AWS credentials in /.aws folder if you haven't already. config.py file is used to define all models/buckets and paths for S3.

## Utilities:

More information about function in code. Brief here:

1. ```load_file(self,file:"string",bucket:"bucketname")->"bytes":```

Loads file from S3 in form of bytes
2. ```store_file(self,filesource:"filename",filedestination:"filename",bucket:"bucketname")->"response":```

Store file from local to S3
3. ```delete_file(self,file:"filename",bucket:"bucketname")->"response":```

Delete file from S3
4. ```dload_pickle_model(self,file:'string',bucket:'bucketname') -> 'Model Object' :```

Load Pickle model from S3. Return python object
5. ```store_pickle_model(self,model_object:'Model Object',file:"filename",bucket:'bucketname')->'response':```

Store object into S3 in form of pickles model. No need to pickle it manually, Just pass object name. Function will picke first and then upload to S2.
6.```load_csvdataframe(self,file:"filename",bucket:'bucketname')->'Pandas Dataframe':```

Load csv file from S3 into Pandas Dataframe``
7. ```store_csvdataframe(self,dataframe:'pandas dataframe',file:'filename',bucket:'bucketname'):```

Store Pandas dataframe into csv format in S3

## Example:

```
mys3 =s3.s3_utils(prod=True)
mymodel  = mys3.load_pickle_model("regressionmodel.pickle","ml-models")
```






