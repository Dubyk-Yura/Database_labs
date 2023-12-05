use lab4;

-- 1
DROP TRIGGER IF EXISTS check_pet_id;

DELIMITER //
CREATE TRIGGER check_pet_id
BEFORE INSERT ON pet
FOR EACH ROW
BEGIN
	DECLARE count_pet_id INT;
    SELECT COUNT(*) INTO count_pet_id
    FROM pet_type
    WHERE id = NEW.pet_type_id;
    
    IF count_pet_id = 0 THEN
		SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'This pet_type_id not exsist in pet type';
	END IF;
END//
DELIMITER ;

-- 3b
DROP TRIGGER IF EXISTS prevent_status_update;

DELIMITER //
CREATE TRIGGER prevent_status_update
BEFORE UPDATE ON status
FOR EACH ROW
BEGIN
	SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'It is forbidden to modify status table';
END//
DELIMITER ;

-- 3с
DROP TRIGGER IF EXISTS prevent_status_delete;

DELIMITER //
CREATE TRIGGER prevent_status_delete
BEFORE DELETE ON status
FOR EACH ROW
BEGIN
	SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'It is forbidden to delete row in status table';
END//
DELIMITER ;


-- 3 Створити таблицю-журнал, в якій вести логи зі штампом часу при ВСТАВЦІ даних у таблицю
DROP TRIGGER IF EXISTS log_insertion_in_status;

CREATE TABLE IF NOT EXISTS log_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    insert_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    log_text VARCHAR(255)
);

DELIMITER //

CREATE TRIGGER log_insertion_in_status
AFTER INSERT ON status
FOR EACH ROW
BEGIN
    INSERT INTO log_table (log_text) VALUES ('inserted data in status');
END//
DELIMITER ;