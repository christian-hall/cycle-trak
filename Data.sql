DROP DATABASE IF EXISTS cycletrak;
CREATE DATABASE cycletrak;
USE cycletrak;

CREATE TABLE users(
	id				int				primary key auto_increment,
    name			varchar(50)		not null,
    password		varchar(10)		not null,
    birthdate		date			not null,
    sex				varchar(1)		not null,
    weight			decimal(4,1)	not null,
    height			int				not null,
    total_mileage	bigint			not null,
    
    CONSTRAINT unique_username UNIQUE(name)
);

CREATE TABLE cycles(
	id				int				primary key auto_increment,
    name			varchar(15)		not null,
    bike_type		varchar(20)		not null,
    year			int				not null,
    make			varchar(20)		not null,
    model			varchar(30)		not null,
    date_bought		date			not null,
    date_retired	date,
    odometer		bigint			not null,
    
    CONSTRAINT unique_cylename UNIQUE(name)
);

CREATE TABLE locations(
	id				int				primary key auto_increment,
    name			varchar(25)		not null,
    city			varchar(30)		not null,
    distance		int				not null,
    terrain			varchar(25 )		not null,
    notes			varchar(3000)	not null,
    
    CONSTRAINT unique_locationname UNIQUE(name)
);

CREATE TABLE rides(
	id				int				primary key auto_increment,
    name			varchar(50)		not null,
    cycle_id		int				not null,
    location_id		int				not null,
    datetime		datetime		not null,
    duration		bigint			not null,
    distance		decimal(6,2)	not null,
    
    FOREIGN KEY (cycle_id) REFERENCES cycles(id),
    FOREIGN KEY (location_id) REFERENCES locations(id)
);

INSERT INTO users (id, name, password, birthdate, sex, weight, height, total_mileage) VALUES
	(1, 'Christian Hall', 'June8th!', '1995-03-26', 'm', 197.6, 69, 29);

INSERT INTO cycles (id, name, bike_type, year, make, model, date_bought, odometer) VALUES
	(1, 'ESPORTA Bike', 'Stationary', '2015', 'Life-Fitness', 'C1 Upright', '2021-03-31', 29);

INSERT INTO locations (id, name, city, distance, terrain, notes) VALUES
	(1, 'ESPORTA Oakley', 'Cincinnati', 0, 'Stationary', 'Stationary bike at my local gym');

INSERT INTO rides (id, name, cycle_id, location_id, datetime, duration, distance) VALUES
	(1, 'Proving Ride 1', 1, 1, '2021-05-03 16:15:00', 3600, 14.7),
	(2, 'Proving Ride 2', 1, 1, '2021-05-05 16:15:00', 3600, 14.3);

DROP USER IF EXISTS ct_user@localhost;
CREATE USER ct_user@localhost IDENTIFIED BY 'sesame';
GRANT ALL ON cycletrak.* TO ct_user@localhost;