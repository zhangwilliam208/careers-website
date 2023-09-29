from flask import Flask, render_template, jsonify
app=Flask(__name__)
JOBS=[
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
   'salary':'$ 120,000'
  }
]
@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS,company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)