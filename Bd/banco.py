import mysql.connector
#import sys
#import boto3
#import os

ENDPOINT="database-1.ck0y7zcou9ly.us-east-1.rds.amazonaws.com"
PORT="3306"
USER="admin"
PASSWORD="Albert071421"
REGION="us-east-1b"
DBNAME="Certificados_Renato"
#os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'

#gets the credentials from .aws/credentials
#session = boto3.Session(profile_name='default')
#client = session.client('rds')

#token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USER, Region=REGION)

#ssl_ca='SSLCERTIFICATE'

try:
    conexao =  mysql.connector.connect(host=ENDPOINT, user=USER, passwd=PASSWORD, port=PORT, database=DBNAME)
    cursor = conexao.cursor()
    cursor.execute("""SELECT now()""")
    query_results = cursor.fetchall()
    print(query_results)
except Exception as e:
    print("Database connection failed due to {}".format(e))    

