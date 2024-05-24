-- models/participants.sql

{{config(materialized='table')}}

SELECT
    json_extract_path_text(participants, 'id') as participantId,
    json_extract_path_text(participants, 'name') as name,
    json_extract_path_text(participants, 'position') as position,
    json_extract_path_text(participants, 'abbreviation') as abbreviation
FROM {{ ref('tipico_events_raw') }}