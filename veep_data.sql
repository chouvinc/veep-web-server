CREATE TABLE veep_execs {
	id INTEGER
	username TEXT
	email TEXT
	role TEXT
	year TEXT
	program TEXT
};

CREATE TABLE veep_projects{
	id TEXT
	project_name TEXT
	notforprofit TEXT
	project_description TEXT
	memberlimit TEXT
}

CREATE TABLE veep_clients {
	id TEXT
	username TEXT
	email TEXT
	display_name TEXT
	not_for_profit TEXT
}

INSERT INTO veep_execs (
	id,
	username,
	email,
	role,
	year,
	program
)
VALUES 
	("1","anourimand","arash.nourimand@mail.utoronto.ca", "Executive Director 1", "3", "Mech")
	("2","vchou","po.chou@mail.utoronto.ca","Operations Director","3","Mech")
