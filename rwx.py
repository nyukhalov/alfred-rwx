'''
RWX v0.1

Github: https://github.com/???
Author: Roman Niukhalov
'''

ex = {
	0: "---",
	1: "--x",
	2: "-w-",
	3: "-wx",
	4: "r--",
	5: "r-x",
	6: "rw-",
	7: "rwx",
}

roles = {
	0: "owner",
	1: "group",
	2: "other"
}

bad_format_msg = "Type one to three digits each in the range [0..7]"

query = '{query}'
query = query.lower()

title = ""
explanation = ""

valid = True

if len(query) > 3:
	valid = False
else:
	exp_parts = []
	for idx, x in enumerate(query):
		num = ord(x) - ord('0')
		if num < 0 or num > 7:
			valid = False
			break
		exp_parts.append("{0}: {1}".format(roles[idx], ex[num]))
		title += ex[num]
	explanation = ", ".join(exp_parts)

if not valid:
	title = bad_format_msg
	explanation = ""

json = """{{"items": [
	{{
		"uid": "result",
		"title": "{0}",
		"subtitle": "{1}"
	}}
]}}""".format(title, explanation)

print json
