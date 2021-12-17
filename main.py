from wwr import get_jobs as wwr_get_jobs
from stackoverflow import get_jobs as so_get_jobs
from remoteok import get_jobs as remote_get_jobs
from flask import Flask, render_template, request, redirect, send_file

app = Flask("jobScrapper")
db = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report")
def report():

    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = db[word]
        else:
            jobs = wwr_get_jobs(word) + so_get_jobs(word) + remote_get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template("report.html",
                           searchingBy=word,
                           resultsNumber=len(jobs),
                           jobs=jobs)


app.run(host="0.0.0.0")