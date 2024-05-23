-- models/event_data.sql

{{ config(materialized='table') }}

SELECT
    id,
    startTime,
    messageTime,
    sportType,
    matchState,
    status,
    marketCount,
    score,
    gameClock,
    eventReferences,
    eventTags,
    lastModifiedTime,
    eventMetadata
FROM {{ source('source', 'api_data') }}