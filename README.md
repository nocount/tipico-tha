# tipico-tha
Two part take home assignment for Tipico interview process

# Project Description

## Task 1:

The dag performs the api query and then writes to Redshift using the pandas_redshift library(pandas to_sql was also considered but I ran into some tricky engine issues connecting to my Redshift instance).  
Dag can be edited with S3/Redshift credentials then put into the dags directory of a running airflow app then activated and it should run every 10 minutes and upload to the Redshift cluster.  
Tested on aiflow server running on a personal EC2 instance

## Task 2:
Created a data model based on the extracted data from the api and is basically as follows:


Data Model Design  

Entities and Attributes:  
EventDetails: eventId, sport, category, startTime  
Participants: participantId, eventId, name, role  
Group: groupId, eventId, name,parentGroupId  
Markets: marketId, eventId, specifier  
Outcomes: outcomeId, marketId, name, odds  


Relationships:
Each event can have multiple participants.  
Each event belongs to a group.  
Each event can have multiple markets.  
Each market can have multiple outcomes.  

UML Diagram:




## Task 3:
dbt project was created using dbt cloud and synced with my personal github and used my personal Redshift as a connector to perform the modeling and transformations.  
In the project I focused on the data models for the core Event, Group and Participants








