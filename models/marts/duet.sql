SELECT Name, Count(*) FROM {{ ref('py_duet') }}
GROUP BY Name
