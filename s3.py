"""
Util functions for S3
© Aranti.ai
Author: Prasad Ostwal
"""

from .config import *
import boto3
import joblib
import pandas as pd

class s3_utils():
	"""
	Utilities to IO operations on Amazon S3. 
	This library assumes that credentials are stored locally or class is being called from lambda.
	"""
	def __init__(self,prod=False):
		"""
		Connect to S3 when object is created
		"""
		self.S3 = boto3.client('s3', region_name=AWS_S3_HOST)
		if prod is True:
			self.folder = LAMBDA_TEMP_FOLDER
		else:
			self.folder = LOCAL_TEMP_FOLDER

	def load_file(self,file:"string",bucket:"bucketname")->"bytes":
		"""
		
		Args:
			file: filename that has to be loaded
			bucket: bucketname

		Returns:
			Bytes containing data of file.
		
		Example:
			s3.load_file("learn.txt",BUCKET_NAME)

		"""
		response = self.S3.get_object(Bucket=bucket, Key=file)
		return response['Body'].read() 

	def store_file(self,filesource:"filename",filedestination:"filename",bucket:"bucketname")->"response":
		"""

		Args:
			filesource: Filename with path and extension
			filedestination: filename with path and extension
			bucket: bucketname

		Returns:
			Not defined yet

		Example:
			s3.store_file("learn.txt","learn.txt",BUCKET_NAME)

		"""
		self.S3.upload_file(filesource, bucket,filedestination)

	def delete_file(self,file:"filename",bucket:"bucketname")->"response": #TODO: Not checked yet
		"""

		Args:
			file: filname that exists in bucket
			bucket: bucketname

		Returns:
			Not defined yet

		Example:
			s3.delete_file("learn.txt",BUCKET_NAME)

		"""
		self.S3.delete_object(Bucket=bucket,Key=file)

	def load_pickle_model(self,file:'string',bucket:'bucketname') -> 'Model Object' :
		"""

		Args:
			file: filename of pickled object that exists in bucket
			bucket: bucketname

		Returns:
			Object extracted from picked file

		Example:
			myobj = s3.load_pickle_model("Regression.pkl",BUCKET_NAME)
			myobj.predict(x)

		"""
		data = self.load_file(file=file,bucket=bucket)
		myfile = open(f"{self.folder}{file}", "wb")
		myfile.write(data)
		with open(f"{self.folder}{file}", 'rb') as myfile:
			model = joblib.load(myfile)
		return model

	def store_pickle_model(self,model_object:'Model Object',file:"filename",bucket:'bucketname')->'response':
		"""

		Args:
			model_object: Object that needs to be pickled and stored into S3
			file: filename for object
			bucket: bucketname

		Returns:
			Not defined yet

		Example:
			from sklearn.linear_model import LinearRegression
			lm = LinearRegression()
			s3.store_pickle_model(lm,"Regression.pkl",BUCKET_NAME)
		"""
		joblib.dump(model_object,f"{self.folder}{file}")
		self.store_file(filesource=f"{self.folder}{file}",bucket=bucket,filedestination=file)

	def load_csvdataframe(self,file:"filename",bucket:'bucketname')->'Pandas Dataframe':
		"""

		Args:
			file: filename of csv file
			bucket: bucketname

		Returns:
			Pandas DataFrame


		Example:
			data = s3.load_csvdataframe("myfile.csv",BUCKET_NAME)
		"""
		data = self.load_file(file=file,bucket=bucket)
		return pd.read_csv(io.BytesIO(data))

	def store_csvdataframe(self,dataframe:'pandas dataframe',file:'filename',bucket:'bucketname'):
		"""

		Args:
			dataframe: Pandas dataframe
			file: filename
			bucket: bucketname

		Returns:
			Not yet defined

		Example:

			s3.store_csvdataframe(dataframe,"data.csv",BUCKET_NAME)

		"""
		dataframe.to_csv(f"{self.folder}{file}")
		self.store_file(filesource=f"{self.folder}{file}",filedestination=file,bucket=MODEL_BUCKET_NAME)