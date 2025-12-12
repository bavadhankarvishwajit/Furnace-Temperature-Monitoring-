# generate_api_key.py
"""
Generate an API key, hash it with pbkdf2_sha256 (passlib), store hash in ApiKeys table,
and print the raw key once for provisioning devices/apps.
"""

import secrets
import pyodbc
from passlib.context import CryptContext
from datetime import datetime, timedelta
import argparse

DB_CONN = (
    r"DRIVER={ODBC Driver 17 for SQL Server};"
    r"SERVER=localhost\SQLEXPRESS;"
    r"DATABASE=AdminDB;"
    r"Trusted_Connection=yes;"
)

# Use pbkdf2_sha256 to avoid bcrypt platform issues and the 72-byte limit.
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def create_api_key(owner="esp32_device", notes=None, expires_days=None):
    raw_key = secrets.token_urlsafe(32)   # ~43 chars strong key
    key_hash = pwd_context.hash(raw_key)
    expires_at = None
    if expires_days is not None:
        expires_at = datetime.utcnow() + timedelta(days=expires_days)

    conn = pyodbc.connect(DB_CONN)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO ApiKeys (KeyHash, Owner, IsEnabled, CreatedAt, ExpiresAt, Notes)
        VALUES (?, ?, 1, SYSUTCDATETIME(), ?, ?)
    """, (key_hash, owner, expires_at, notes))
    conn.commit()

    # ✅ MODIFIED LINES 36-39: safer fetch of inserted row ID
    cur.execute("SELECT CAST(SCOPE_IDENTITY() AS INT)")
    row = cur.fetchone()
    kid = row[0] if row and row[0] is not None else 0

    cur.close()
    conn.close()
    return raw_key, kid

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--owner", default="esp32_device")
    parser.add_argument("--notes", default=None)
    parser.add_argument("--expires-days", type=int, default=None)
    args = parser.parse_args()

    key, kid = create_api_key(owner=args.owner, notes=args.notes, expires_days=args.expires_days)
    print("\n======================== IMPORTANT ========================")
    print("API KEY (copy this now - it will NOT be stored in DB):")
    print(key)
    print("API KEY ID (DB id):", kid)
    print("==========================================================\n")
