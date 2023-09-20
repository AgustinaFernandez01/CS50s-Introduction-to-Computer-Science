-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Query to find the crime scene report matching the date and location
SELECT *
FROM crime_scene_reports
WHERE date = '2021-07-28' AND location = 'Humphrey Street';
-- Query to identify the thief based on interview information
SELECT DISTINCT p.name AS thief_name
FROM people p
JOIN interviews i ON p.id = i.person_id
WHERE i.info LIKE '%duck%' AND i.info LIKE '%stolen%';
-- Query to identify the thief's accomplice based on interview information
SELECT DISTINCT p.name AS accomplice_name
FROM people p
JOIN interviews i ON p.id = i.person_id
WHERE i.info LIKE '%accomplice%' AND i.info LIKE '%helped%';
