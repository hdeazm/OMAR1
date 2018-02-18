import web

db_host = 'cdm1s48crk8itlnr.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'lqj6xaxowmsh28df'
db_user = 'qbcje16tzu3v6ux4'
db_pw = 'pqpgvzp9rtng73ca'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )