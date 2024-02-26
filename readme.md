-- CREATE OR REPLACE FUNCTION trigger_set_timestamp()
-- RETURNS TRIGGER AS $$
-- BEGIN
--   NEW.updated_at = NOW();
--   RETURN NEW;
-- END;
-- $$ LANGUAGE plpgsql;


-- CREATE TRIGGER set_timestamp
-- BEFORE UPDATE ON priorities
-- FOR EACH ROW
-- EXECUTE PROCEDURE trigger_set_timestamp();

-- INSERT INTO priorities (priority, is_active) 
-- VALUES ('p2', True) RETURNING *;

select * from priorities