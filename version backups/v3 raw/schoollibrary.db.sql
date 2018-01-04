BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `users` (
	`id`	INTEGER NOT NULL,
	`name`	text,
	`type`	TEXT CHECK(type = "student" or type = "staff"),
	PRIMARY KEY(`id`)
);
INSERT INTO `users` VALUES (1,'Karthik','staff');
INSERT INTO `users` VALUES (2,'Carter','student');
INSERT INTO `users` VALUES (3,'John','student');
CREATE TABLE IF NOT EXISTS `loans` (
	`book_id`	INTEGER UNIQUE,
	`user_id`	INTEGER,
	`expiration_date`	DATETIME,
	FOREIGN KEY(`user_id`) REFERENCES `users`(`id`),
	PRIMARY KEY(`book_id`,`user_id`),
	FOREIGN KEY(`book_id`) REFERENCES `books`(`id`)
);
INSERT INTO `loans` VALUES (2,1,NULL);
CREATE TABLE IF NOT EXISTS `books` (
	`id`	INTEGER NOT NULL,
	`title`	TEXT,
	`author`	text,
	`schoolID`	INTEGER,
	PRIMARY KEY(`id`)
);
INSERT INTO `books` VALUES (1,'Catcher in the Rye','J. D. Salinger',1);
INSERT INTO `books` VALUES (2,'Don Quixote','Miguel de Cervantes',1);
COMMIT;
