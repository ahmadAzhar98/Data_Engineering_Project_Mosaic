# Overview and Scenario
You have been hired by the Data Mosaic Initiative, an organization aiming to gather multi-faceted insights on emerging topics. Your mission is to collect data from multiple sources of different types (structured, unstructured, semi-structured), store or upload it to a repository, and produce a short report that demonstrates your pipeline design and addresses theoretical considerations.


# Link for dataset
https://www.kaggle.com/datasets/mithileshbwankhede/ipl-player-performance-dataset-2008-2023

## Step 1
create a virtual environment using this command - python3 -m venv <env_name>

## Step 2
activate virtual environment - source <name>/bin/activate  

## Step 3
run this command - pip install -r requirements.txt

## Step 4 
create an developer API account for reddit from this link
https://www.reddit.com/prefs/apps
to generate REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET and USER_AGENT. Once done create an .env and paste them there.

## Step 5
cd scripts and run each pipeline one by one using the command - python3 <pipeline_name> as a result new data will appear in dataset/raw and dataset/clean
