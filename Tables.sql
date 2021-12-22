-- https://en.rakko.tools/tools/36/ - sqlchecker



CREATE TABLE Risks(
id int AUTO_INCREMENT NOT NULL , 
rid varchar(12) NOT NULL,
Risk_Description MEDIUMTEXT NOT NULL, 
RiskLevel INT, 
Owner varchar(50),
Next_Review DATETIME DEFAULT CURRENT_TIMESTAMP,
Last_Review DATE,
Review_Frequency varchar(23) NOT NULL,
RiskArea varchar(250) NOT NULL ,
Man_Ctrs varchar(5000),
Impact INT(2) NOT NULL , 
Likelihood INT(2) NOT NULL , 
Archive TINYINT(2) Default 0, 
Category TINYINT(2) NOT NULL,
PRIMARY KEY (ID) 
);

CREATE TABLE Category(
cid int NOT NULL ,
category varchar(50) NOT NULL,
PRIMARY KEY (cid)
);


CREATE TABLE impact(
iid int NOT NULL ,
impact varchar(15) NOT NULL,
PRIMARY KEY (iid)
);
CREATE TABLE likelihood(
lid int NOT NULL ,
likelihood varchar(15) NOT NULL,
PRIMARY KEY (lid)
);
CREATE TABLE risklevel(
rlid int NOT NULL ,
risklevel varchar(15) NOT NULL

);

-- insert data into lookup tables https://www.mysqltutorial.org/mysql-insert-multiple-rows/
INSERT INTO Category (cid, category)
VALUES(1, 'Business Continuity'),
(2, 'Contractual'),
(3, 'Financial'),
(4, 'Legal'),
(5, 'Legislative/Regulatory'),
(6, 'Physical(SH&W, built enviroment'),
(7, 'Professional'),
(8, 'social'),
(9, 'Student/Trainee/Adult Learner');

INSERT INTO impact(iid,impact) 
VALUES
(1, 'Minor'),
(2, 'Moderate'),
(3, 'Major'),
(4, 'Severe');

INSERT INTO likelihood(lid,likelihood) 
VALUES
(1, 'Low'),
(2, 'Medium'),
(3, 'High'),
(4, 'Very High');
