# Function that returns all records based on a pattern: prefix of phone number
"""
create or replace function get_by_phone_prefix(pr varchar)
returns TABLE(name varchar, phone_number char(11)) as
$$
begin
    return query
    select numbers.name, numbers.phone_number from numbers 
	where numbers.phone_number like concat(pr, '%');
end;
$$
language plpgsql;
"""

# Procedure to insert new user by name and phone, update phone if user already exists
"""
create or replace procedure insert_update(
    username varchar,
    phone_num char(11)
)
as $$
begin
    IF EXISTS(SELECT id FROM numbers WHERE name = username) THEN
    UPDATE numbers SET phone_number = phone_num WHERE name = username;
    ELSE
    INSERT INTO numbers(name, phone_number)
    VALUES(username, phone_num);
    END IF;

end;
$$
language plpgsql;
"""

# Procedure to insert many new users by list of name and phone. Use loop and if statement in stored procedure. 
# Check correctness of phone in procedure
"""
create or replace procedure insert_many(
    username varchar[],
    phone_num char(11)[]
)
as $$
begin
    FOR i IN 1..array_length(username, 1) LOOP
	IF LENGTH(phone_num[i]) = 11 THEN 
		INSERT INTO numbers(name, phone_number) VALUES(username[i], phone_num[i]);
	END IF;
	END LOOP;
end;
$$
language plpgsql;
"""


# Function to querying data from the tables with pagination (by limit and offset)
"""
create or replace function get_with_pagination(page INT, lim INT)
returns TABLE(name varchar, phone_number char(11)) as
$$
begin
    return query
    select numbers.name, numbers.phone_number from numbers 
	ORDER BY numbers.name 
	LIMIT lim OFFSET (page-1)*lim;
end;
$$
language plpgsql;
"""
