#Habitat For Humanity EXCEL parsing Lambda Function
In order to make it dirt simple to automatically create/update build events, it makes sense to utilize AWS's Lambda functions. 

The idea is that all you need to do is register your Lambda function, upload your EXCEL file, and you're done.

The source files for the lambda are contained in the src/ directory. 

```
cd src/
./makeZip.sh
```

Then login to the AWS console, create a Lambda function triggered by S3 creation events, upload the new `src/xlsxReader.zip` file, and you're ready to go! The EXCEL files are expected to have the below columns:

```
0 Campaign Name
1 Donor Preferred Listing
2 Sage ID
3 Opportunity Name
4 Build Group or Event
5 Division
6 Family Name
7 Address
8 Lot #
9 Community
10 Amount
11 Build Day 1
12 Build Day 2
13 Build Day 3
14 Build Day 4
15 Build Day 5
16 Build Day 6
17 Build Day 7
18 Build Day 8
```

More information on AWS Lambda can be found here: https://aws.amazon.com/lambda/
