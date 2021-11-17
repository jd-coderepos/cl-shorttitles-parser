import sys
import re
from filters import *
from utils import *
from core_func import *
import func.titled_solution as titled_solution
import func.using_entity as using_entity
import func.toward_entity as toward_entity
import func.case_study as case_study
import func.colon_separator as colon_separator
import func.determiner_entity as determiner_entity
import func.ing_pattern_information as ing_pattern_information
import func.tool_entity as tool_entity
import func.proof as proof
import func.search as search
import func.grouping as grouping
import func.automated as automated
import func.supervision as supervision
import func.evaluation as evaluation
import func.improved as improved
import func.algorithm as algorithm
import func.programming as programming
import func.learning as learning
import func.prediction as prediction
import func.rules as rules
import func.application as application


def filter(line):
	if question(line): return True
	elif creative(line): return True
	elif proc_overview(line): return True
	elif meeting(line): return True
	elif conference(line): return True
	elif admin_reports(line): return True
	elif review(line): return True
	elif paper_parts(line): return True
	elif institute(line): return True
	elif non_english(line): return True
	return False

def update_rules_statistics(rules_statistics, rule_name):
	if rule_name in rules_statistics:
		count = rules_statistics[rule_name]
		count = count+1
		rules_statistics[rule_name] = count
	else:
		rules_statistics[rule_name] = 1
	return rules_statistics
	
	
#def parse_line(line, output, ct):
def parse_line(line, output, rules_statistics):
	toks = line.split(' ')
	line_lower = line.lower()
	research_problem = []
	solution = []
	resource = []
	language = []
	tool = []
	method = []
	dataset = []
							
	line_lower = line.lower()
		
	#template
	#PHINC: A Parallel Hinglish Social Media Code-Mixed Corpus for Machine Translation
	#Hypernym-LIBre: A Free Web-based Corpus for Hypernym Detection
	#TOCP: A Dataset for Chinese Profanity Processing
	#FlorUniTo@TRAC-2: Retrofitting Word Embeddings on an Abusive Lexicon for Aggressive Language Detection	
	if re.match("[^ ]*?([a-z][A-Z]|[A-Z][A-Z]|\d+)[^ ]*?:", line):		
		solution, research_problem, resource, language, tool, method, dataset = titled_solution.computer_science(line)
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:
			rules_statistics = update_rules_statistics(rules_statistics, "rule1")
	elif re.match('Using', line):
		solution, research_problem, resource, language, tool, method, dataset = using_entity.computer_science(line)
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:
			rules_statistics = update_rules_statistics(rules_statistics, "rule2")
	elif begins_phrase('Toward', line):
		solution, research_problem, resource, language, tool, method, dataset = toward_entity.computer_science(line)
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:
			rules_statistics = update_rules_statistics(rules_statistics, "rule3")
	elif ':' in line and not (re.match('(a )?case study:', line.lower()) or re.match('^.*:( a)? case study', line_lower) or re.match('^.*:( the)? case of', line_lower)):
		parts = line.split(':')

		phrase = parts[0].strip()
		if (len(phrase.split(' ')) < 3 and is_method(phrase.lower())) or (len(phrase.split(' ')) < 4 and (is_tool(phrase) or is_resource(phrase.lower()))):
			solution.append(phrase)
			solution, research_problem, resource, language, tool, method, dataset = colon_separator.computer_science('', parts[1].lstrip().strip())
		else:
			solution, research_problem, resource, language, tool, method, dataset = colon_separator.computer_science(phrase, parts[1].lstrip().strip())		
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:	
			rules_statistics = update_rules_statistics(rules_statistics, "rule4")
	elif re.match('(a )?case study:', line.lower()):		
		i = line.find(':')
		phrase = line[i:].strip()
								
		if ' ' in phrase:
			i = phrase.find(' ')
			phrase = phrase[i:].lstrip()
		
		connector_indexes = get_list_of_connector_indexes(phrase.lower(), connectors_rx)
		connector_indexes.sort()	
		
		if len(connector_indexes) == 0 and len(phrase.split(' ')) < 6:
			solution.append(phrase)
		else:
			solution, research_problem, resource, language, tool, method, dataset = case_study.computer_science(phrase)
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:	
			rules_statistics = update_rules_statistics(rules_statistics, "rule5")
	elif ending(line_lower, ': (a )?case study'):		
		phrase = line.split(':')[0].strip()
		phrase_lower = phrase.lower()
		
		solution, research_problem, resource, language, tool, method, dataset = case_study.computer_science(phrase)
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:
			rules_statistics = update_rules_statistics(rules_statistics, "rule6")
	elif re.match('^.*:( a)? case study', line_lower):
		parts = line.split(':')	
		
		phrase = parts[0].strip()
		if (len(phrase.split(' ')) < 3 and is_method(phrase.lower())) or (len(phrase.split(' ')) < 4 and (is_tool(phrase) or is_resource(phrase.lower()))):
			solution.append(phrase)
		else:
			solution, research_problem, resource, language, tool, method, dataset = case_study.computer_science(phrase)
			
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:
			parts[1] = parts[1].lstrip()
			connector_indexes = get_list_of_connector_indexes(parts[1].lower(), connectors_rx)
			connector_indexes.sort()
			
			if len(connector_indexes) > 0:
				phrase = parts[1][connector_indexes[0]:].lstrip()
				if ' ' in phrase:
					i = phrase.find(' ')
					phrase = phrase[i:].lstrip()
				
				if re.match('Using', phrase) or re.match('using', phrase):
					sol, rp, res, lang, t, meth, data = using_entity.computer_science(phrase)
				else:
					sol, rp, res, lang, t, meth, data = case_study.computer_science(phrase)
			else:			
				i = parts[1].lower().find('study ')
				phrase = parts[1][i:].strip()
				if ' ' in phrase:
					i = phrase.find(' ')
					phrase = phrase[i:].lstrip()			
				if not phrase == '':
					sol, rp, res, lang, t, meth, data = case_study.computer_science(phrase)
					
			if len(sol) > 0 or len(rp) > 0 or len(res) > 0 or len(lang) > 0 or len(t) > 0 or len(meth) > 0 or len(data) > 0:
				solution, research_problem, resource, language, tool, method, dataset = extend_lists_seven(solution, sol, research_problem, rp, resource, res, language, lang, tool, t, method, meth, dataset, data)
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:
			rules_statistics = update_rules_statistics(rules_statistics, "rule7")
	elif re.match('^.*:( the)? case of', line_lower):
		parts = line.split(':')	
		
		phrase = parts[0].strip()
		if (len(phrase.split(' ')) < 3 and is_method(phrase.lower())) or (len(phrase.split(' ')) < 4 and (is_tool(phrase) or is_resource(phrase.lower()))):
			solution.append(phrase)
		else:
			solution, research_problem, resource, language, tool, method, dataset = case_study.computer_science(phrase)

		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:		
			#the Case of Amharic
			#the case of the Linguistic Crescent varieties
			parts[1] = parts[1].lstrip()
			
			i = parts[1].find('of ')
			phrase = parts[1][i:].lstrip()
			
			if ' ' in phrase:
				i = phrase.find(' ')
				phrase = phrase[i:].lstrip()
				
			if re.match('Using', phrase) or re.match('using', phrase):
				sol, rp, res, lang, t, meth, data = using_entity.computer_science(phrase)
			else:
				sol, rp, res, lang, t, meth, data = case_study.computer_science(phrase)				
			
			if len(sol) > 0 or len(rp) > 0 or len(res) > 0 or len(lang) > 0 or len(t) > 0 or len(meth) > 0 or len(data) > 0:
				solution, research_problem, resource, language, tool, method, dataset = extend_lists_seven(solution, sol, research_problem, rp, resource, res, language, lang, tool, t, method, meth, dataset, data)
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:
			rules_statistics = update_rules_statistics(rules_statistics, "rule8")
	elif re.match('(a )?case study ', line.lower()):		
		connector_indexes = get_list_of_connector_indexes(line.lower(), connectors_rx)
		connector_indexes.sort()
		
		if len(connector_indexes) > 0:
			phrase = line[connector_indexes[0]:].lstrip()
			if ' ' in phrase:
				i = phrase.find(' ')
				phrase = phrase[i:].lstrip()
			
			if re.match('Using', phrase) or re.match('using', phrase):
				solution, research_problem, resource, language, tool, method, dataset = using_entity.computer_science(phrase)
			else:
				solution, research_problem, resource, language, tool, method, dataset = case_study.computer_science(phrase)
		else:			
			i = line.lower().find('study ')
			phrase = line[i:].strip()
			if ' ' in phrase:
				i = phrase.find(' ')
				phrase = phrase[i:].lstrip()			
			if not phrase == '':
				solution, research_problem, resource, language, tool, method, dataset = case_study.computer_science(phrase)
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:
			rules_statistics = update_rules_statistics(rules_statistics, "rule9")
	elif determiner_start(line.lower()):
		solution, research_problem, resource, language, tool, method, dataset = determiner_entity.computer_science(line)
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:
			rules_statistics = update_rules_statistics(rules_statistics, "rule10")
		# if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:
			# output.write(line+'\n')
			# ct = ct + 1
	elif starts_phrase('from', line_lower) and ' to ' in line_lower:		
		connector_indexes = get_list_of_connector_indexes(line.lower(), connectors_rx)
		connector_indexes.sort()		
		
		i = line.find(' ')
		line = line[i:].strip()
		
		if len(connector_indexes) == 1:
			#print(line)		
			connector = get_info_exactly_one_connector(line.lower())
			
			if connector == None:
				return solution, research_problem, resource, language, method, tool, dataset, ct
			
			i = line.lower().find(' '+connector+' ')
			subpart_0 = line[0:i]
			subpart_1 = line[i+len(' '+connector+' '):]

			if ' ' not in subpart_0:
				solution.append(subpart_1)
			else:				
				language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_0)
				solution.append(subpart_1)
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:		
			rules_statistics = update_rules_statistics(rules_statistics, "rule11")
	elif start_ing(line):
		solution, research_problem, resource, language, tool, method, dataset = ing_pattern_information.computer_science(line)
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:
			rules_statistics = update_rules_statistics(rules_statistics, "rule12")
	elif ending(line_lower, 'systems') or ending(line_lower, 'system') or ending(line_lower, 'models') or ending(line_lower, 'model') or ending(line_lower, 'programs') or ending(line_lower, 'program'):
		solution, research_problem, resource, language, tool, method, dataset = tool_entity.computer_science(line)
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:
			rules_statistics = update_rules_statistics(rules_statistics, "rule13")
	elif ending(line_lower, 'search'):	
		solution, research_problem, method = search.computer_science(line)
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:
			rules_statistics = update_rules_statistics(rules_statistics, "rule14")
	elif ending(line_lower, 'classification') or ending(line_lower, 'clustering'):	
		solution, research_problem, method = grouping.computer_science(line)
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:
			rules_statistics = update_rules_statistics(rules_statistics, "rule15")
	elif 'proof' in line_lower:
		solution, method = proof.computer_science(line)
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:
			rules_statistics = update_rules_statistics(rules_statistics, "rule16")
	#elif second_word_ending('of', line):	
	elif begins_phrase('automatic', line_lower) or begins_phrase('automated', line_lower):
		solution, research_problem, resource, language, tool, method, dataset = automated.computer_science(line)
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:		
			rules_statistics = update_rules_statistics(rules_statistics, "rule17")
	elif first_word_ending('supervized', line_lower) or first_word_ending('supervised', line_lower):
		solution, research_problem, resource, language, tool, method, dataset = supervision.computer_science(line)
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:		
			rules_statistics = update_rules_statistics(rules_statistics, "rule18")
	elif 'evaluation' in line_lower:
		solution, research_problem, resource, language, tool, method, dataset = evaluation.computer_science(line)
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:		
			rules_statistics = update_rules_statistics(rules_statistics, "rule19")
	elif starts_phrase('improve', line_lower):
		i = line.find(' ')
		line = line[i:].lstrip()
		solution, research_problem, resource, language, tool, method, dataset = improved.computer_science(line)
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:		
			rules_statistics = update_rules_statistics(rules_statistics, "rule20")
	elif 'algorithm' in line_lower:
		solution, research_problem, resource, language, tool, method, dataset = algorithm.computer_science(line)
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:		
			rules_statistics = update_rules_statistics(rules_statistics, "rule21")
	elif 'programming' in line_lower:	
		solution, research_problem, resource, language, tool, method, dataset = programming.computer_science(line)
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:		
			rules_statistics = update_rules_statistics(rules_statistics, "rule22")
	elif 'learning' in line_lower:
		solution, research_problem, resource, language, tool, method, dataset = learning.computer_science(line)
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:		
			rules_statistics = update_rules_statistics(rules_statistics, "rule23")
	elif 'prediction' in line_lower:
		solution, research_problem, resource, language, tool, method, dataset = prediction.computer_science(line)
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:		
			rules_statistics = update_rules_statistics(rules_statistics, "rule24")
	elif 'rule' in line_lower or 'protocol' in line_lower:
		solution, research_problem, resource, language, tool, method, dataset = rules.computer_science(line)
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:
			rules_statistics = update_rules_statistics(rules_statistics, "rule25")
	elif 'application' in line_lower:
		solution, research_problem, resource, language, tool, method, dataset = application.computer_science(line)
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:
			rules_statistics = update_rules_statistics(rules_statistics, "rule26")
	else:
		connector_indexes = get_list_of_connector_indexes(line.lower(), connectors_rx)
		connector_indexes.sort()

		if len(connector_indexes) == 0:
			if ' and ' in line.lower():	
				language, dataset, tool, method, resource, research_problem = and_heuristics(line)
				if len(language) == 0 and len(dataset) == 0 and len(tool) == 0 and len(method) == 0 and len(resource) == 0 and len(research_problem) == 0:
					language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(line)
			else:
				if is_dataset(line.lower()) and not 'without' in line.lower():
					dataset.append(line)
				else:
					solution.append(line)
					
			if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:
				rules_statistics = update_rules_statistics(rules_statistics, "rule27")
				
		elif len(connector_indexes) == 1:
			connector = get_info_exactly_one_connector(line.lower())
			
			if connector == None:
				#return solution, research_problem, resource, language, method, tool, dataset, ct
				return solution, research_problem, resource, language, method, tool, dataset, rules_statistics
			
			i = line.lower().find(' '+connector+' ')
			subpart_0 = line[0:i]
			subpart_1 = line[i+len(' '+connector+' '):]
		
			if 'using' == connector.lower() or 'with' == connector.lower() or 'by' == connector.lower() or 'through' == connector.lower() or 'via' == connector.lower():
				if is_research_problem(subpart_0) and is_tool(subpart_1):
					solution.append(subpart_0)
					tool.append(subpart_1)
				elif is_research_problem(subpart_0) and is_research_problem(subpart_1):
					if len(subpart_1.split(' ')) > 4 or len(subpart_0.split(' ')) == 2:
						research_problem.append(subpart_0)
						solution.append(subpart_1)
					else:
						solution.append(subpart_0)
						method.append(subpart_1)
				elif is_tool(subpart_1):
					if not non_content(subpart_0, subpart_0.lower()):				
						solution.append(subpart_0)
					tool.append(subpart_1)
				else:
					if not non_content(subpart_0, subpart_0.lower()):				
						solution.append(subpart_0)
					language, dataset, method, resource, research_problem = language_or_dataset_or_method_or_resource_or_rp(subpart_1)
			elif 'for' == connector.lower():
				if len(subpart_0.split(' ')) < 4 and is_research_problem(subpart_0) and is_tool(subpart_1):
					solution.append(subpart_0)
					tool.append(subpart_1)
				elif is_tool(subpart_0):
					solution.append(subpart_0)
					language, dataset, method, resource, research_problem = language_or_dataset_or_method_or_resource_or_rp(subpart_1)
				elif is_dataset(subpart_0):
					dataset.append(subpart_0)
					language, method, resource, research_problem = language_or_method_or_resource_or_rp(subpart_1)
				elif is_language(subpart_1):
					solution.append(subpart_0)
					language.append(subpart_1)
				elif is_tool(subpart_1):
					solution.append(subpart_0)
					tool.append(subpart_1)
				else:
					solution.append(subpart_0)
					language, dataset, method, resource, research_problem = language_or_dataset_or_method_or_resource_or_rp(subpart_1)
			elif is_language(subpart_1):
				solution.append(subpart_0)
				language.append(subpart_1)
			elif 'in' == connector.lower() or 'on' == connector.lower() or 'over' == connector.lower() or 'under' == connector.lower() or 'across' == connector.lower() or 'against' == connector.lower() or 'at' == connector.lower() or 'within' == connector.lower() or 'involving' == connector.lower() or 'including' == connector.lower():
				if not non_content(subpart_0, subpart_0.lower()):
					solution.append(subpart_0)
				language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_1)
			elif 'of' == connector.lower():
				if not non_content(subpart_0, subpart_0.lower()):
					language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_0)
				lang, data, t, meth, res, rp = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_1)
				language, dataset, tool, method, resource, research_problem = extend_lists_all(language, lang, dataset, data, tool, t, method, meth, resource, res, research_problem, rp)
			elif is_language(subpart_0):
				language.append(subpart_0)
				solution.append(subpart_1)
			elif 'as' == connector.lower():
				if ending(subpart_1.lower(), 'problem'):
					if not non_content(subpart_0, subpart_0.lower()):
						solution.append(subpart_0)
					research_problem.append(subpart_1)
				else:
					language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_0)
					solution.append(subpart_1)
			elif 'from' == connector.lower():
				if not non_content(subpart_0, subpart_0.lower()):
					solution.append(subpart_0)			
				language, tool, dataset, research_problem, method, resource = language_or_tool_or_dataset_or_rp_or_method_or_resource(subpart_1)
			elif 'to' == connector.lower():
				if not non_content(subpart_0, subpart_0.lower()):
					solution.append(subpart_0)			
				language, tool, dataset, research_problem, method, resource = language_or_tool_or_dataset_or_rp_or_method_or_resource(subpart_1)
			elif 'between' == connector.lower():
				if ' and ' in subpart_1:
					if not non_content(subpart_0, subpart_0.lower()):					
						solution.append(subpart_0)
					language, dataset, tool, method, resource, research_problem = and_heuristics(subpart_1)
				else:
					if not non_content(subpart_0, subpart_0.lower()):					
						solution.append(subpart_0)
					language, tool, dataset, research_problem, method, resource = language_or_tool_or_dataset_or_rp_or_method_or_resource(subpart_1)
			elif 'towards' == connector.lower():
				if not non_content(subpart_1, subpart_1.lower()):
					solution.append(subpart_1)
				language, tool, dataset, research_problem, method, resource = language_or_tool_or_dataset_or_rp_or_method_or_resource(subpart_0)
				
			if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:
				rules_statistics = update_rules_statistics(rules_statistics, "rule28")
			# else:	
				# print(connector)
				# if not non_content(subpart_0, subpart_0.lower()):					
					# print(subpart_0)
				# print(subpart_1+'\n')
			#else:					
	# if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0:
		# output.write(line+'\n')
		# output.write('solution: '+str(solution)+'\n')
		# output.write('research problem: '+str(research_problem)+'\n')
		# output.write('resource: '+str(resource)+'\n')
		# output.write('language: '+str(language)+'\n')
		# output.write('tool: '+str(tool)+'\n')
		# output.write('method: '+str(method)+'\n')
		# output.write('dataset: '+str(dataset)+'\n\n')
		# ct = ct + 1

	return solution, research_problem, resource, language, method, tool, dataset, rules_statistics
	#return solution, research_problem, resource, language, method, tool, dataset, ct

def write_out(out_file, values, type):
	out_file.write('TOTAL UNIQUE '+type+': '+str(len(values))+'\n\n')
	for v in values:
		out_file.write(v+'\n')
	
def read_file(input_file, output_dir):
	solution = []
	research_problem = []
	resource = []
	language = []
	tools = []
	method = []
	datasets = []

	rules_statistics = {}	
	
	titles_count = 0
	solution_count = 0
	research_problem_count = 0
	resource_count = 0
	language_count = 0
	method_count = 0
	tool_count = 0
	dataset_count = 0
	
	raw_count = 0
	
	subgrouped_titles = 0
	
	output_file = open(output_dir+'/parsed-titles-full-output.dat', 'w', encoding='utf-8')
	research_problem_file = open(output_dir+'/research_problem.dat', 'w', encoding='utf-8')
	solution_file = open(output_dir+'/solution.dat', 'w', encoding='utf-8')
	resource_file = open(output_dir+'/resource.dat', 'w', encoding='utf-8')
	language_file = open(output_dir+'/language.dat', 'w', encoding='utf-8')
	tool_file = open(output_dir+'/tool.dat', 'w', encoding='utf-8')
	dataset_file = open(output_dir+'/dataset.dat', 'w', encoding='utf-8')
	method_file = open(output_dir+'/method.dat', 'w', encoding='utf-8')
	processed_titles_file = open(output_dir+'/processed-titles.dat', 'w', encoding='utf-8')
	clean_acl_titles = open(output_dir+'/acl-titles.dat', 'w', encoding='utf-8')
		
	with open(input_file, 'r', encoding='utf-8') as f:
		while(True):
			line = f.readline().rstrip("\n")
			if line:
								
				if (filter(line)): continue
				
				original_title = line
				title = preprocess(line)
				
				if '' == title:
					continue
				elif len(title.split(' ')) <= 4:
					continue			

				raw_count = raw_count + 1
					
				#sol, rp, res, lang, meth, t, data, subgrouped_titles = parse_line(title, output_file, subgrouped_titles)
				sol, rp, res, lang, meth, t, data, rules_statistics = parse_line(title, output_file, rules_statistics)
								
				data_str = ""
				
				if len(sol) > 0:
					solution_count = solution_count + len(sol)
					sol_str = ""
					for s in sol:
						sol_str = sol_str+"\t"+s
						solution.append(s)
					sol_str = sol_str.lstrip().rstrip()
					sol_str = "solution: "+sol_str+"\n"
					data_str = data_str+sol_str
				if len(rp) > 0:
					research_problem_count = research_problem_count + len(rp)
					rp_str = ""
					for res_prob in rp:
						rp_str = rp_str+"\t"+res_prob
						research_problem.append(res_prob)
					rp_str = rp_str.lstrip().rstrip()
					rp_str = "research_problem: "+rp_str+"\n"
					data_str = data_str+rp_str
				if len(res) > 0:
					resource_count = resource_count + len(res)
					res_str = ""
					for r in res:
						res_str = res_str+"\t"+r
						resource.append(r)
					res_str = res_str.lstrip().rstrip()
					res_str = "resource: "+res_str+"\n"
					data_str = data_str+res_str
				if len(lang) > 0:
					language_count = language_count + len(lang)
					lang_str = ""
					for lan in lang:
						lang_str = lang_str+"\t"+lan
						language.append(lan)
					lang_str = lang_str.lstrip().rstrip()
					lang_str = "language: "+lang_str+"\n"
					data_str = data_str+lang_str		
				if len(meth) > 0:
					method_count = method_count + len(meth)
					meth_str = ""
					for m in meth:
						meth_str = meth_str+"\t"+m
						method.append(m)
					meth_str = meth_str.lstrip().rstrip()
					meth_str = "method: "+meth_str+"\n"
					data_str = data_str+meth_str
				if len(t) > 0:
					tool_count = tool_count + len(t)
					tool_str = ""
					for tool in t:
						tool_str = tool_str+"\t"+tool
						tools.append(tool)
					tool_str = tool_str.lstrip().rstrip()
					tool_str = "tool: "+tool_str+"\n"
					data_str = data_str+tool_str
				if len(data) > 0:
					dataset_count = dataset_count + len(data)
					dataset_str = ""
					for d in data:
						dataset_str = dataset_str+"\t"+d
						datasets.append(d)
					dataset_str = dataset_str.lstrip().rstrip()
					dataset_str = "dataset: "+dataset_str+"\n"
					data_str = data_str+dataset_str
				
				if data_str != "":
					processed_titles_file.write(original_title+'\n')
					output_file.write(title+'\n')
					output_file.write(data_str+'\n')
					titles_count = titles_count + 1		
				
				clean_acl_titles.write(title+'\n')
				
			else:			
				break
	
	solution = set(solution)
	for sol in solution:
		solution_file.write(str(sol)+'\n')	
		
	research_problem = set(research_problem)
	for rp in research_problem:
		research_problem_file.write(str(rp)+'\n')
	
	resource = set(resource)
	for res in resource:
		resource_file.write(str(res)+'\n')	
	
	language = set(language)
	for lang in language:
		language_file.write(str(lang)+'\n')	
	
	tools = set(tools)
	for t in tools:
		tool_file.write(str(t)+'\n')	
	
	method = set(method)
	for meth in method:
		method_file.write(str(meth)+'\n')
	
	datasets = set(datasets)
	for data in datasets:
		dataset_file.write(str(data)+'\n')		
	
	print('done!')
	print('total valid titles: '+str(raw_count))
	print('Written to '+output_dir+'\\acl-titles.dat')   
	print('total processed titles: '+str(titles_count))	
	print('Written to '+output_dir+'\\processed-titles.dat')
	print('Total solution entities extracted: '+str(solution_count))
	print('Total research_problem entities extracted: '+str(research_problem_count))
	print('Total resource entities extracted: '+str(resource_count))
	print('Total language entities extracted: '+str(language_count))
	print('Total method entities extracted: '+str(method_count))
	print('Total tool entities extracted: '+str(tool_count))
	print('Total dataset entities extracted: '+str(dataset_count)+'\n')

	# for key in rules_statistics:
		# print(key+'\t'+str(rules_statistics[key])+'\n')	
	
# takes two arguments:	
# 1. input data file with a single title in each line
# 2. output directory where the parsed data will be written to
def main(argv):	
	if not len(argv) == 2:
		print('Usage: python parse_titles.py <titles-input-file> <output_data_dir>')
	else:
		read_file(argv[0], argv[1])

if __name__ == "__main__":
    main(sys.argv[1:])
	