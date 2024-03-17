#!/usr/bin/python3

"""
Write a script that lists all states from the database hbtn_0e_0_usa.
"""

if __name__ == "__main__":
    
    import MySQLdb
    import sys
    try:
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]