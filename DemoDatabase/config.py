import os
from pathlib import Path
import pyodbc

basedir = Path(__file__).resolve().parent

class Config:
    """Base configuration."""
    # Build ODBC connection string for pyodbc
    DATABASE_URI = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=localhost,1433;"
        "DATABASE=testdb;"
        "UID=sa;"
        "PWD=MyS3cure_;"
        "TrustServerCertificate=yes;"
    )

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
