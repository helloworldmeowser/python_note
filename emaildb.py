import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Drop the table if it exists and create a new table
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

# Prompt for a file name
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'

# Open the file
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    row = cur.fetchone()
    if row is None:
        # Insert a new record for the email with a count of 1
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
    else:
        # Update the count for an existing record
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))

# Commit the transaction
conn.commit()

# Query and display the top 10 email addresses by count
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# Close the cursor and connection
cur.close()
conn.close()

