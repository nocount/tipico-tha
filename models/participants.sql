-- models/participants.sql

{{config(materialized='table')}}

-- with participants as (
--     select
--         id,
--         json_extract_path_text(json_text, 'items', true ) as items
--     from participants
-- ),

-- numbers as (
--     select * from numbers
-- ),

-- joined as (
--     select 
--         json_array_length(participants, true) as number_of_items,
--         json_extract_array_element_text(
--             participants, 
--             numbers.ordinal::int, 
--             true
--             ) as item
--     from participants
--     cross join numbers
--         json_array_length(participants.id, true)
-- ),

SELECT
    json_extract_path_text(participants, 'id') as participantId,
    json_extract_path_text(participants, 'name') as name,
    json_extract_path_text(participants, 'position') as position,
    json_extract_path_text(participants, 'abbreviation') as abbreviation
FROM {{ ref('tipico_events_raw') }}