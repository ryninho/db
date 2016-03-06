import psycopg2 as pg
import pandas as pd
import pandas.io.sql as psql
import urlparse
import imp
import os
from sqlalchemy import create_engine

config = imp.load_source('config', os.path.realpath(os.path.join(os.path.dirname(__file__), './config.py')))

class Db(object):

  def __init__(self, db_url=config.db_url[config.env]):
    db_parsed = urlparse.urlparse(db_url)
    self.conn = pg.connect(database=db_parsed.path[1:],
      user=db_parsed.username,
      password = db_parsed.password,
      host = db_parsed.hostname,
      port=db_parsed.port)
    self.conn.autocommit = True
    self.engine = create_engine(db_url)

  def to_dataframe(self,query,**kwargs):
    filename = kwargs.pop("filename",__file__)
    query = (""" /*data-science/%s*/ """ % filename) + query
    df = psql.read_sql(sql=query, con=self.conn,**kwargs)
    self.conn.commit()
    return df

  def to_sql(self,table,df):
    df.to_sql(table,self.engine,if_exists="append",index=False)

  def close(self):
    self.conn.close()

