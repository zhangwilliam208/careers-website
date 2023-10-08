from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

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
  return render_template('home.html',jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
  jobs=load_jobs_from_db()
  return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
  job=load_job_from_db(id)
  if not job:
    return "Not Found", 404
  return render_template('jobpage.html',job=job) 
  
if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)