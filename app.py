from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app=Flask(__name__)
'''JOBS=[
  {'id':1,
   'title':'Data Analyst',
   'location':'Bangolulu',
   'salary':'Rs 100,000'
  },
  {'id':2,
   'title':'Data Scientist',
   'location':'Delhi',
   'salary':'Rs 150,000'
  },
  {'id':3,
   'title':'frontend engineer',
   'location':'remote'
   
  },
  {'id':4,
   'title':'backtend engineer',
   'location':'San Francisco USA',
   'salary':'$ 140,000'
  }
]
'''
@app.route("/")
def hello_world():
  jobs=load_jobs_from_db()
  return render_template('home.html',jobs=jobs,company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  jobs=load_jobs_from_db()
  return jsonify(jobs)
if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)