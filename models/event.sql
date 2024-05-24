-- models/event.sql

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
FROM {{ ref('tipico_events_raw') }}