# Aggreagting multiple CSV files and Loading to Redshift table using AWS EMR and Glue

My goal is aggreagte multiple CSV files in the S3 bucket, Load the result to S3 using EMR and load aggreagted data to Redshift table with AWS Glue.

----------------------------------------------------------------------------------------------------------------------------------------------------

Part 1: 

Aggregate csv files from S3 bucket and load to another S3 bucket folder.


1. Launch EMR cluster. 

2. SSH Into The Cluster

3. Create an S3 bucket with folders:
   input
   output
   files
   
5. Upload csv files to input folder.

6. Once in the EMR terminal, opn a new file named spark-etl.py using the following command:

    nano spark-agg.py
    
7. Copy & Paste the code from repo into that file.

8. Save that file by pressing Ctrl X then typing Y to accept writing the data and then Enter to save the changes you made.

9. Submit that pySpark spark-agg.py job on the cluster  or create EMR step to run that script, this Spark job will aggregate from input folder and write    to the output folder: 
  
   Option 1:    spark-submit spark-agg.py s3://<YOUR-BUCKET>/input/ s3://<YOUR-BUCKET>/output/spark
   
   Option 2: 
   
            2.1 In the AWS console, navigate to the S3 bucket you created in the previous section.
   
            2.2 Create a file named spark-agg.py on your computer.
   
            2.3 Copy and past this code into the spark-agg.py file. (Notice that the last line is updated.)
   
            2.4 Upload this file to the files folder in your S3 bucket.
   
            2.5 Navigate to the EMR service in the AWS console and select your cluster.
   
            2.6 Select the Steps tab.
   
            2.7 For the Step Type choose Custom Jar
   
            2.8 Name the Step.
   
            2.9 For JAR Location input command-runner.jar
   
            2.10 For the Arguements section input the following code replacing with your bucket name:
   
                  spark-submit s3://<bucketname>/files/spark-agg.py s3://<bucketname>/input s3://<bucketname>/output/spark
   
            2.11 Click Add.
            
  
    Once the job completes successfully, you navigate to the output folder to check if an output/ with data is created.
  
----------------------------------------------------------------------------------------------------------------------------------------------------          

Part 2: 

Now We have an aggreated file under s3://<bucketname>/output/spark. We need to load that file to Redshift cluster. We will use AWS Glue to t load data from S3 to Redshift table. 


   1. Create a Redshift cluster.
   
   2. Create a table to load data to that table:
   
      create table res_tbl(ftr text, count int)
   
   3. Create AWSGluerole IAM role with the below policies

      <img width="1129" alt="Screen Shot 2022-11-29 at 11 12 59 AM" src="https://user-images.githubusercontent.com/28351206/204582673-b454bbd6-cb7e-4dcb-b9e7-6b55e8832396.png">

   4. Create a Glue crawler for S3 data using s3://<bucketname>/output/spark and the crawler. 
   
   5. Create Redshift connection in AWS Glue. 
   
   5. Create a Glue crawler for Redshift table using res_tbl table and the crawler. 
   
   6. Create a Glue ETL job based on source(S3 data source) and target (Redshift table data source) and run the job.
   
After successfully completing the job you will see the data in Redshift table.

