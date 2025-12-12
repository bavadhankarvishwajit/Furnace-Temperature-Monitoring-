import pyodbc

try:
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost\\SQLEXPRESS;"  # change this later to your instance name
        "DATABASE=AdminDB;"
        "Trusted_Connection=yes;"        # OR use UID=sa;PWD=yourpassword;
    )
    print("✅ Connected successfully!")
except Exception as e:
    print("❌ Error:", e)
