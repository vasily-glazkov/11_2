import json

data = []


def load_candidates(path):
	global data
	with open(path, encoding="utf-8") as file:
		data = json.load(file)
	return data


def get_candidate(uid):
	for item in data:
		if item["id"] == uid:
			return {
				'name': item['name'],
				'position': item['position'],
				'picture': item['picture'],
				'skills': item['skills'],
			}
	return {'not_found': 'No such entry'}


def get_candidates_by_name(name):
	found_candidates = []
	for item in data:
		if name.lower() in item['name'].lower():
			found_candidates.append(item)
	return found_candidates


def get_candidates_by_skill(skill):
	display_candidates = []
	for item in data:
		if skill.lower() in item['skills'].lower() or skill in item['skills']:
			display_candidates.append(item)
	return display_candidates
