dialect = 'oracle' # can be MySQL or MSSQL
sql_driver = 'cx_oracle'
db_host = '127.0.0.1' # change for ip of db server
db_port = '1521' # change for diff db server
service_name = 'xe' # change according to the service
user = 'admin'
pwd = 'password'
instant_client_lib = 'instantclient_18_5'

sqlalchemy_database_uri = f'{dialect}+{sql_driver}://{user}:{pwd}@{db_host}:{db_port}/?service_name={service_name}'

api_prefix = '/api/v1.0'
api_port = '2525'
api_host = '0.0.0.0'