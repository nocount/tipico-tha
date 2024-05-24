# tipico-tha
Three part take home assignment for Tipico interview process

# Project Description

## Task 1 - Airflow DAG:

The dag(tipico_event_dag.py) performs the api query and then writes to Redshift using the pandas_redshift library(pandas to_sql was also considered but I ran into some tricky engine issues connecting to my Redshift instance).  

Dag can be edited with S3/Redshift credentials then put into the dags directory of a running airflow app then activated and it should run every 10 minutes and upload to the Redshift cluster.  
[Serverless Redshift](docs/redshift_env.PNG)

Tested on aiflow server running on a personal EC2 instance
[Dag Running on Airflow Server](docs/event_dag.PNG)

## Task 2 - Data Model:
The next task was to create a data model based on the data we extracted and stored in the previous task.

I created a data model, described below, and then created a class diagram to better visualize the entire model.

[Class Diagram](docs/tipico_event_model.png)


### Design Description:

Entities:

### Event:

Attributes:  
eventId: int  
groupId: int  
sport: string  
category: string  
startTime: datetime  
messageTime: datetime    
sportType: string  
matchState: string  
status: string  
marketCount: int  
score: int  
gameClock:  string  
eventReferences: string  
eventTags: string  
lastModifiedTime: string  
eventMetadata: string  

Relationships:  
Belongs to one Group (One-to-Many)  
Has many Participants (Many-to-Many) through the EventParticipant association table.  
Has many Markets (One-to-Many)  

### Participant:

Attributes:
participantId: int  
name: string  
position: string  
abbreviation: string  

Relationships:
Participates in many Events (Many-to-Many) through the EventParticipant association table.

### Group:

Attributes:
groupId: int  
name: string  
parentGroupId: int  

Relationships:
Contains many Events (One-to-Many)

### Market:

Attributes:
marketId: int  
eventId: int  
specifier: string  

Relationships:
Belongs to one Event (One-to-Many)
Has many Outcomes (One-to-Many)

### Outcome:

Attributes:
outcomeId: int  
marketId: int  
name: string  
odds: float  

Relationships:
Belongs to one Market (One-to-Many)

### Specifier:

Attributes:
eventId: int  
key: string  
value: float  
type: string  

Relationships:
Belongs to one Market (One-to-Many)




## Task 3 - DBT Project:
The next task was to create a dbt project to implement the data model and transformations that we designed and documented in the previous step.

The dbt project was created using dbt cloud and synced with my personal github and used my personal Redshift as a connector to perform the modeling and transformations.  

File sturcture is dbt standard and all relevant transforms are found under the models/ dir.

In the project I focused on the data models for the core Event, Group and Participants as shown in the models directory of the dbt project.

Since Redshift lacks a flatten or unnest type function the transformations for the group and participant models proved complex and I was not able to finish them completely with the time I allowed myself.

[DBT env](docs/dbt_env.PNG)




