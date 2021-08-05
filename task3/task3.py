from jsonpath_ng.ext import parse
import json
from jsonpath_ng import jsonpath

vals = open("values.json", "r")
json_vals = json.load(vals)

jsp_expr1 = parse('$..id')

tests = open("tests.json", "r") 
json_tests = json.load(tests)

for match in jsp_expr1.find(json_vals):
    jsp_expr2 = parse("$..*[?(@.id==%d)].value" % match.value)

    for match2 in jsp_expr2.find(json_tests):
        val = jsp_expr2.find(json_vals)[0].value
        jsp_expr2.update(json_tests, val)

print(json.dumps(json_tests, indent=2))
report = open("report.json", "w")
report.write(json.dumps(json_tests, indent=2))
report.close()