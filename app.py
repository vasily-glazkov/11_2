from flask import Flask, render_template
from utils import load_candidates, get_candidate, get_candidates_by_name, get_candidates_by_skill
from config import PATH

app = Flask(__name__)
data = load_candidates(PATH)


@app.route("/")
def index_page():
	return render_template("list.html", items=data)


@app.route('/candidate/<int:uid>/')
def candidate_page(uid):
	candidate = get_candidate(uid)
	return render_template('candidate.html', candidate=candidate)


@app.route('/search/<name>/')
def search_page(name):
	candidates = get_candidates_by_name(name)
	return render_template('search.html', candidates=candidates, candidates_len=len(candidates))


@app.route('/skill/<skill_name>/')
def skills_page(skill_name):
	candidates = get_candidates_by_skill(skill_name)
	return render_template('skill.html', candidates=candidates, candidates_len=len(candidates),
						   skill=skill_name.lower())


if __name__ == '__main__':
	app.run()
