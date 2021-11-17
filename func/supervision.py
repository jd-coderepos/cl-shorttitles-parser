import re
from utils import *
from core_func import *

def computer_science(line):
	solution = []
	research_problem = []
	resource = []
	language = []
	tool = []
	method = []
	dataset = []
	
	connector_indexes = get_list_of_connector_indexes(line.lower(), connectors_rx)
	connector_indexes.sort()
	
	if len(connector_indexes) == 0:
		if is_tool(line):
			solution.append(line)
		elif is_method(line):
			solution.append(line)
	elif len(connector_indexes) == 1:
		connector = get_info_exactly_one_connector(line.lower())
		
		if connector == None:
			return solution, research_problem, resource, language, tool, method, dataset
		
		i = line.lower().find(' '+connector+' ')
		subpart_0 = line[0:i]
		subpart_1 = line[i+len(' '+connector+' '):]
		
		if connector == 'by' or connector == 'via':
			if not non_content(subpart_0, subpart_0.lower()):
				if is_dataset(subpart_0):
					dataset.append(subpart_0)
				elif is_method(subpart_0):
					method.append(subpart_0)	
				elif is_research_problem(subpart_0):
					research_problem.append(subpart_0)
			solution.append(subpart_1)
		elif connector == 'using' or connector == 'with' or connector == 'through':
			if not non_content(subpart_0, subpart_0.lower()):
				if is_dataset(subpart_0):
					dataset.append(subpart_0)			
				elif is_method(subpart_0):
					method.append(subpart_0)
				elif is_research_problem(subpart_0):
					research_problem.append(subpart_0)
			language, data, tool, meth, resource, rp = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_1)
			
			if len(data) > 0:
				dataset.append(data[0])
			elif len(meth) > 0:
				method.append(meth[0])
			elif len(rp) > 0:
				research_problem.append(rp[0])
		elif len(subpart_0.split(' ')) == 2:
			tokens = subpart_0.split(' ')
			if not non_content(subpart_0, subpart_0.lower()):
				if is_dataset(subpart_0):
					dataset.append(subpart_0)			
				elif is_method(subpart_0):
					method.append(subpart_0)
				elif is_research_problem(subpart_0):
					research_problem.append(subpart_0)
			language, tool, data, rp, meth, resource = language_or_tool_or_dataset_or_rp_or_method_or_resource(subpart_1)
			
			if len(tool) > 0:
				solution.append(tool[0])
				tool = []
			elif len(data) > 0:
				dataset.append(data[0])
			elif len(meth) > 0:
				method.append(meth[0])
			elif len(rp) > 0:
				research_problem.append(rp[0])
		else:
			if not non_content(subpart_0, subpart_0.lower()):
				solution.append(subpart_0)
			language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_1)
		
	return solution, research_problem, resource, language, tool, method, dataset
	