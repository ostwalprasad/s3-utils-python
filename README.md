# s3-utils-python


Collection of S3 utilites to load/store/delete data files and pickled python files from Python. To use this module please store your AWS credentials in /.aws folder if you haven't already. config.py file is used to define all models/buckets and paths for S3.

## Utilities:

More information about function in code. Brief here:

1. **Loads file from S3 in form of bytes**
 ```load_file(self,file:"string",bucket:"bucketname")->"bytes":```


2. **Store file from local to  S3** ```store_file(self,filesource:"filename",filedestination:"filename",bucket:"bucketname")->"response":```

3. **Delete file from S3** 
```delete_file(self,file:"filename",bucket:"bucketname")->"response":```

4. **Load Pickle model from S3 and return object** ```load_pickle_model(self,file:'string',bucket:'bucketname') -> 'Model Object' :```

5. **Store object into S3 in form of pickle file** 
No need to pickle it manually, Just pass object name. Function will picke first and then upload to S2.
```store_pickle_model(self,model_object:'ModelObject',file:"filename",bucket:'bucketname')->'response':```

7. **Load csv file from S3 into Pandas Dataframe** ```load_csvdataframe(self,file:"filename",bucket:'bucketname')->'Pandas Dataframe':```
``
8. **Store Pandas dataframe into csv format in S3** ```store_csvdataframe(self,dataframe:'pandasdataframe',file:'filename',bucket:'bucketname'):```


## Example:
To load pickled model from S3 and convert back into object. Use this.
```
mys3 =s3.s3_utils(prod=True)
mymodel  = mys3.load_pickle_model("regressionmodel.pickle","ml-models")
```
## Configs

Use `config.py` file to specify bucket names, files names and AWS hosts etc.

    MODEL_BUCKET_NAME = 'model-bucket-name'
    DATA_BUCKET_NAME= 'data-bucket-name'
    MODEL_FILE_NAME = 'model.pkl'
    AWS_S3_HOST='ap-south-1'
    LAMBDA_TEMP_FOLDER = '/tmp/'
    LOCAL_TEMP_FOLDER = "/"


