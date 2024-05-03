import psycopg2

conn = psycopg2.connect(host="localhost", dbname="Nurtay", user="postgres", password="kaziev2004", port="5432")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS person(
   id INT PRIMARY KEY,
   name VARCHAR(255),
   phone VARCHAR(255),
   gender CHAR);
   """)

cur.execute("""INSERT INTO person (id, name, phone, gender) VALUES
            (1, 'Mike', '8747179', 'm'),
            (2, 'ajsjs', '8747179', 'm'),
            (3, 'Diaskojsaoi', '8707900', 'f')""")

conn.commit()

cur.close()
conn.close()
#1
SELECT * from person
CREATE OR REPLACE FUNCTION get_records_by_pattern(p_pattern VARCHAR)
RETURNS TABLE(id INT, name VARCHAR, phone INT, gender CHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT person.id, person.name, person.phone, person.gender
    FROM person
    WHERE person.name ILIKE '%' || p_pattern || '%'
    OR person.phone::TEXT ILIKE '%' || p_pattern || '%'
    OR person.id::TEXT ILIKE '%' || p_pattern || '%'
    OR person.gender::TEXT ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;
SELECT * FROM get_records_by_pattern('Johsss');

# #3
 CREATE OR REPLACE FUNCTION insert_users(p_names VARCHAR[], p_phones VARCHAR[])
RETURNS TABLE (name VARCHAR, phone VARCHAR, error_message VARCHAR) AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(p_names, 1) LOOP
        -- Check if phone is numeric and has correct length
        IF length(p_phones[i]) <> 9 OR NOT (p_phones[i] ~ '^[0-9]+$') THEN
            -- Return incorrect phone number
            RETURN QUERY SELECT p_names[i], p_phones[i], 'Incorrect phone number'::VARCHAR;
        ELSE
            -- Insert the user
            BEGIN
                INSERT INTO person (id, name, phone, gender) VALUES (DEFAULT, p_names[i], p_phones[i], 'm');
            EXCEPTION WHEN OTHERS THEN
                -- Return error if insertion fails
                RETURN QUERY SELECT p_names[i], p_phones[i], 'No error'::VARCHAR;
            END;
        END IF;
    END LOOP;

    RETURN;
END;
$$ LANGUAGE plpgsql;

-- Example usage
SELECT * FROM insert_users(ARRAY['Dik', 'Bob', 'John Dok'], ARRAY['8747179', 'abc123456', '987654321']);

#5
SELECT * from person
CREATE OR REPLACE PROCEDURE delete_user_by_username_or_phone(p_delete_by VARCHAR, p_value VARCHAR)
AS $$
BEGIN
    IF p_delete_by = 'username' THEN
        DELETE FROM person WHERE name = p_value;
    ELSIF p_delete_by = 'phone' THEN
        DELETE FROM person WHERE phone::TEXT = p_value;
    ELSE
        RAISE EXCEPTION 'Invalid delete_by parameter. Use "username" or "phone".';
    END IF;
END;
$$ LANGUAGE plpgsql;

CALL delete_user_by_username_or_phone('phone', '8747179');

#4
SELECT * FROM person


CREATE OR REPLACE FUNCTION get_users_with_pagination(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, name VARCHAR, phone INT, gender CHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT person.id, person.name, person.phone, person.gender
    FROM person
    LIMIT p_limit
    OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;
SELECT * FROM get_users_with_pagination(2, 0);
SELECT * FROM get_users_with_pagination(2, 2);

