-- models/group.sql

{{config(materialized='table')}}

SELECT
    json_extract_path_text(group, 'id') as groupId, 
    json_extract_path_text(group, 'name') as name, 
    json_extract_path_text(group, 'parentGroup') as parentGroup,
FROM {{ ref('tipico_events_raw') }}