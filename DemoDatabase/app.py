from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
import pyodbc
import locale

# Set locale for number formatting with thousand separators
locale.setlocale(locale.LC_ALL, '')

load_dotenv()

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Custom filter for formatting numbers with thousand separators
@app.template_filter('format_number')
def format_number(value):
    try:
        return f"{int(value):,}"
    except (ValueError, TypeError):
        return value

# Fetch connection string from config
connection_string = app.config['DATABASE_URI']


@app.route('/')
def home():
    """Fetch products from the database and render the index page."""
    try:
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            # Join Products with Categories to get category names
            cursor.execute("""
                SELECT p.ProductName, c.CategoryName, p.UnitsInStock, p.UnitPrice 
                FROM Products p
                LEFT JOIN Categories c ON p.CategoryID = c.CategoryID
            """)
            products = cursor.fetchall()
            # Convert to list of dictionaries
            product_list = [{'ProductName': row[0], 'CategoryName': row[1], 'UnitsInStock': row[2], 'UnitPrice': row[3]} for row in products]
            return render_template('index.html', products=product_list)
    except Exception as e:
        return render_template('index.html', products=[], error=str(e))


@app.route('/dbtest')
def dbtest():
    """Attempt a simple query to verify DB connectivity using pyodbc."""
    try:
        # Connect to the database using pyodbc
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            return jsonify({'ok': True, 'result': result[0]})
    except Exception as e:
        return jsonify({'ok': False, 'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)