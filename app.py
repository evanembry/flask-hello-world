from flask import Flask
import psycopg2

app = Flask(__name__)

# 1) HOME ROUTE
@app.route('/')
def index():
    
    return "Hello World from Evan Embry in 3308!"

# 2) DB TEST
@app.route('/db_test')
def db_test():
    try:
        conn = psycopg2.connect("postgresql://my_flask_db_8hvx_user:JokHVuSOwBweWCTTHCLuRR0sHges97pk@dpg-cvmabqje5dus73entpeg-a/my_flask_db_8hvx")
        conn.close()
        return "Database connection works!"
    except Exception as e:
        return f"Error connecting to DB: {e}"

# 3) DB CREATE (Creates the 'Basketball' table)
@app.route('/db_create')
def db_create():
    try:
        conn = psycopg2.connect("postgresql://my_flask_db_8hvx_user:JokHVuSOwBweWCTTHCLuRR0sHges97pk@dpg-cvmabqje5dus73entpeg-a/my_flask_db_8hvx")
        cur = conn.cursor()
        
        # Create table if not exists
        cur.execute('''
            CREATE TABLE IF NOT EXISTS Basketball(
                First VARCHAR(255),
                Last VARCHAR(255),
                City VARCHAR(255),
                Name VARCHAR(255),
                Number INT
            );
        ''')
        
        conn.commit()
        conn.close()
        
        return "Basketball table created successfully!"
    except Exception as e:
        return f"Error creating table: {e}"

# 4) DB INSERT (Inserts rows into the 'Basketball' table)
@app.route('/db_insert')
def db_insert():
    try:
        conn = psycopg2.connect("postgresql://my_flask_db_8hvx_user:JokHVuSOwBweWCTTHCLuRR0sHges97pk@dpg-cvmabqje5dus73entpeg-a/my_flask_db_8hvx")
        cur = conn.cursor()
        
        # Insert data
        cur.execute('''
            INSERT INTO Basketball (First, Last, City, Name, Number)
            VALUES
            ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
            ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
            ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
            ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
        
        conn.commit()
        conn.close()
        
        return "Basketball Table Populated"
    except Exception as e:
        return f"Error inserting data: {e}"

# 5) DB SELECT (Selects all rows from 'Basketball', returns as HTML table)
@app.route('/db_select')
def db_select():
    try:
        conn = psycopg2.connect("postgresql://my_flask_db_8hvx_user:JokHVuSOwBweWCTTHCLuRR0sHges97pk@dpg-cvmabqje5dus73entpeg-a/my_flask_db_8hvx")
        cur = conn.cursor()
        
        # Query data
        cur.execute("SELECT * FROM Basketball;")
        records = cur.fetchall()
        
        conn.close()
        
        # Build an HTML table from records
        html = "<h2>Basketball Table Data:</h2>"
        html += "<table border='1'>"
        html += "<tr><th>First</th><th>Last</th><th>City</th><th>Name</th><th>Number</th></tr>"
        
        for row in records:
            html += "<tr>"
            for col in row:
                html += f"<td>{col}</td>"
            html += "</tr>"
        
        html += "</table>"
        
        return html
    except Exception as e:
        return f"Error selecting data: {e}"

# 6) DB DROP (Drops the 'Basketball' table)
@app.route('/db_drop')
def db_drop():
    try:
        conn = psycopg2.connect("postgresql://my_flask_db_8hvx_user:JokHVuSOwBweWCTTHCLuRR0sHges97pk@dpg-cvmabqje5dus73entpeg-a/my_flask_db_8hvx")
        cur = conn.cursor()
        
        cur.execute("DROP TABLE Basketball;")
        
        conn.commit()
        conn.close()
        
        return "Basketball Table Dropped"
    except Exception as e:
        return f"Error dropping table: {e}"

# Required for gunicorn to run
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
