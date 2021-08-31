import re
from utils import *
from core_func import *

def computer_science(line):
	solution = []
	method = []
	
	connector_indexes = get_list_of_connector_indexes(line.lower(), connectors_rx)
	connector_indexes.sort()

	if len(connector_indexes) == 0:
		solution.append(line)
	elif ending(line.lower(), 'proofs') or ending(line.lower(), 'proof'):
		if len(connector_indexes) == 1:
			connector = get_info_exactly_one_connector(line.lower())

			if connector == None:
				return solution, method
			
			i = line.lower().find(' '+connector+' ')
			subpart_0 = line[0:i]
			subpart_1 = line[i+len(' '+connector+' '):]
			
			if connector == 'using' or connector == 'with' or connector == 'via' or connector == 'by' or connector == 'through':
				if not non_content(subpart_0, subpart_0.lower()):
					method.append(subpart_0)
				solution.append(subpart_1)
			else:
				if not non_content(subpart_0, subpart_0.lower()):
					solution.append(subpart_0)
				method.append(subpart_1)
	else:
		if len(connector_indexes) == 1:
			connector = get_info_exactly_one_connector(line.lower())

			if connector == None:
				return solution, method, dataset
			
			i = line.lower().find(' '+connector+' ')
			subpart_0 = line[0:i]
			subpart_1 = line[i+len(' '+connector+' '):]
			
			if connector == 'using' or connector == 'with' or connector == 'via' or connector == 'by' or connector == 'through':
				if not non_content(subpart_0, subpart_0.lower()):
					method.append(subpart_0)
				solution.append(subpart_1)
			else:
				if not non_content(subpart_0, subpart_0.lower()):
					solution.append(subpart_0)
				method.append(subpart_1)
		
	
	return solution, method
	