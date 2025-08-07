# 2-Tier Serverless Web Application on AWS

This project is a full-stack, serverless web application built on Amazon Web Services (AWS). It demonstrates a classic 2-tier architecture, separating the frontend presentation layer from the backend application and data logic. The application allows users to view data from a database and submit new data through a web form.

## Architecture Diagram

The application follows a simple, scalable, and cost-effective serverless pattern.

## Tech Stack

### Frontend:
1. HTML  
2. CSS  
3. JavaScript (Fetch API for API calls)  

### Backend & Infrastructure:
- **Amazon S3**: For static website hosting.  
- **Amazon API Gateway**: To create and manage the RESTful API (GET & POST endpoints).  
- **AWS Lambda**: For serverless compute functions (Python).  
- **Amazon DynamoDB**: As the NoSQL database for data storage.  
- **AWS IAM**: To manage secure access between AWS services.  

## Project Workflow & Setup

This project was built by first configuring the backend infrastructure, followed by the frontend deployment.

### Backend Configuration

#### Database Creation (Amazon DynamoDB):
- A NoSQL table was created in DynamoDB to serve as the primary data store.

#### Permissions Setup (AWS IAM):
- An IAM Role was created with policies granting full access to the DynamoDB table.
- This role is assumed by the Lambda functions to allow them to read and write data.

#### Compute Logic (AWS Lambda):
Two separate Python-based Lambda functions were created:
- **GET Function**: Retrieves existing items from the DynamoDB table.
- **POST Function**: Inserts new items into the DynamoDB table.

#### API Endpoint (Amazon API Gateway):
A REST API was configured with two corresponding methods:
- **GET Method**: Linked to the "get data" Lambda function.
- **POST Method**: Linked to the "insert data" Lambda function.

- CORS (Cross-Origin Resource Sharing) was enabled for both methods to allow requests from the S3 website origin.
- The API was deployed to a stage, which generated a unique **Invoke URL**.

### Frontend Configuration

#### Application Code:
- The **Invoke URL** from API Gateway was pasted into the `script.js` file, connecting the frontend's fetch calls to the live API endpoints.

#### Static Hosting (Amazon S3):
- An S3 bucket was created and configured for public access.
- The `index.html` and `script.js` files were uploaded to the bucket.
- Static website hosting was enabled, with `index.html` set as the entry point.

## Usage

To use the application, navigate to the **public website endpoint URL** provided by the S3 bucket's static hosting configuration.

- The page will load and display existing data by calling the **GET** endpoint.
- Users can fill out the form and click **"Submit"** to send new data to the database via the **POST** endpoint.
