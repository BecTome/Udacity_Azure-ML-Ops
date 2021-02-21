import request

uri = ''
key = ''

data = [{'age':[57], 'job':['technician'], 'marital':['married'], 
	'education':['high.school'], ....}]
header = {'auth':key}
req = request.post(uri, data, header=header)
