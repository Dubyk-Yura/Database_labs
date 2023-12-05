USE lab4;

-- 2a
DROP PROCEDURE IF EXISTS insert_in_pet_type;
DELIMITER //
CREATE PROCEDURE insert_in_pet_type(
	IN new_type VARCHAR(255)
)
BEGIN
INSERT INTO pet_type(type) VALUES(new_type);
END//
DELIMITER ;

-- 2b
DROP PROCEDURE IF EXISTS insert_in_client_pet_by_values;
DELIMITER //
CREATE PROCEDURE insert_in_client_pet_by_values(
	IN client_name VARCHAR(45),
	IN client_surname VARCHAR(45),
    IN client_contact_number VARCHAR(13),
	IN pet_name VARCHAR(45),
	IN pet_age INT
)
BEGIN
	DECLARE client_id INT;
    DECLARE pet_id INT;
    
    SELECT id INTO client_id 
    FROM client 
    WHERE name = client_name AND surname = client_surname AND contact_number = client_contact_number;
    
    SELECT id INTO pet_id
    FROM pet
    WHERE name = pet_name AND age = pet_age;
    
    IF pet_id IS NUll THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'pet not founded';
	END IF;
    
	IF client_id IS NUll THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'client not founded';
	END IF;
	
    IF client_id AND pet_id IS NOT NULL THEN 
		INSERT INTO client_pet (client_Id, pet_id) 
        VALUES (client_id, pet_id);
	END IF;
END//
DELIMITER ;


-- 2c
DROP PROCEDURE IF EXISTS insert_ten_column_into_pet_type;
DELIMITER //
CREATE PROCEDURE insert_ten_column_into_pet_type()
BEGIN
    DECLARE iter INT DEFAULT 0;
    WHILE iter<= 9 DO
		INSERT INTO pet_type(type) VALUES (CONCAT('Noname',iter));
        SET iter = iter + 1;
	END WHILE;
END//
DELIMITER ;


-- 2d
DROP FUNCTION IF EXISTS get_statistics_from_procedures_price_F;
DROP PROCEDURE IF EXISTS get_statistics_from_procedures_price_P;

-- Function
DELIMITER //
CREATE FUNCTION get_statistics_from_procedures_price_F (
statistic_type VARCHAR(3)
)
RETURNS INT
DETERMINISTIC
BEGIN
	DECLARE result INT;
    IF statistic_type = 'Max' THEN 
		SELECT MAX(price) INTO result FROM procedures;
    ELSEIF statistic_type = 'Min' THEN 
		SELECT MIN(price) INTO result FROM procedures;
	ELSEIF statistic_type = 'Sum' THEN 
		SELECT SUM(price) INTO result FROM procedures;
	ELSEIF statistic_type = 'Avg' THEN 
		SELECT AVG(price) INTO result FROM procedures;
    ELSE
    SET result = NULL;
    END IF;
    RETURN result;
END //
DELIMITER ;

-- Procedure
DELIMITER //
CREATE PROCEDURE get_statistics_from_procedures_price_P (
statistic_type VARCHAR(3)
)
BEGIN
	DECLARE result INT;
    SET result = get_statistics_from_procedures_price_F(statistic_type);
	IF result IS NOT NULL THEN 
		SELECT CONCAT(statistic_type, ' in field price in procedures is -> ', result) as '';
	ELSE
		SELECT 'Invalid type' as '';
	END IF;
END //
DELIMITER ;


-- 2e iii
DROP PROCEDURE IF EXISTS convert_rows_in_databases;

DELIMITER //
CREATE PROCEDURE convert_rows_in_databases()
BEGIN
	DECLARE done INT DEFAULT false;
    DECLARE db_name VARCHAR(255);
    DECLARE cur CURSOR
    FOR SELECT status from status;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = true;
    OPEN cur;
myLoop: LOOP
	FETCH cur INTO db_name;
	IF done THEN
		LEAVE myLoop;
	END IF;
	
	SET @create_db_query = CONCAT('CREATE DATABASE IF NOT EXISTS ', db_name);
	PREPARE query_ FROM @create_db_query;
	EXECUTE query_;
	DEALLOCATE PREPARE query_;
	
    SET @num_tables = ROUND(RAND() * 9) + 1;
	SET @counter = 1;
    WHILE @counter <= @num_tables DO
		SET @table_name = CONCAT(db_name, '_', @counter);
		SET @create_table_query = CONCAT('CREATE TABLE ', db_name, '.', @table_name, ' (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))');
		PREPARE query_ FROM @create_table_query;
		EXECUTE query_;
		DEALLOCATE PREPARE query_;
        SET @counter = @counter + 1;
	END WHILE;

END LOOP;
	CLOSE cur;
END //

DELIMITER ;



