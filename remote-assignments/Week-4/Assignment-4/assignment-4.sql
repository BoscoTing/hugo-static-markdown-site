USE assignment;
CREATE TABLE article(
author VARCHAR(255), 
FOREIGN KEY (author) REFERENCES user(email), 
title TEXT NOT NULL,
content TEXT NOT NULL
);

SELECT email FROM user LIMIT 20;

USE assignment;
INSERT INTO article(author, title, content) VALUES 
("123@test99.com","K'Sante","This is K'Sante"),
("123@test99.com","HP","a champion with 4,700 HP"),
("123@test99.com","Armor","329 Armor,"),
("123@test99.com","MR","and 201 MR"),
("123@test99.com","Unstoppable","has Unstoppable"),
("1234@test7.com","Shield","a Shield"),
("1234@test7.com","Walls","and goes over walls"),
("1234@test7.com","Airborne","Has Airborne"),
("1234@test7.com","Cooldown","and the cooldown is only 1 second too"),
("1234@test7.com","Mana","It costs 15 Mana"),
("456@test5.com","Refreshed","The W CD is even refreshed when he transforms"),
("456@test5.com","Passive","He has true damage on his passive"),
("456@test5.com","Then","Then"),
("456@test5.com","Stacks","when he stacks Armor and MR"),
("456@test5.com","Haste","he gets Ability Haste too"),
("123@test7.com","Q","Ability Haste to his Q"),
("123@test7.com","Casting","and his spell casting speeds up"),
("123@test7.com","Then","Then"),
("123@test7.com","AD","he has an AD ratio"),
("123@test7.com","W","so his W"),
("123@test6.com","A","AAAAAAAAAAAAAAA"),
("123@test6.com","K'Sante","This is K'Sante"),
("123@test6.com","HP","a champion with 4,700 HP"),
("123@test6.com","Armor","329 Armor"),
("123@test6.com","MR","and 201 "),
("123@test5.com","Unstoppable","has Unstoppable"),
("123@test5.com","Shield","a Shield"),
("123@test5.com","Walls","and goes over walls"),
("123@test5.com","Airborne","Has Airborne"),
("123@test5.com","Cooldown","and the cooldown is only 1 second too");

-- 07/23 Add user_id column in article table.
-- ALTER TABLE article 
-- ADD COLUMN user_id INTEGER NOT NULL;

-- 07/23 Set user_id in article table as foreign key references to id in user table. 
-- SET FOREIGN_KEY_CHECKS=0;
-- ALTER TABLE article
-- ADD FOREIGN KEY (user_id) REFERENCES user(id);
-- SET FOREIGN_KEY_CHECKS=1;

-- 07/23 Update user_id to match the values of id in user table. 
-- UPDATE article ar, user u SET ar.user_id = u.id
-- WHERE ar.author = u.email;

-- 1. Write an SQL statement to select all articles with their author’s email. 
SELECT content FROM user u INNER JOIN (SELECT * FROM article) AS ar 
ON u.id = ar.user_id;

-- 2. Write another SQL statement to select articles from 7th to 12th sorted by id.
SELECT content, user_id FROM article
ORDER BY user_id ASC
LIMIT 6 OFFSET 6;
