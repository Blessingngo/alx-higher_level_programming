--creates the MySQL server user user_0d_1 with all the privileges
CREATE USER
	IF NOT EXISTS user_0d_1@localhost
	IDENTIFIED BY 'user_0d_1_pwd';
GRANTS ALL PRIVILEGES
	ON *.*
	TO user_0d_1@localhost
