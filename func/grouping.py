import re
from utils import *
from core_func import *

def computer_science(line):
	solution = []
	research_problem = []
	method = []
	
	connector_indexes = get_list_of_connector_indexes(line.lower(), connectors_rx)
	connector_indexes.sort()

	if len(connector_indexes) == 0:
		if not 'and' in line.lower():
			solution.append(line)
	elif len(connector_indexes) == 1:
		connector = get_info_exactly_one_connector(line.lower())

		if connector == None:
			return solution, research_problem, method
		
		i = line.lower().find(' '+connector+' ')
		subpart_0 = line[0:i]
		if 'attacks' in subpart_0:
			subpart_0 = "the"
		subpart_1 = line[i+len(' '+connector+' '):]
		
		if connector == 'using' or connector == 'with' or connector == 'via' or connector == 'by' or connector == 'through':
			if not non_content(subpart_0, subpart_0.lower()):
				if is_research_problem(subpart_0):
					research_problem.append(subpart_0)
				else:
					method.append(subpart_0)
					
			solution.append(subpart_1)
		else:
			if not non_content(subpart_0, subpart_0.lower()):
				solution.append(subpart_0)
				
			if is_research_problem(subpart_1):
				research_problem.append(subpart_1)
			else:
				method.append(subpart_1)
			
	return solution, research_problem, method
	