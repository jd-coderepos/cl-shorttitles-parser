import re
from utils import *

def no_connector_heuristics(phrase):
	research_problem = []
	resource = []
	language = []
	tool = []
	method = []
	dataset = []
	
	if ':' in phrase:
		phrase = phrase[0:phrase.find(':')]
	language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(phrase)
	return language, dataset, tool, method, resource, research_problem

def one_connector_heuristics_postprocess_toward(solution, research_problem, resource, language, tool, dataset):
	if len(solution) == 1 and not has_specialcase(solution[0]):
		if is_research_problem(solution[0]):
			research_problem.append(solution[0])
			solution = []
		else:
			lang, data, t, res = language_or_dataset_or_tool_or_resource(solution[0])
			if len(lang) == 1 or len(data) == 1 or len(t) == 1 or len(res) == 1:
				solution = []
			language, dataset, tool, resource = extend_lists(language, lang, dataset, data, tool, t, resource, res)
	return solution, research_problem, resource, language, tool, dataset
	
def one_connector_heuristics_postprocess(solution, research_problem, resource, language, tool, method, dataset):
	#Where in the heuristcs for 'NAME: title' pattern, the beginning of the phrase was often a solution
	#in Using patterns, the beginning of the phrase may be a resource or a tool or a method
	#thus after processing the line using the 'NAME: title' pattern heuristics, we change the result
	#so we check if the solution is a tool or a language or a method or a resource
	if len(solution) == 1 and (not has_specialcase(solution[0]) or ' ' in solution[0]):
		lang, data, t, meth, res = language_or_dataset_or_tool_or_method_or_resource(solution[0])
		if len(lang) == 1 or len(data) == 1 or len(t) == 1 or len(meth) == 1 or len(res) == 1:
			solution = []
		language, dataset, tool, method, resource = extend_lists_five(language, lang, dataset, data, tool, t, method, meth, resource, res)
	return solution, research_problem, resource, language, tool, method, dataset

	
def one_connector_heuristics_titled_solution(part_1, part_1_lower):
	solution = []
	research_problem = []
	resource = []
	language = []
	tool = []
	method = []
	dataset = []

	#solution: [solution] for [research problem]
	if contains_one_connector(part_1_lower, 'for', non_for_connectors_rx):
		solution, research_problem, resource, language, tool, method, dataset = for_connector(part_1)	
	elif contains_one_connector(part_1_lower, 'of', non_of_connectors_rx):
		solution, research_problem, resource, language, tool, dataset, method = of_connector(part_1)		
	elif contains_one_connector(part_1_lower, 'using', non_using_connectors_rx) or \
	contains_one_connector(part_1_lower, 'with', non_with_connectors_rx):
		solution, resource, language, tool, method, dataset, research_problem = using_with_connector(part_1)
	elif contains_one_connector(part_1_lower, 'by', non_by_connectors_rx):
		solution, resource, language, tool, method, dataset, research_problem = by_connector(part_1)		
	elif contains_one_connector(part_1_lower, 'on', non_on_connectors_rx):
		solution, research_problem, resource, language, tool, dataset, method = on_connector(part_1)		
	elif contains_one_connector(part_1_lower, 'from', non_from_connectors_rx):
		solution, language, dataset, tool, method, resource, research_problem = from_connector(part_1)		
	elif contains_one_connector(part_1_lower, 'in', non_in_connectors_rx):
		resource, research_problem, solution, language, tool, method, dataset = in_connector(part_1)		
	elif contains_one_connector(part_1_lower, 'through', non_through_connectors_rx) or \
	contains_one_connector(part_1_lower, 'via', non_via_connectors_rx):
		solution, research_problem, method, tool, resource, language, dataset = through_via_connector(part_1)		
	elif contains_one_connector(part_1_lower, 'to', non_to_connectors_rx):
		if 'applied to' in part_1_lower:
			tool, solution, research_problem, resource, language, dataset, method = applied_to_connector(part_1)
		else:
			resource, research_problem, solution, language, tool, method, dataset = to_connector(part_1)
	elif contains_one_connector(part_1_lower, 'as', non_as_connectors_rx):
		resource, research_problem, solution, method, language, dataset, tool = as_connector(part_1)
	elif contains_one_connector(part_1_lower, 'at', non_at_connectors_rx):
		solution, research_problem, resource = at_connector(part_1)
	elif contains_one_connector(part_1_lower, 'over', non_over_connectors_rx) or \
	contains_one_connector(part_1_lower, 'under', non_under_connectors_rx):
		solution, research_problem, resource, language, tool, method = under_over_connector(part_1)
	elif contains_one_connector(part_1_lower, 'including', non_including_connectors_rx) or \
	contains_one_connector(part_1_lower, 'involving', non_involving_connectors_rx):
		solution, resource, language, tool, method, dataset, research_problem = involving_including_connector(part_1)
	elif contains_one_connector(part_1_lower, 'across', non_across_connectors_rx):
		#Learning-to-Match Keypoints Across 2D Image and 3D Point Cloud
		#Integrating Power Budget and Resource Management across a Virtualized Server Cluster
		solution, research_problem, dataset, tool, resource, language, method = across_connector(part_1)
	elif contains_one_connector(part_1_lower, 'against', non_against_connectors_rx):
		solution, method = against_connector(part_1)
	elif contains_one_connector(part_1_lower, 'within', non_within_connectors_rx):
		solution, dataset, tool, resource, method, language, research_problem = within_connector(part_1)
	elif contains_one_connector(part_1_lower, 'representing', non_representing_connectors_rx):
		solution, resource = representing_connector(part_1)
	elif contains_one_connector(part_1_lower, 'towards', non_towards_connectors_rx):
		solution, research_problem = towards_connector(part_1)
	elif contains_one_connector(part_1_lower, 'between', non_between_connectors_rx):
		solution, resource, language, tool, method, dataset = between_connector(part_1)
		
	return solution, research_problem, resource, language, tool, method, dataset

def and_heuristics(phrase):
	language = []
	dataset = []	
	tool = []
	method = []
	resource = []	
	research_problem = []
	
	phrase = phrase.replace(' And ', ' and ').replace(' AND ', ' and ')
	subparts = phrase.split(' and ')
	subparts[0] = subparts[0].strip()
	subparts[1] = subparts[1].lstrip().strip()
			
	if (' ' not in subparts[0] and ' ' in subparts[1]) or (' ' in subparts[0] and ' ' not in subparts[1]):
		language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(phrase)
	else:
		language, dataset, tool, method, resource = language_or_dataset_or_tool_or_method_or_resource(subparts[1])
		if len(language) > 0:
			language.append(subparts[0])
		elif len(dataset) > 0:
			dataset.append(subparts[0])
		elif len(tool) > 0:
			tool.append(subparts[0])
		elif len(method) > 0:
			method.append(subparts[0])
		elif len(resource) > 0:
			resource.append(subparts[0])
		elif len(research_problem) > 0:
			research_problem.append(subparts[0])
			
	return language, dataset, tool, method, resource, research_problem
	
def between_connector(phrase):	
	solution = []
	resource = []
	language = []
	tool = []
	method = []
	dataset = []
	research_problem = []

	phrase = phrase.replace(' Between ', ' between ').replace(' BETWEEN ', ' between ')
	i = phrase.find(' between ')
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' between '):]
		
	if ' and ' in subparts_1:
		if ' ' in subparts_0 and len(subparts_0.split(' ')) > 2:
		
			if is_method(subparts_0.lower()) or is_tool(subparts_0) or is_resource(subparts_0.lower()):
				solution.append(subparts_0)

		language, dataset, tool, method, resource, research_problem = and_heuristics(subparts_1)	
	else:
		language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subparts_1)
		
		if not(determiner_start(subparts_0.lower()) and len(subparts_0.split(' ')) == 2) and not non_content(subparts_0, subparts_0.lower()):
			lang, data, t, meth, res, rp = language_or_dataset_or_tool_or_method_or_resource_or_rp(subparts_0)
			language, dataset, tool, method, resource, research_problem = extend_lists_all(language, lang, dataset, data, tool, t, method, meth, resource, res, research_problem, rp)
		
	return solution, resource, language, tool, method, dataset
	
def towards_connector(phrase):
	solution = []
	research_problem = []

	phrase = phrase.replace(' Towards ', ' towards ').replace(' TOWARDS ', ' towards ')
	i = phrase.find(' towards ')

	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' towards '):]	
	
	solution.append(subparts_0)
	research_problem.append(subparts_1)
	
	return solution, research_problem
	
def representing_connector(phrase):
	solution = []
	resource = []

	phrase = phrase.replace(' Representing ', ' representing ').replace(' REPRESENTING ', ' representing ')
	i = phrase.find(' representing ')	
	
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' representing '):]	

	if is_tool(subparts_0) or is_method(subparts_0.lower()) or is_resource(subparts_0.lower()):
		solution.append(subparts_0)
	
	if is_resource(subparts_1):
		resource.append(subparts_1)
	
	return solution, resource
	
def within_connector(phrase):
	solution = []
	dataset = []
	tool = []
	resources = []
	method = []
	language = []
	research_problem = []
	
	phrase = phrase.replace(' Within ', ' within ').replace(' WITHIN ', ' within ')
	i = phrase.find(' within ')
	
	subparts_0 = phrase[0:i]

	if is_tool(subparts_0) or is_resource(subparts_0.lower()):
		solution.append(subparts_0)
	elif ' ' in subparts_0 and is_method(subparts_0.lower()):
		solution.append(subparts_0)
	
	subparts_1 = phrase[i+len(' within '):]	
	
	if ' and ' in subparts_1:
		language, dataset, tool, method, resources, research_problem = and_heuristics(subparts_1)
	else:
		if is_dataset(subparts_1.lower()):
			dataset.append(subparts_1)
		elif is_tool(subparts_1):
			tool.append(subparts_1)
		elif is_resource(subparts_1.lower()):
			resources.append(subparts_1)
		elif is_method(subparts_1.lower()):
			method.append(subparts_1)
	
	return solution, dataset, tool, resources, method, language, research_problem
	
def against_connector(phrase):
	solution = []
	method = []
	
	phrase = phrase.replace(' Against ', ' against ').replace(' AGAINST ', ' against ')
	i = phrase.find(' against ')
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' against '):]	
	
	if ' ' in subparts_0 and is_method(subparts_0):
		solution.append(subparts_0)
	else:
		solution.append(subparts_0)
		
	if is_method(subparts_1):
		method.append(subparts_1)
	
	return solution, method
	
def across_connector(phrase):
	solution = []
	research_problem = []
	dataset = []
	tool = []
	resources = []
	language = []
	method = []

	phrase = phrase.replace(' Across ', ' across ').replace(' ACROSS ', ' across ')
	i = phrase.find(' across ')
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' across '):]

	if not non_content(subparts_0, subparts_0.lower()):
		if is_tool(subparts_0):
			solution.append(subparts_0)	
		elif ' ' in subparts_0 and is_method(subparts_0):
			solution.append(subparts_0)
		elif is_research_problem(subparts_0):
			research_problem.append(subparts_0)
		elif not is_method(subparts_0):
			subparts_0 = remove_and_ending(subparts_0)
			solution.append(subparts_0)
	
	if ' and ' in subparts_1.lower():
		language, dataset, tool, method, resources, research_problem = and_heuristics(subparts_1)
	else:
		if not ending(subparts_1.lower(), 'ion(s)?'):
			if is_dataset(subparts_1.lower()):
				dataset.append(subparts_1)
			elif is_tool(subparts_1):
				tool.append(subparts_1)
			elif is_resource(subparts_1.lower()):
				resources.append(subparts_1)
	
	return solution, research_problem, dataset, tool, resources, language, method
	
def at_connector(phrase):
	solution = []
	research_problem = []
	resource = []
	
	phrase = phrase.replace(' At ', ' at ').replace(' AT ', ' at ')
	i = phrase.find(' at ')
	subparts_0 = phrase[0:i]

	if not non_content(subparts_0, subparts_0.lower()):
		if re.match('Using', phrase):
			phrase = phrase.replace('Using ', '')
			resource.append(phrase)
		elif is_research_problem(subparts_0):
			research_problem.append(subparts_0)
		elif not(is_method(subparts_0) and not ' ' in subparts_0):
			subparts_0 = remove_and_ending(subparts_0)
			solution.append(subparts_0)
		
	return solution, research_problem, resource

def involving_including_connector(phrase):
	solution = []
	resource = []
	language = []
	tool = []
	method = []
	dataset = []
	research_problem = []
	if ' involving ' in phrase.lower():
		phrase = phrase.replace(' Involving ', ' involving ').replace(' INVOLVING ', ' involving ')
	elif ' including ' in phrase.lower():
		phrase = phrase.replace(' Including ', ' including ').replace(' INCLUDING ', ' including ')	
	
	parts = phrase.split(' involving ') if ' involving ' in phrase \
	else phrase.split(' including ')
	
	if is_dataset(parts[0].lower()):
		dataset.append(parts[0])
	elif not non_content(parts[0], parts[0].lower()):
		parts[0] = remove_and_ending(parts[0])
		if not(is_method(parts[0]) and not ' ' in parts[0]):
			solution.append(parts[0])
			
	if ' and ' in parts[1].lower():
		language, data, tool, method, resource, research_problem = and_heuristics(parts[1])
	else:
		language, data, tool, method, resource = language_or_dataset_or_tool_or_method_or_resource(parts[1])
	if len(data) > 0:
		dataset.append(data[0])
		
	return solution, resource, language, tool, method, dataset, research_problem
	
def under_over_connector(phrase):
	solution = []
	research_problem = []
	resources = []
	language = []
	tool = []
	method = []
	dataset = []
	
	if ' under ' in phrase.lower():
		phrase = phrase.replace(' Under ', ' under ').replace(' UNDER ', ' under ')
	elif ' over ' in phrase.lower():
		phrase = phrase.replace(' Over ', ' over ').replace(' OVER ', ' over ')		
	
	i = phrase.find(' under ') if ' under ' in phrase \
	else phrase.find(' over ')	
	
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' under '):] if ' under ' in phrase \
	else phrase[i+len(' over '):]

	if not non_content(subparts_0, subparts_0.lower()):
		if is_tool(subparts_0):
			solution.append(subparts_0)	
		elif ' ' in subparts_0 and is_method(subparts_0):
			solution.append(subparts_0)			
		elif is_research_problem(subparts_0):
			research_problem.append(subparts_0)
		elif not is_method(subparts_0):
			subparts_0 = remove_and_ending(subparts_0)
			solution.append(subparts_0)

	if ' and ' in subparts_1.lower():
		language, dataset, tool, method, resources, rp = and_heuristics(subparts_1)
		if len(rp) > 0:
			research_problem.append(rp[0])
	else:
		if is_language(subparts_1):
			language.append(subparts_1)
		elif is_tool(subparts_1):
			tool.append(subparts_1)
		elif is_resource(subparts_1.lower()):
			resources.append(subparts_1)
		elif is_method(subparts_1):
			method.append(subparts_1)
		
	return solution, research_problem, resources, language, tool, method
	
def by_connector(phrase):	
	solution = []
	resource = []
	language = []
	tool = []
	method = []
	dataset = []
	research_problem = []

	phrase = phrase.replace(' By ', ' by ').replace(' BY ', ' by ')
	
	parts = phrase.split(' by ')
	
	if is_dataset(parts[0].lower()):
		dataset.append(parts[0])
	elif not non_content(parts[0], parts[0].lower()):
		parts[0] = remove_and_ending(parts[0])
		if not(is_method(parts[0]) and not ' ' in parts[0]):
			solution.append(parts[0])
	
	if ' and ' in parts[1].lower():
		language, data, tool, method, resource, research_problem = and_heuristics(parts[1])
		if len(data) > 0:
			dataset.append(data[0])
	else:
		meth = is_by_method(parts[1])
		if meth:
			method.append(parts[1])
		else:
			lang, t, res = language_or_tool_or_resource(parts[1])
			language, tool, resource = extend_lists_small(language, lang, tool, t, resource, res)
	
	return solution, resource, language, tool, method, dataset, research_problem
	
def using_with_connector(phrase):
	solution = []
	resource = []
	language = []
	tool = []
	method = []
	dataset = []
	research_problem = []
	if ' using ' in phrase.lower():
		phrase = phrase.replace(' Using ', ' using ').replace(' USING ', ' using ')
	elif ' with ' in phrase.lower():
		phrase = phrase.replace(' With ', ' with ').replace(' WITH ', ' with ')	
	
	parts = phrase.split(' using ') if ' using ' in phrase \
	else phrase.split(' with ')
	
	if is_dataset(parts[0].lower()):
		dataset.append(parts[0])
	elif not non_content(parts[0], parts[0].lower()):
		parts[0] = remove_and_ending(parts[0])
		if not(is_method(parts[0]) and not ' ' in parts[0]):
			solution.append(parts[0])
			
	if ' and ' in parts[1].lower():
		language, data, tool, method, resource, research_problem = and_heuristics(parts[1])
		if len(data) > 0:
			dataset.append(data[0])
	else:		
		language, tool, method, resource = language_or_tool_or_method_or_resource(parts[1])
				
	return solution, resource, language, tool, method, dataset, research_problem
	
def of_connector(phrase):
	solution = []
	research_problem = []
	resource = []
	language = []
	tool = []
	dataset = []
	method = []
	phrase = phrase.replace(' Of ', ' of ').replace(' OF ', ' of ')
	i = phrase.find(' of ')
	phrase_lower = phrase.lower()
	
	#some patterns are hard-coded
	if 'part of speech' in phrase_lower:
		phrase = remove_and_ending(phrase)
		solution.append(phrase)
	elif 'sense of humor' in phrase_lower or 'internet of things' in phrase_lower or 'family of' in phrase_lower or 'community of' in phrase_lower:
		solution.append(phrase)
	#otherwise generically applied
	else:
		subparts_0 = phrase[0:i]
		if is_dataset(subparts_0.lower()):	
			dataset.append(subparts_0)
		elif not non_content(subparts_0, subparts_0.lower()):
			subparts_0 = remove_and_ending(subparts_0)
			if not(is_method(subparts_0) and not ' ' in subparts_0):
				solution.append(subparts_0)			
			
		subparts_1 = phrase[i+len(' of '):]	
		
		if ' and ' in subparts_1.lower():
			language, data, tool, method, resource, research_problem = and_heuristics(subparts_1)
			if len(data) > 0:
				dataset.append(data[0])
		else:
			if is_dataset(subparts_1.lower()):	
				dataset.append(subparts_1)
			elif is_research_problem(subparts_1):
				research_problem.append(subparts_1)
			elif is_tool(subparts_1):
				tool.append(subparts_1)
			else:
				resource, sol, language = resource_or_solution_or_language(subparts_1)
				if len(sol) > 0:
					solution.append(sol[0])
		
	return solution, research_problem, resource, language, tool, dataset, method

def applied_to_connector(phrase):
	tool = []
	solution = []
	research_problem = []
	resource = []
	language = []
	method = []
	dataset = []
	
	phrase = phrase.replace(' Applied to ', ' applied to ')
	i = phrase.find(' applied to ')
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' applied to '):]
	
	if not non_content(subparts_0, subparts_0.lower()):
		if is_tool(subparts_0):
			tool.append(subparts_0)
		else:
			subparts_0 = remove_and_ending(subparts_0)
			if not(is_method(subparts_0) and not ' ' in subparts_0):
				solution.append(subparts_0)
	
	if ' and ' in subparts_1.lower():
		language, dataset, t, method, resource, research_problem = and_heuristics(subparts_1)
		if len(t) > 0:
			tool.append(t[0])
	else:
		if is_language(subparts_1):
			language.append(subparts_1)
		elif is_research_problem(subparts_1):
			research_problem.append(subparts_1)		
		elif is_resource(subparts_1.lower()):
			resource.append(subparts_1)
		
	return tool, solution, research_problem, resource, language, dataset, method
		
def for_connector(phrase):
	solution = []
	research_problem = []
	resources = []
	language = []
	tools = []
	method = []
	dataset = []
		
	phrase = phrase.replace(' For ', ' for ').replace(' FOR ', ' for ')
	i = phrase.find(' for ')
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' for '):]
	
	if is_dataset(subparts_0.lower()):
		dataset.append(subparts_0)
	elif not non_content(subparts_0, subparts_0.lower()):
		subparts_0 = remove_and_ending(subparts_0)	
		if not(is_method(subparts_0) and not ' ' in subparts_0):
			solution.append(subparts_0)
	
	if ' and ' in subparts_1.lower():
		language, data, tools, method, resources, research_problem = and_heuristics(subparts_1)
		if len(data) > 0:
			dataset.append(data[0])
	else:
		if is_language(subparts_1):
			language.append(subparts_1)
		elif is_tool(subparts_1):
			tools.append(subparts_1)		
		elif is_research_problem(subparts_1):
			research_problem.append(subparts_1)
		elif is_method(subparts_1):
			method.append(subparts_1)
		elif is_resource(subparts_1.lower()):
			resources.append(subparts_1)
		#else:		
			#print(subparts_1)
			# print('language: '+str(language))
			# print('resources: '+str(resources))
			# print('research problem: '+str(research_problem))
			#print()
				
	return solution, research_problem, resources, language, tools, method, dataset
	
def on_connector(phrase):
	solution = []
	research_problem = []
	resources = []
	language = []
	tool = []
	dataset = []
	method = []
	
	phrase = phrase.replace(' On ', ' on ').replace(' ON ', ' on ')
	i = phrase.find(' on ')
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' on '):]

	if not non_content(subparts_0, subparts_0.lower()):
		if is_tool(subparts_0) or is_method(subparts_0):
			solution.append(subparts_0)	
		elif is_research_problem(subparts_0):
			research_problem.append(subparts_0)
		else:
			subparts_0 = remove_and_ending(subparts_0)
			if not(is_method(subparts_0) and not ' ' in subparts_0):
				solution.append(subparts_0)
	
	if ' and ' in subparts_1.lower():
		language, dataset, tool, method, resources, rp = and_heuristics(subparts_1)
		if len(rp) > 0:
			research_problem.append(rp[0])
	else:
		if is_language(subparts_1):
			language.append(subparts_1)
		elif is_tool(subparts_1):
			tool.append(subparts_1)
		elif is_resource(subparts_1.lower()):
			resources.append(subparts_1)
		else:
			subparts_1 = remove_and_ending(subparts_1)	
			research_problem.append(subparts_1)
		
	return solution, research_problem, resources, language, tool, dataset, method
		
def from_connector(phrase):
	solution = []
	resources = []
	method = []
	language = []
	dataset = []
	tool = []
	research_problem = []

	phrase = phrase.replace(' From ', ' from ').replace(' FROM ', ' from ')
	i = phrase.find(' from ')
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' from '):]	
	
	subparts_0 = remove_and_ending(subparts_0)
	if not(is_method(subparts_0) and not ' ' in subparts_0):
		solution.append(subparts_0)
		
	subparts_1 = remove_and_ending(subparts_1)
	if ' and ' in subparts_1.lower():
		language, dataset, tool, method, resources, research_problem = and_heuristics(subparts_1)
	else:
		if is_resource(subparts_1.lower()):
			resources.append(subparts_1)
		elif is_method(subparts_1):
			method.append(subparts_1)
	
	return solution, language, dataset, tool, method, resources, research_problem
	
def in_connector(phrase):
	resource = []
	research_problem = []
	solution = []
	language = []
	tool = []
	method = []
	dataset = []

	phrase = phrase.replace(' In ', ' in ').replace(' IN ', ' in ')
	i = phrase.find(' in ')
	subparts_0 = phrase[0:i].strip()
	subparts_1 = phrase[i+len(' in '):].lstrip().strip()

	if not non_content(subparts_0, subparts_0.lower()):
		if is_tool(subparts_0) or is_resource(subparts_0.lower()):
			solution.append(subparts_0)	
		elif ' ' in subparts_0 and (is_method(subparts_0) or is_research_problem(subparts_0)):
			solution.append(subparts_0)
	
	if ' and ' in subparts_1.lower():
		language, dataset, tool, method, resource, research_problem = and_heuristics(subparts_1)
	else:
		if is_language(subparts_1):
			language.append(subparts_1)
		elif is_tool(subparts_1):
			tool.append(subparts_1)
		elif is_research_problem(subparts_1):
			research_problem.append(subparts_1)
		elif is_resource(subparts_1.lower()):
			resource.append(subparts_1)
		elif is_method(subparts_1):
			method.append(subparts_1)

	return resource, research_problem, solution, language, tool, method, dataset
	
def through_via_connector(phrase):
	solution = []
	research_problem = []
	method = []
	tool = []
	resource = []
	language = []
	dataset = []

	if ' through ' in phrase.lower():
		phrase = phrase.replace(' Through ', ' through ').replace(' THROUGH ', ' through ').replace(' throUgh ', ' through ')
	else:
		phrase = phrase.replace(' Via ', ' via ').replace(' VIA ', ' via ')
	i = phrase.find(' through ') if ' through ' in phrase \
	else phrase.find(' via ')
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' through '):] if ' through ' in phrase \
	else phrase[i+len(' via '):]

	if not non_content(subparts_0, subparts_0.lower()):
		subparts_0 = remove_and_ending(subparts_0)
		if not(is_method(subparts_0) and not ' ' in subparts_0):
			solution.append(subparts_0)
			
	if ' and ' in subparts_1.lower():
		language, dataset, tool, method, resource, research_problem = and_heuristics(subparts_1)
	else:
		if is_method(subparts_1):
			method.append(subparts_1)
		elif is_tool(subparts_1):
			tool.append(subparts_1)
		elif is_research_problem(subparts_1):
			research_problem.append(subparts_1)
		elif is_resource(subparts_1.lower()):
			resource.append(subparts_1)

	return solution, research_problem, method, tool, resource, language, dataset
	
def to_connector(phrase):
	resource = []
	research_problem = []
	solution = []
	language = []
	tool = []
	method = []
	dataset = []
	
	if 'end to end' in phrase.lower():
		phrase = remove_and_ending(phrase)	
		solution.append(phrase)
	elif 'peer to peer' in phrase.lower():
		solution.append(phrase)
	else:
		phrase = phrase.replace(' To ', ' to ').replace(' TO ', ' to ')
		i = phrase.find(' to ')
		subparts_0 = phrase[0:i]
		subparts_1 = phrase[i+len(' to '):]	

		if not non_content(subparts_0, subparts_0.lower()):
			if begins_phrase('[Uu]sing', subparts_0):
				i = subparts_0.find(' ')
				subparts_0 = subparts_0[i:].lstrip()
				if is_tool(subparts_0):
					tool.append(subparts_0)
				elif ' ' in subparts_0 and is_method(subparts_0):
					method.append(subparts_0)
				elif is_resource(subparts_0.lower()):
					resource.append(subparts_0)
				elif not(is_method(subparts_0) and not ' ' in subparts_0):
					subparts_0 = remove_and_ending(subparts_0)
					solution.append(subparts_0)					
			else:
				subparts_0 = remove_and_ending(subparts_0)
				
				if re.match("^.*(ing|ion|pproach)(\b|$)", subparts_0.lower()):			
					if ' ' in subparts_0:
						solution.append(subparts_0)
				elif not(is_method(subparts_0) and not ' ' in subparts_0):
					solution.append(subparts_0)					

		if ' and ' in subparts_1.lower():
			#print('subparts_1: '+subparts_1)
			language, dataset, t, meth, res, research_problem = and_heuristics(subparts_1)
			tool, method, resource = extend_lists_small(tool, t, method, meth, resource, res)
		else:
			if is_language(subparts_1):
				language.append(subparts_1)
			elif is_research_problem(subparts_1):
				research_problem.append(subparts_1)
			elif is_dataset(subparts_1.lower()):
				dataset.append(subparts_1)
			elif is_tool(subparts_1):
				tool.append(subparts_1)
			elif is_resource(subparts_1.lower()):
				resource.append(subparts_1)
			
	return resource, research_problem, solution, language, tool, method, dataset
	
def as_connector(phrase):
	resource = []
	research_problem = []
	solution = []
	method = []
	language = []
	dataset = []
	tool = []
	
	phrase = phrase.replace(' As ', ' as ').replace(' AS ', ' as ')
	i = phrase.find(' as ')	
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' as '):]	
		
	if (' ' in subparts_0 and is_method(subparts_0)) and is_method(subparts_1):
		subparts_0 = remove_and_ending(subparts_0)	
		method.append(subparts_0)
		subparts_1 = remove_and_ending(subparts_1)
		solution.append(subparts_1)
	else:
		if ' ' in subparts_0 and is_method(subparts_0):
			method.append(subparts_0)
		elif is_resource(subparts_0.lower()):
			solution.append(subparts_0)
		elif not(is_method(subparts_0) and not ' ' in subparts_0):
			subparts_0 = remove_and_ending(subparts_0)		
			solution.append(subparts_0)

		if ' and ' in subparts_1.lower():
			language, dataset, tool, meth, resource, research_problem = and_heuristics(subparts_1)
			if len(meth) > 0:
				method.append(meth[0])
		else:
			if is_method(subparts_1):
				method.append(subparts_1)
			elif len(solution) == 0:
				solution.append(subparts_1)
			elif is_research_problem(subparts_1):
				research_problem.append(subparts_1)
			elif is_resource(subparts_1.lower()):
				resource.append(subparts_1)
		
	return resource, research_problem, solution, method, language, dataset, tool

	