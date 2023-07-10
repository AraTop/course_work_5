CREATE TABLE vacancies (
   id SERIAL PRIMARY KEY,
   name VARCHAR(255),
   price INTEGER ,
   employment VARCHAR(255),
   alternate_url VARCHAR(255),
   requirement VARCHAR(255),
   experience VARCHAR(255),
   name_company VARCHAR(255)
);

INSERT INTO vacancies (name, price, employment, alternate_url, requirement, experience, name_company)
VALUES (%s, %s, %s, %s, %s, %s, %s);