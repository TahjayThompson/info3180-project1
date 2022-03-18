import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgres://grqwpjpalentrk:0487412fd797ac0cee8f25370ac4a8beacc097fd3f01237919445b014e5575cf@ec2-3-222-204-187.compute-1.amazonaws.com:5432/d41foksp1efhqe').replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlch
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', './uploads')