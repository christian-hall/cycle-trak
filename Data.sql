DROP DATABASE IF EXISTS cycletrak;
CREATE DATABASE cycletrak;
USE cycletrak;

CREATE TABLE user(
	id				int				not null auto_increment,
    name			varchar(50)		not null,
    password		varchar(10)		not null,
    birthdate		date			not null,
    sex				varchar(1)		not null,
    weight			decimal			not null,
    height			int				not null,
    total_mileage	bigint			not null,
    
    CONSTRAINT unique_username UNIQUE(name)
);

CREATE TABLE cycle(
	id				int				not null auto_increment,
    name			varchar(15)		not null,
    bike_type		varchar(20)		not null,
    year			bigint			not null,
    make			varchar(20)		not null,
    model			varchar(30)		not null,
    date_bought		date			not null,
    date_retired	date,
    odometer		bigint			not null
);