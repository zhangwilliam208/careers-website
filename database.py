from sqlalchemy import create_engine, text
engine=create_engine("mysql+pymysql://william:Fcs!41254@localhost/joviancareers",)
with engine.connect() as conn:
  result=conn.execute(text("SELECT * FROM jobs"))
  print(result.all()) 