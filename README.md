# AWS-Serverless-Bill-Calculator-Webapp
This is a simple Web application which calculates the total bill when the number of items and price of each item is entered.

This Project is built using the following AWS services:<br/>
      AWS Lambda --> to create the function which does the backend mathematical operation.<br/>
      AWS API Gateway --> to invoke/trigger the Lambda function using the REST API Gateway invoke url.<br/>
      AWS DynamoDB --> to store the result of a request which is the total bill in a DynamoDB table along with the current time.<br/>
      AWS Amplify --> to deploy the web application.<br/>
      AWS IAM --> to configure the permissions for the Lambda function to interact with DynamoDB table.<br/>
It also has HTML code for the front end.
      
    
