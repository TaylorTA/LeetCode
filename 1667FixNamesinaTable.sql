select user_id, CONCAT(UPPER(SUBSTR(name, 1,1)),LOWER(SUBSTR(name,2))) as name
from Users
order by user_id ASC
