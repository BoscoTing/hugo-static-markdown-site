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

-- 1. Write an SQL statement to select all articles with their author’s email. 
SELECT content FROM user INNER JOIN (SELECT * FROM article) AS ar 
ON email = ar.author;

-- 2. Write another SQL statement to select articles from 7th to 12th sorted by id.
SELECT content, id FROM article INNER JOIN (SELECT * FROM user) u 
ON u.email = author 
ORDER BY id ASC
LIMIT 5 OFFSET 6;

-- SELECT * FROM article ar
-- INNER JOIN user u on ar.author = u.email
-- ORDER BY id ASC
-- LIMIT 5 OFFSET 6;
