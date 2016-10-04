import sqlite3


# connect to test.db, if it does not exist, create a database called test.db
# db is a sqlite databse that can respond to sql queries using the execute() function
db = sqlite3.connect('test.db')

# create a table called tt_table
db.execute('''create table tt_table
			(id int primary key not null,
			name text not null,
			sex text not null,
			age int not null);''')

test_data = [[1,"Isaac","M",27],[2,"Johanna","F",25],[3,"Jackjack","M",1]]

# populate the table with data
for i in test_data:
	db.execute('insert into tt_table values (?,?,?,?)', i)

# c will be a cursor to the result of the query. c is an iterable
c = db.execute("select * from tt_table where sex='M'")

# calling fetchall() on the cursor will load all the data out of the database into a list of results
results = c.fetchall()

print results