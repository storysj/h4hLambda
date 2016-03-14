#Habitat For Humanity EXCEL parsing Lambda Function
In order to make it dirt simple to automatically create/update build events, it makes sense to utilize AWS's Lambda functions. 

The idea is that all you need to do is register your Lambda function, upload your EXCEL file, and you're done.

The source files for the lambda are contained in the src/ directory. 

```
cd src/
./makeZip.sh
```

Then login to the AWS console, create a Lambda function triggered by S3 creation events, upload the new `src/xlsxReader.zip` file, and you're ready to go! The EXCEL files are expected to match the format of the included SpringBuild.xlsx file.

More information on AWS Lambda can be found here: https://aws.amazon.com/lambda/
