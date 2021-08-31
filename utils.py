import re

numeric_short = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
prepositions_short = ['at', 'for', 'in', 'of', 'on', 'over', 'to', 'toward']
adjectives_short = ['efficient', 'improved', 'formal', 'simple', 'new', 'novel', 'mixed', 'robust', 'supervised', 'unsupervised', 'statistical', 'uniform', 'stochastic', 'discriminative', 'iterative']
determiners_short = ['the', 'a', 'an', 'future']

det_rx = 'the|a|an|future'

#case_study_research_problem_splitter prepositions and verbs
cs_rp_splitters_rx = 'in|of|on|over|from|using|for'

lang_rx = 'English|Latin|Spanish|French|German|Russian|Portuguese|Italian|Dutch|Czech|Swedish|Polish|Bulgarian|Hungarian|\
Slovenian|Norwegian|Irish|Romanian|Venetan|Danish|Croatian|Serbian|Icelandic|Greece|Greek|Occitan|Estonian|Welsh|Finnish|Slavic|\
Afrikaans|Odawa|Ainu|Kven|Mi\'kmaq|Gagauz|Kanyen\'k\\\'eha|Chukchi|Shipibo\-Konibo|Kunwinjku|Naija|Wolof|Evenki|Kyrgyz|Setswana|\
Tigrigna|Oromo|Wolaytta|Sundanese|Balinese|Bataks|Egyptian|Levantine|Abui|Wambaya|\
Hindi|Bengali|Lahnda|Telugu|Marathi|Tamil|Urdu|Punjabi|Gujarati|Bangla|Sindhi|Odia|Sanskrit|Bhojpuri|Magahi|Malayalam|Kannada|Dravidian|Indic|Konkani|Tibetan|\
Arabic|Turkish|Turkic|Amharic|Hebrew|Persian|Syriac|Coptic|Farsi|Armenian|Mediterranean|Iberian|\
Taizi|Sanaani|Najdi|Jordanian|Syrian|Iraqi|Moroccan|Mordvinic|Shahmukhi|\
Mandarin|Chinese|Japanese|Kanji|Hakka|Basque|Hiberno-English|\
Indonesian|Javanese|Korean|Vietnamese|Taiwanese|Sinhala|Malay|Malaysian|Malagasy|Thai|Tagalog|Filipino|Latvian|Cantonese|Tuvan|Chintang|\
Maltese|Quechua|Murrinh-Patha|Bambara|Breton|Erzya|Laz|Lakota|Somali|\
Sign|R|Python|Java|java|Prolog|Accadian|Maori|Tikopia|JavaScript|Javascript|C\+\+|C/C\+\+|Scala|Haskell|SPARQL|Sparql|COBOL|\
Natural|Minority|Ega|Piu|Arapaho|Braille|\
Prolog|Warao'

nl_parts_rx = 'Adverbs|[vV]erb(s)?|Idioms|Questions|[dD]ialogue(s)?|Dialog|Hypertexts|Discourse|Charts|Subtitles|Interviews|INTER(\-)?VIEW[sS]?|\
Words|Prepositions|Sarcasm|Documents|[tT]ext(s)?|Instructions|[cC]orp(us|ora)|Metaphors|Phrases|[sS]peech|[sS]entence(s)?|[dD]ocument(s)?|[uU]tterance(s)?|\
Captions|Compounds'

living_1_rx = '(human|student|animal|songwriter|\
journalist|interpreter|egyptologist|developer|novice|expert)[s]?'
living_2_rx = 'blind|f\*r\*i\*e\*n\*d\*s\*|everyone|people'
living_3_rx = 'children[s]?'

places_rx = 'taiwan|argentina|mexico|spain|us(a)?|india|africa|china|japan|germany|france'

object_rx = 'Wheelchairs'
abstract_rx = 'Concepts|Events|Courses|Action|Belief/Factuality|Prevention|Research|World'

non_content_words_rx = 'available|prevention|action|course|use'

#tool regular expression patterns
tools_1_rx = 'bert|lstm|memory|controller|perceptron|library|generator|writer|finder|tagger|segmentor|summarizer|realizer|translator|demonstrator|solver|hypernet|facebook|spark|android|apple|stack\soverflow|duplex|github|google\splay|app|ide|ontology|browser|differentiator|agent|windows|\
segmenter|stemmer|lemmatizer|retriever|aligner|recognizer|baseline|analyzer|synthesizer|diacritizer|identifier|learner|processor|browser|frontend|backend|end|analogue|hadoop|chrome|stereo|blockchain|macintosh|technology|estimator|cluster|listener|enumerator|robot|talk|application'
tools_2_rx = '(tool|network|system|pack|suite|interface|architecture|parser|car|toolkit|indexer|classifier|net|engine|field|client|package|kit|computer|tensor|device|puzzle|encoder|microcontroller|\
tester|framework|environment|program|annotator|auto\-encoder|autoencoder|detector|decoder|implementation|agent|platform|transformer|embedding|checker|crf|svm|machine|layer|compiler|software|sensor)[s]?'
tools_3_rx = 'workbench(es)?'

#method regular expression patterns
method_1_rx = '(protocol|experiment|science|method|procedure|heuristic|paradigm|algorithm|walk|review|template|model|standard|mechanism|verbalism|attack|proof|grammar|\
workflow|specification|spec|proposal|design|recipe|technique|formalism|rule|movement|inference|format|principle|prototype|module|margin|mixture|formula|equation|path|practice)[s]?'
method_2_rx = '(approach|process|search|parse)(es)?'
method_3_rx = '(strateg|methodolog|probabilit|theor|analog)(ies|y)'
method_4_rx = 'lingua|analysis|measure|programming|logic|annotation|feedback|support|loop|cleanup|clean-up|retrieval|descent|retrieval|entropy|colonoscopy|radiotherapy|descent|softmax|transform|composition|x\-ray|videography|invariance|mix|bound|ensemble|uncertainty|\
scheme|schema|look\-up|online|backoff|transfer|closure|prosody|rhetoric|transport|carlo|markov|pivot|retrieval|weighted|learning|formula|theory|interferometry|ascent|gradient|cover|algebra|multiplexing|fmri|cryptography|minima|period|surveillance|selection'

#resource regular expression patterns
resources_1_rx = '(dictionar|stor|typolog|inventor|ontolog|summar|biograph|fluenc|terminolog|accurac|geometr|poetr|polic|vocabular|dependenc|taxonom|commentar|entr|hierarch|quer|obituar|observator)(ies|y)'
resources_2_rx = 'knowledge|information|literature|web|media|twitter|codalab|wikipedia|cloud|news|space|wordnet|slang|time|input|sytax|automata|prose|blogosphere|era|archive|traffic|odometry|desktop|release|provenance|bulletin|trojan|potential|imagery|navigator|honeybot|pool|spreadsheet|data|\
discourse|memory|work|wiktionary|wikidata|quran|irony|sarcasm|code|behavior|rebuttal|intent|email|demand|anaphorae|hardware|age|uses|answer|prior|gaze|orthography|reddit|cache|length|skype|sgx|record|emoji|grid|voice|malware|account|fabric|coin|screenshot|reservoir|qualification|scrabble'
resources_3_rx = '(resource|source|description|catalogue|set|collection|text|annotation|lexicon|dataset|database|data|structure|writing|term|question|comment|content|object|table|mask|dendrite|cytoplasm|\
dialogue|bible|game|stream|novel|concept|size|vector|error|reference|influence|forum|accent|phone|number|board|list|portal|filter|metric|set|clause|evidence|cluster|submission|processor|applications|\
computer|board|knowledgebase|base|language|tree|tree[Bb]ank|bank|event|character|output|grammar|synset|lexeme|pair|log|report|image|essay|domain|document|phrase|syllable|pathway|store|eigenvector|response|\
narrative|subtitle|label|audio|video|name|word|gram|translation|distance|variable|recipe|pattern|forest|client|kernel|structure|aspect|review|graph|behaviour|sequence|feedback|map|symbol|channel)[s]?'
resources_4_rx = 'corp(ora|us)'
resources_5_rx = 'thesaur(i|us)'
resources_6_rx = '(speech|sketch)(es)?'
resources_7_rx = 'anaphor(a)?'

#dataset
dataset_1_rx = '(dataset|benchmark|corpus|database|data)'

#problem domains
domains_rx = 'bio(-)?medical|healthcare|science|west african|life science(s)?|indian|american|formosan|geography|iberian'

#research_fields
fields = 'linguistics|biochemistry|e-commerce|mathematica|intelligence|astronomy'

#generic resource regular expression patterns
gen_resources_1_rx = '(protocol|system|forum|figure|paper|twitter|tweet|rumour|posting|patent|web|micro(\-)?blog|input|article|\
experiment|pack|argument|science|domain|suite|market|bank|example|case|use(\-)?case|scenario|instance|conference|location)[s]?'
gen_resources_2_rx = "(communit|centur|stud)(y|ies)"
gen_resources_3_rx = "healthcare|e\-Commerce|enterprise|reddit"
gen_resources_4_rx = "business(es)?"

#phrase start
generic_starter_rx = 'efficient|improved|formal|simple|new|novel|mixed|robust|supervised|unsupervised|hybrid|statistical|uniform|stochastic|\
discriminative|iterative|the|a|an|future|one|two|three|four|five|six|seven|eight|nine|ten|lightweight|general|some|tentative|various|overview'

#generic phrase end usually at unigram or bigram level
generic_terms_rx = 'recognition|detection|maintenance|accuracy|characterization(s)?|development|study|need|new|way|procedure|operation(s)?|alternative|working|getting|heuristic|paradigm|algorithm|workflow|architecture(s)?|prospect|specification|spec|dataset|roadmap|application|preservation|interpretation|demonstration|principle(s)?|generalization|\
extraction|symmetry|challenge(s)?|problem(s)?|evaluation|system(s)?|tester|case|tool|generation|structure|foundation|framework|process|resource(s)?|bases|strateg(ies|y)|problem|challenge|center|experiment|representation(s)?|theory|large|survey|competency|quality|consensus|demo|refinement|overview|abduction|review|tutorial|\
classification|environment|logic|proposal|notion|design|model|recipe|program|attempt|approach(es)?|workbench|detector|lexicon|database|implementation|treatment|interaction|identification|research|novel|performance|robustness|comparison|characteristic(s)?|verification|introduction|manipulability|limitation(s)?|construction|\
understanding|estimation|improvement|determination|methodology|mission|method(s)?|agent|rationale|strategy|platform|issue(s)?|corpus|heuristic|technique(s)?|benchmark|formalism|report|infrastructure|analysis|acquisition|large-scale|high-quality|strength|prediction|stability|solution|estimation|selection|refinement(s)?'

#pronouns regular expression
pronoun_rx = 'this|these|that|those|who|which|as|each|all|either|one|both|any|such'

#used in system
software_rx = 'model|implementation|system|library|application|tool|agent|parser|extractor'

non_of_connectors_rx = 'in|for|on|to|from|with|via|through|using|as|by|at|over|against|under|within|including|involving|representing|across|towards|between'
non_from_connectors_rx = 'in|for|on|to|of|with|via|through|using|as|by|at|over|against|under|within|including|involving|representing|across|towards|between'
non_on_connectors_rx = 'in|for|from|to|of|with|via|through|using|as|by|at|over|against|under|within|including|involving|representing|across|towards|between'
non_for_connectors_rx = 'in|of|on|to|from|with|via|through|using|as|by|at|over|against|under|within|including|involving|representing|across|towards|between'
non_to_connectors_rx = 'in|of|on|for|from|with|via|through|using|as|by|at|over|against|under|within|including|involving|representing|across|towards|between'
non_in_connectors_rx = 'to|of|on|for|from|with|via|through|using|as|by|at|over|against|under|within|including|involving|representing|across|towards|between'
non_as_connectors_rx = 'to|of|on|for|from|with|via|through|using|in|by|at|over|against|under|within|including|involving|representing|across|towards|between'
non_with_connectors_rx = 'to|of|on|for|from|as|via|through|using|in|by|at|over|against|under|within|including|involving|representing|across|towards|between'
non_through_connectors_rx = 'to|of|on|for|from|as|via|with|using|in|by|at|over|against|under|within|including|involving|representing|across|towards|between'
non_via_connectors_rx = 'to|of|on|for|from|as|through|with|using|in|by|at|over|against|under|within|including|involving|representing|across|towards|between'
non_using_connectors_rx = 'to|of|on|for|from|as|through|with|via|in|by|at|over|against|under|within|including|involving|representing|across|towards|between'
non_by_connectors_rx = 'to|of|on|for|from|as|through|with|via|in|using|at|over|against|under|within|including|involving|representing|across|towards|between'
non_at_connectors_rx = 'to|of|on|for|from|as|through|with|via|in|using|by|over|against|under|within|including|involving|representing|across|towards|between'
non_over_connectors_rx = 'to|of|on|for|from|as|through|with|via|in|using|by|at|against|under|within|including|involving|representing|across|towards|between'
non_under_connectors_rx = 'to|of|on|for|from|as|through|with|via|in|using|by|at|over|against|within|including|involving|representing|across|towards|between'
non_including_connectors_rx = 'to|of|on|for|from|as|through|with|via|in|using|by|at|over|against|under|within|involving|representing|across|towards|between'
non_involving_connectors_rx = 'to|of|on|for|from|as|through|with|via|in|using|by|at|over|against|under|within|including|representing|across|towards|between'
non_across_connectors_rx = 'to|of|on|for|from|as|through|with|via|in|using|by|at|over|against|under|within|including|involving|representing|towards|between'
non_against_connectors_rx = 'to|of|on|for|from|as|through|with|via|in|using|by|at|over|under|within|including|involving|representing|across|towards|between'
non_within_connectors_rx = 'to|of|on|for|from|as|through|with|via|in|using|by|at|over|against|under|including|involving|representing|across|towards|between'
non_representing_connectors_rx = 'to|of|on|for|from|as|through|with|via|in|using|by|at|over|against|under|within|including|involving|across|towards|between'
non_towards_connectors_rx = 'to|of|on|for|from|as|through|with|via|in|using|by|at|over|against|under|within|including|involving|across|representing|between'
non_between_connectors_rx = 'to|of|on|for|from|as|through|with|via|in|using|by|at|over|against|under|within|including|involving|across|representing|towards'

connectors_rx = 'to|of|on|for|from|with|by|via|through|using|in|as|over|against|within|under|at|including|towards|across|involving|representing|between'
connectors_list = ['to', 'of', 'on', 'for', 'from', 'with', 'by', 'via', 'through', 'using', 'in', 'as']

phrasal_connectors_rx = 'applied to'

question_words = 'how|what|when|where|which|who|whom|whose|why|can|would|should'

def system_solution(part0, part1):
	v = ending(part0.lower(), 'system')
	resource, solution = resource_or_solution(part1)
	return v and solution

def task_dataset_match(phrase):
	return re.match(".*?(([A-Z][A-Z])|([a-z][A-Z])|[\-\d+]).*", phrase)
		
def research_problem_suffixes(phrase):
	return re.match(".*((ing|ion)|(tics|ment|logy|reference|fer|sor|ser|yzer(s)?|lysis)$)", phrase)

def get_solution_or_resource(phrase):	
	if re.match("^.*(ing|ion|pproach)(\b|$)", phrase):
		return phrase, ""
	else:
		return "", phrase

def contains_ion_ing(phrase):
	return re.match('^.*(ion|ing)', phrase)

def ends_ion_ing(phrase):
	return re.match('^.*(ion|ing)$', phrase)
	
def has_specialcase(phrase):
	return not re.match('^.*([a-z][A-Z]|[A-Z][A-Z]|\d+).*', phrase) is None

def get_info_exactly_one_connector(phrase):
	phrase = phrase.lower()
	if contains_one_connector(phrase, 'of', non_of_connectors_rx):
		return 'of'
	elif contains_one_connector(phrase, 'from', non_from_connectors_rx):
		return 'from'
	elif contains_one_connector(phrase, 'on', non_on_connectors_rx):
		return 'on'
	elif contains_one_connector(phrase, 'for', non_for_connectors_rx):
		return 'for'
	elif contains_one_connector(phrase, 'to', non_to_connectors_rx):
		return 'to'
	elif contains_one_connector(phrase, 'in', non_in_connectors_rx):
		return 'in'
	elif contains_one_connector(phrase, 'as', non_as_connectors_rx):
		return 'as'
	elif contains_one_connector(phrase, 'with', non_with_connectors_rx):
		return 'with'
	elif contains_one_connector(phrase, 'through', non_through_connectors_rx):
		return 'through'
	elif contains_one_connector(phrase, 'via', non_via_connectors_rx):
		return 'via'
	elif contains_one_connector(phrase, 'using', non_using_connectors_rx):
		return 'using'
	elif contains_one_connector(phrase, 'by', non_by_connectors_rx):
		return 'by'
	elif contains_one_connector(phrase, 'over', non_over_connectors_rx):
		return 'over'
	elif contains_one_connector(phrase, 'against', non_against_connectors_rx):
		return 'against'
	elif contains_one_connector(phrase, 'within', non_within_connectors_rx):
		return 'within'
	elif contains_one_connector(phrase, 'under', non_under_connectors_rx):
		return 'under'
	elif contains_one_connector(phrase, 'at', non_at_connectors_rx):
		return 'at'
	elif contains_one_connector(phrase, 'including', non_including_connectors_rx):
		return 'including'
	elif contains_one_connector(phrase, 'towards', non_towards_connectors_rx):
		return 'towards'
	elif contains_one_connector(phrase, 'across', non_across_connectors_rx):
		return 'across'
	elif contains_one_connector(phrase, 'involving', non_involving_connectors_rx):
		return 'involving'
	elif contains_one_connector(phrase, 'representing', non_representing_connectors_rx):
		return 'representing'
	elif contains_one_connector(phrase, 'between', non_between_connectors_rx):
		return 'between'
	else:
		return None	
		
def contains_one_connector(phrase, connector, non_connector_candidate_rx):
	return (' '+connector+' ' in phrase and not re.match('^.* ('+non_connector_candidate_rx+') ', phrase))

def contains_any_element(phrase, rx):
	return re.match('^.* ('+rx+') ', phrase)
	
def ending(phrase, end):
	return not re.match('^.*?('+end+')$', phrase) is None
	
def matches(rx, phrase):	
	return not re.match('^('+rx+')', phrase) is None

def starts_phrase(rx, phrase):
	return not re.match('^('+rx+').*? ', phrase) is None
	
def begins_phrase(rx, phrase):
	return not re.match('^('+rx+') ', phrase) is None
	
def split_length(phrase, splitter):
	return len(phrase.split(splitter))
	
def substring_split(phrase, splitter):
	i = phrase.find(splitter)
	part_0 = phrase[0:i]
	part_1 = phrase[i+len(splitter):]
	return part_0, part_1	
	
def first_word_ending(rx, phrase):
	return not re.match('^[^ ]*('+rx+') ', phrase) is None
	
def second_word_ending(rx, phrase):
	return not re.match('^[a-zA-Z]+?\s[a-zA-Z]+?('+rx+') ', phrase) is None
		
def find_index_of_any(rx, phrase):
	for m in re.finditer(' ('+rx+') ', phrase):
		return m.start()
	return -1

def non_content_start(phrase_lower):
	phrase_tokens = phrase_lower.split(' ')
	return re.match('^('+generic_terms_rx+') ', phrase_lower) or \
	(re.match('^('+generic_starter_rx+')$', phrase_tokens[0]) and (len(phrase_tokens) > 1 and re.match('^('+generic_terms_rx+')$', phrase_tokens[1]))) or \
	'system description' in phrase_lower
	
def non_content(phrase, phrase_lower):
	phrase_tokens = phrase_lower.split(' ')
	length = len(phrase_tokens)
	if 'shortcuts' == phrase_lower or 'insights' == phrase_lower or 'predictions' == phrase_lower or 'algorithms' == phrase_lower or 'simulation and real-world evaluation' == phrase_lower or 'description and evaluation' == phrase_lower or 'optimization and evaluation' == phrase_lower or 'design implementation and evaluation' == phrase_lower or 'design and performance evaluation' == phrase_lower or 'generation and evaluation' == phrase_lower or 'design evaluation and analysis' == phrase_lower or 'creation and evaluation' == phrase_lower or 'algorithmic aspects' == phrase_lower or 'approximation algorithms' == phrase_lower or 'algorithmic design' == phrase_lower or 'its applications' == phrase_lower or 'some properties' == phrase_lower or 'in the field monitoring' == phrase_lower or 'advances' == phrase_lower or 'expressiveness and completeness' == phrase_lower or 'performance investigation' == phrase_lower or 'refinement and coarsening' == phrase_lower or 'various solutions' == phrase_lower or 'study' == phrase_lower or \
	'analytical evaluation' == phrase_lower or 'end-to-end evaluation' == phrase_lower or 'realistic evaluation' == phrase_lower or 'evaluation validity' == phrase_lower or 'approximate evaluation' == phrase_lower or 'framework and resources' == phrase_lower or 'fast evaluation' == phrase_lower or 'evaluation system' == phrase_lower or 'comprehensive evaluation' == phrase_lower or 'consistency' == phrase_lower or 'performance comparison' == phrase_lower or 'state' == phrase_lower or 'products' == phrase_lower or 'complexity' == phrase_lower or 'comparative evaluation and analysis' == phrase_lower or 'implementation and evaluation' == phrase_lower or 'applications' == phrase_lower or 'performance analysis and optimization' == phrase_lower or 'introduction' in phrase_lower or 'laws' == phrase_lower or 'computation' == phrase_lower or 'grand challenge' == phrase_lower or 'constructions' == phrase_lower or 'introduction' == phrase_lower or 'various improvements' == phrase_lower or 'counterexample' == phrase_lower or 'some connections' == phrase_lower or \
	'design and evaluation' == phrase_lower or 'evaluation strategies' == phrase_lower or 'empirical evaluation' == phrase_lower or 'evaluation and improvement' == phrase_lower or 'pros and cons' == phrase_lower or 'analysis and evaluation' == phrase_lower or 'accessibility evaluation' == phrase_lower or 'measurement and evaluation' == phrase_lower or 'deployment and evaluation' == phrase_lower or 'robust evaluations' == phrase_lower or 'practical evaluation' == phrase_lower or 'reproducible evaluation' == phrase_lower or 'experimental evaluation' == phrase_lower or 'faster evaluation' == phrase_lower or 'practice' == phrase_lower or 'its expressions' == phrase_lower or 'concentration' == phrase_lower or 'unified management and optimization' == phrase_lower or 'trends' == phrase_lower or 'new developments' == phrase_lower or 'reachability analysis' == phrase_lower or 'superiority' == phrase_lower or 'conclusions' == phrase_lower or 'solutions' == phrase_lower or 'some modifications' == phrase_lower or 'variations' == phrase_lower or \
	'back and forth' == phrase_lower or 'properties' == phrase_lower or 'status' == phrase_lower or 'empirical analysis' == phrase_lower or 'performances' == phrase_lower or 'development' == phrase_lower or 'productivity' == phrase_lower or 'a novel approach' == phrase_lower or 'a holistic approach' == phrase_lower or 'a general framework' == phrase_lower or 'refinement and verification' == phrase_lower or 'correct composition' == phrase_lower or 'design and development' == phrase_lower or 'theoretical aspects' == phrase_lower or 'goal conflict' == phrase_lower or 'analytical study' == phrase_lower or 'deployment challenges' == phrase_lower or 'acceleration' == phrase_lower or 'compressed representations' == phrase_lower or 'simulations' == phrase_lower or 'an unknown environment' == phrase_lower or 'interception' == phrase_lower or 'capacity' == phrase_lower or 'avoidability' == phrase_lower or 'efficiency and validity' == phrase_lower or 'some efficient solutions' == phrase_lower or 'extended' == phrase_lower or \
	'system identification' == phrase_lower or 'design and analysis' == phrase_lower or 'a simple way' == phrase_lower or 'a new approach' == phrase_lower or 'an efficient method' == phrase_lower or 'design and implementation' == phrase_lower or 'security implications' == phrase_lower or 'analysis and implementation' == phrase_lower or 'analysis and control' == phrase_lower or 'verification and control' == phrase_lower or 'practical aspects' == phrase_lower or 'improved estimation' == phrase_lower or 'research and simulation' == phrase_lower or 'technical report' == phrase_lower or 'optimal strategies' == phrase_lower or 'alternative interpretation' == phrase_lower or 'secrecy capacities' == phrase_lower or 'configuration models' == phrase_lower or 'recent advances' == phrase_lower or 'entanglement' == phrase_lower or 'delay and redundancy' == phrase_lower or 'stability and control' == phrase_lower or 'new ways' == phrase_lower or 'reaction' == phrase_lower or 'ability' == phrase_lower or 'restrictions' == phrase_lower or \
	'attack and defense' == phrase_lower or 'promises and challenges' == phrase_lower or 'system description' in phrase_lower or 'improvements and experiments' == phrase_lower or 'performance analysis' == phrase_lower or 'performance evaluation' == phrase_lower or 'fast reconstruction' == phrase_lower or 'user capacity' == phrase_lower or 'estimation and verification' == phrase_lower or 'security' == phrase_lower or 'fundamental limits' == phrase_lower or 'experimental analysis' == phrase_lower or 'incentives and coordination' == phrase_lower or 'design discussion' == phrase_lower or 'local guarantees' == phrase_lower or 'comparison' == phrase_lower or 'easy and fast design and implementation' == phrase_lower or 'connectivity' == phrase_lower or 'requirements issues' == phrase_lower or 'exploration vs. exploitation' == phrase_lower or 'optimised maintenance' == phrase_lower or 'properties and constructions' == phrase_lower or 'one more way' == phrase_lower or 'some improvements' == phrase_lower:
		return True	
	elif length == 1:
		return re.match('^('+generic_terms_rx+')$', phrase_lower)
	elif length == 2:
		return (re.match('^('+generic_starter_rx+')$', phrase_tokens[0]) and re.match('^('+generic_terms_rx+')$', phrase_tokens[1]))
	#elif length == 3:
	#	return re.match('^('+generic_starter_rx+')', phrase_tokens[0]) and re.match('^('+generic_terms_rx+')', phrase_tokens[2]) and not (task_dataset_match(phrase.split(' ')[1]) or 'coreference' == phrase_tokens[1] or 'database' == phrase_tokens[2] or 'corpus' == phrase_tokens[2])
	return False

def remove_and_ending(phrase):
	if ' ' in phrase and ending(phrase, 'and'):
		i = phrase.rindex(' ')
		phrase = phrase[0:i].strip()
	return phrase
	
def resources_lite(phrase):
	phrase = remove_and_ending(phrase)
	phrase_toks = phrase.split(' ')
	return (len(phrase_toks) == 1 and is_resource(phrase.lower())) or \
	(len(phrase_toks) >= 2 and re.match('^('+domains_rx+')', phrase_toks[0].lower()) and is_resource(phrase_toks[len(phrase_toks)-1].lower())) or \
	(is_language(phrase_toks[0]) and is_resource(phrase_toks[len(phrase_toks)-1].lower()))
	
def is_resource(phrase):
	phrase = remove_and_ending(phrase)
	
	if non_content(phrase, phrase.lower()): return False
	
	return (not first_word_ending('ing|ion', phrase.lower()) and \
	(not ending(phrase, 'ion|ing|ment|tics|vity|vities') or 'information' in phrase) and \
	not begins_phrase('improve|compute|enhance|detect|manipulate|read|determine|leverage|recognise|embed|ask|planning|evaluate|support|suggest|fill|interface|represent|acquire|parse|build|recognize|query|find|identify|extract|explore|solve|locate|recommend|distribute|generate|learn|measure|construct|create|maintain|determine|decompose|enrich|overcome|answer|extend|detect|estimate|classify|predict|characterise|disambiguate|assign|cloze|analyze', phrase.lower()) and \
	(ending(phrase, resources_1_rx) or \
	ending(phrase, resources_2_rx) or \
	ending(phrase, resources_3_rx) or \
	ending(phrase, resources_4_rx) or \
	ending(phrase, resources_5_rx) or \
	ending(phrase, resources_6_rx) or \
	ending(phrase, resources_7_rx) or \
	(not has_specialcase(phrase) and ending(phrase, 's|es|ity') and not 'process' in phrase and not 'analysis' in phrase and not 'use' in phrase) or \
	ending(phrase, domains_rx))) or \
	(begins_phrase(places_rx, phrase) and ending(phrase, 'ion|ing|ment|tics|vity|vities'))

def is_living(phrase):
	phrase = remove_and_ending(phrase)
	
	if non_content(phrase, phrase.lower()): return False
	
	return ending(phrase, living_1_rx) or \
	ending(phrase, living_2_rx) or \
	ending(phrase, living_3_rx) or \
	begins_phrase(living_1_rx, phrase) or \
	begins_phrase(living_2_rx, phrase) or \
	begins_phrase(living_3_rx, phrase)

def is_language(phrase):
	phrase = remove_and_ending(phrase)
	phrase_toks = phrase.split(' ')	
	phrase_lower = phrase.lower()
	
	if len(phrase_toks) == 1 and re.match('^('+lang_rx+')$', phrase):
		return True	
	
	if 'corpus' in phrase_lower or 'corpora' in phrase_lower or 'case study' in phrase_lower or 'study' in phrase_lower or \
	'analysis' in phrase_lower or 'learners' in phrase_lower or 'machine' in phrase_lower or 'parsing' in phrase_lower or \
	'segmentation' in phrase_lower or 'twitter' in phrase_lower:
		return False
	
	if begins_phrase(lang_rx, phrase) and ' and ' in phrase and (not(is_research_problem(phrase) or is_resource(phrase)) or ending(phrase.lower(), 'language(s)?')):
		second_language_phrase = phrase.split(' and ')[1].lstrip()
		if not ' ' in second_language_phrase:
			second_language_phrase = second_language_phrase + ' '	
		return begins_phrase(lang_rx, second_language_phrase)
		
	if (len(phrase_toks) > 1 and re.match('^('+lang_rx+')$', phrase_toks[len(phrase_toks)-1])) or re.match('^('+lang_rx+')$', phrase):	
		return not is_research_problem(phrase)
						
	return (len(phrase_toks) >= 3 and not re.match('^('+generic_starter_rx+')', phrase_toks[0]) is None and \
	not re.match('^('+lang_rx+')', phrase_toks[1]) is None and ending(phrase, '(dialect|language)[s]?')) or \
	((begins_phrase(lang_rx, phrase) or begins_phrase(domains_rx, phrase.lower())) and ending(phrase.lower(), '(dialect|language)[s]?'))
	
def is_place(phrase):
	phrase = remove_and_ending(phrase)
	
	if non_content(phrase, phrase.lower()): return False
	
	return ending(phrase, places_rx)

def is_tool(phrase):
	phrase = remove_and_ending(phrase)
	
	if non_content(phrase, phrase.lower()): return False
	
	return ((not first_word_ending('ing|ion', phrase.lower()) or 'vision' in phrase.lower()) and \
	not begins_phrase('improve|compute|enhance|detect|manipulate|read|determine|leverage|recognise|embed|ask|planning|evaluate|support|suggest|fill|interface|represent|acquire|parse|build|recognize|query|find|identify|extract|explore|solve|locate|recommend|distribute|generate|learn|measure|construct|create|maintain|determine|decompose|enrich|overcome|answer|extend|detect|estimate|classify|predict|characterise|disambiguate|assign|cloze|analyze', phrase.lower())) and \
	(ending(phrase.lower(), tools_1_rx) or \
	ending(phrase.lower(), tools_2_rx) or \
	ending(phrase.lower(), tools_3_rx)) or \
	len(phrase) <= 3 or \
	'crf' in phrase.lower() or 'svm' in phrase.lower() or 'lstm' in phrase.lower() or 'toolkit' in phrase.lower() or \
	(has_specialcase(phrase) and not is_resource(phrase) and not 'MUC' in phrase and not 'US' in phrase and not 'Eval' in phrase and not 'task' in phrase.lower() and not ending(phrase.lower(), 'ion|ing|challenge') and not 'performance' in phrase.lower() and not first_word_ending('ing|ion', phrase.lower()))
	
def is_by_method(phrase):	
	phrase = remove_and_ending(phrase)
	
	if non_content(phrase, phrase.lower()): return False
	
	return ending(phrase.lower(), method_1_rx) or \
	ending(phrase.lower(), method_2_rx) or \
	ending(phrase.lower(), method_3_rx) or \
	ending(phrase.lower(), method_4_rx) or \
	(ending(phrase.lower(), 'ion|ing|ment|ness|tics|vity|vities') and not 'information' in phrase.lower()) or \
	first_word_ending('ing|ion', phrase.lower()) or \
	second_word_ending('ing|ion', phrase.lower())
	
def is_method(phrase):	
	phrase = remove_and_ending(phrase)
	
	if non_content(phrase, phrase.lower()) or 'evaluation method' in phrase.lower() or 'experimental evaluation' in phrase.lower(): return False
	
	return first_word_ending('supervized|supervised', phrase.lower()) or \
	ending(phrase.lower(), method_1_rx) or \
	ending(phrase.lower(), method_2_rx) or \
	ending(phrase.lower(), method_3_rx) or \
	ending(phrase.lower(), method_4_rx) or \
	(ending(phrase.lower(), 'ion|ing|ment|ness|tics|vity|vities|ism') and not 'information' in phrase.lower())
	
def is_dataset(phrase):
	if not non_content_start(phrase) and (ending(phrase, dataset_1_rx) or ' dataset ' in phrase or ' corpora ' in phrase or ' corpus ' in phrase):
		return True
	
def is_research_problem(phrase):
	phrase = remove_and_ending(phrase)
	if non_content(phrase, phrase.lower()):
		return False
	if ':' in phrase:
		phrase = phrase[0:phrase.find(':')]
	if first_word_ending(det_rx, phrase.lower()):
		phrase = phrase[phrase.find(' ')+1:]	
	return (ending(phrase.lower(), 'ion|ing|ment|tics|emy|logy|graphic|dence|style|syntax|charter|discovery|choice|system|systems|manager|triad|inference|causality|phenomena|problem(s)?|project|order|equivalence|domain|domains|analysis|similarity|task|track|review|architecture|research|search|retrieval|removal|medicine|control|flow|assembly|paradox') and not (ending(phrase.lower(), 'information') or is_living(phrase.lower()))) or \
	begins_phrase('improve|compute|enhance|detect|manipulate|read|determine|leverage|recognise|embed|ask|planning|evaluate|support|suggest|fill|interface|represent|acquire|parse|build|recognize|query|find|identify|extract|explore|solve|locate|recommend|distribute|generate|learn|measure|construct|create|maintain|determine|decompose|enrich|overcome|answer|extend|detect|estimate|classify|predict|characterise|disambiguate|assign|cloze|analyze', phrase.lower()) or \
	ending(phrase.lower(), fields) or \
	(not is_resource(phrase.lower()) and (has_specialcase(phrase) or (second_word_ending('ing|ion', phrase.lower()) and not second_word_ending('location', phrase.lower())))) or \
	(first_word_ending('ing|ion|ize', phrase.lower()) and not first_word_ending('location', phrase.lower()))

def has_ing_connector(phrase):
	tokens = phrase.split(' ')
	length = len(tokens)-1
	for x in range(length, 0, -1):
		if re.match('^.*(ing)$', tokens[x]):
			return tokens[x]
	return ""
	
	
def resource_or_solution_or_language(phrase):
	resource = []
	solution = []
	language = []
	phrase_lower = phrase.lower()
	if is_language(phrase):
		language.append(phrase)
	elif ending(phrase.split(' ')[0], 'ing'):
		solution.append(phrase)
	elif is_resource(phrase.lower()):
		resource.append(phrase)
	elif not is_living(phrase_lower) and not is_place(phrase_lower) and not ending(phrase_lower, non_content_words_rx):
		solution.append(phrase)
	return resource, solution, language

def language_or_tool_or_resource(phrase):
	language = []
	tool = []
	resource = []
	phrase_lower = phrase.lower()
	if is_language(phrase):
		language.append(phrase)
	elif is_tool(phrase):
		tool.append(phrase)
	elif is_resource(phrase_lower):
		resource.append(phrase)		
	return language, tool, resource	

def language_or_dataset_or_tool_or_method_or_resource(phrase):
	language = []
	dataset = []
	tool = []
	method = []
	resource = []
	phrase_lower = phrase.lower()
		
	if is_language(phrase):
		language.append(phrase)
	elif is_dataset(phrase_lower):
		dataset.append(phrase)
	elif is_tool(phrase):
		tool.append(phrase)
	elif is_method(phrase):
		method.append(phrase)
	elif is_resource(phrase_lower):
		resource.append(phrase)
	return language, dataset, tool, method, resource

def language_or_dataset_or_tool_or_resource(phrase):
	language = []
	dataset = []
	tool = []
	resource = []
	phrase_lower = phrase.lower()
	if is_language(phrase):
		language.append(phrase)
	elif is_dataset(phrase_lower):
		dataset.append(phrase)
	elif is_tool(phrase):
		tool.append(phrase)
	elif is_resource(phrase_lower):
		resource.append(phrase)
	return language, dataset, tool, resource
	
def language_or_tool_or_method_or_resource(phrase):
	language = []
	tool = []
	method = []
	resource = []
	phrase_lower = phrase.lower()
	if is_language(phrase):
		language.append(phrase)
	elif is_tool(phrase):
		tool.append(phrase)
	elif is_method(phrase):
		method.append(phrase)
	elif is_resource(phrase_lower):
		resource.append(phrase)		
	return language, tool, method, resource

def language_or_method_or_resource_or_rp(phrase):
	language = []
	method = []
	resource = []
	research_problem = []
	phrase_lower = phrase.lower()
	if is_language(phrase):
		language.append(phrase)
	elif is_method(phrase):
		method.append(phrase)
	elif is_resource(phrase_lower):
		resource.append(phrase)
	elif is_research_problem(phrase):
		research_problem.append(phrase)		
	return language, method, resource, research_problem	
	
def language_or_dataset_or_method_or_resource_or_rp(phrase):
	language = []
	dataset = []
	method = []
	resource = []
	research_problem = []
	phrase_lower = phrase.lower()
	if is_language(phrase):
		language.append(phrase)
	elif is_dataset(phrase_lower):
		dataset.append(phrase)
	elif is_method(phrase):
		method.append(phrase)
	elif is_resource(phrase_lower):
		resource.append(phrase)
	elif is_research_problem(phrase):
		research_problem.append(phrase)		
	return language, dataset, method, resource, research_problem
	
def language_or_dataset_or_tool_or_method_or_resource_or_rp(phrase):
	language = []
	dataset = []
	tool = []
	method = []
	resource = []
	research_problem = []
	phrase_lower = phrase.lower()
	if is_language(phrase):
		language.append(phrase)
	elif is_dataset(phrase_lower):
		dataset.append(phrase)
	elif is_tool(phrase):
		tool.append(phrase)
	elif is_method(phrase):
		method.append(phrase)
	elif is_resource(phrase_lower):
		resource.append(phrase)
	elif is_research_problem(phrase):
		research_problem.append(phrase)		
	return language, dataset, tool, method, resource, research_problem
	
def language_or_tool_or_method_or_resource_or_rp(phrase):
	language = []
	tool = []
	method = []
	resource = []
	research_problem = []
	phrase_lower = phrase.lower()
	if is_language(phrase):
		language.append(phrase)
	elif is_tool(phrase):
		tool.append(phrase)
	elif is_method(phrase):
		method.append(phrase)
	elif is_resource(phrase_lower):
		resource.append(phrase)
	elif is_research_problem(phrase):
		research_problem.append(phrase)		
	return language, tool, method, resource, research_problem

def language_or_tool_or_dataset_or_rp_or_method_or_resource(phrase):
	language = []
	tool = []
	dataset = []
	research_problem = []	
	method = []
	resource = []
	phrase_lower = phrase.lower()
	if is_language(phrase):
		language.append(phrase)
	elif is_tool(phrase):
		tool.append(phrase)
	elif is_dataset(phrase):
		dataset.append(phrase)
	elif is_research_problem(phrase):
		research_problem.append(phrase)			
	elif is_method(phrase):
		method.append(phrase)
	elif is_resource(phrase_lower):
		resource.append(phrase)
	return language, tool, dataset, research_problem, method, resource	
	
def rp_or_language_or_tool_or_method_or_resource(phrase):
	research_problem = []
	language = []
	tool = []
	method = []
	resource = []
	phrase_lower = phrase.lower()
	if is_research_problem(phrase):
		research_problem.append(phrase)	
	elif is_language(phrase):
		language.append(phrase)
	elif is_tool(phrase):
		tool.append(phrase)
	elif is_method(phrase):
		method.append(phrase)
	elif is_resource(phrase_lower):
		resource.append(phrase)
	return research_problem, language, tool, method, resource

def get_scientific_knowledge_elements(phrase):
	solution = []
	research_problem = []
	resource = []
	language = []
	if not non_content(phrase, phrase.lower()):
		if is_research_problem(phrase):
			research_problem.append(phrase)
		else:
			resource, solution, language = resource_or_solution_or_language(phrase)
	return solution, research_problem, resource, language

def get_scientific_knowledge_elements_all(phrase):
	solution = []
	research_problem = []
	resource = []
	language = []
	tool = []
	method = []
	if not non_content(phrase, phrase.lower()):
		if is_tool(phrase):
			tool.append(phrase)
		elif is_method(phrase):
			method.append(phrase)
		elif is_research_problem(phrase):
			research_problem.append(phrase)
		else:
			resource, solution, language = resource_or_solution_or_language(phrase)
	return solution, research_problem, resource, language, tool, method

def extend_lists_small(list1, l1, list2, l2, list3, l3):
	if l1:
		list1.extend(l1)
	if l2:
		list2.extend(l2)
	if l3:
		list3.extend(l3)
	return list1, list2, list3
	
def extend_lists(list1, l1, list2, l2, list3, l3, list4, l4):
	if l1:
		list1.extend(l1)
	if l2:
		list2.extend(l2)
	if l3:
		list3.extend(l3)
	if l4:
		list4.extend(l4)
	return list1, list2, list3, list4

def extend_lists_five(list1, l1, list2, l2, list3, l3, list4, l4, list5, l5):
	if l1:
		list1.extend(l1)
	if l2:
		list2.extend(l2)
	if l3:
		list3.extend(l3)
	if l4:
		list4.extend(l4)
	if l5:
		list5.extend(l5)
	return list1, list2, list3, list4, list5
	
def extend_lists_all(list1, l1, list2, l2, list3, l3, list4, l4, list5, l5, list6, l6):
	if l1:
		list1.extend(l1)
	if l2:
		list2.extend(l2)
	if l3:
		list3.extend(l3)
	if l4:
		list4.extend(l4)
	if l5:
		list5.extend(l5)
	if l6:
		list6.extend(l6)
	return list1, list2, list3, list4, list5, list6
	
def extend_lists_seven(list1, l1, list2, l2, list3, l3, list4, l4, list5, l5, list6, l6, list7, l7):
	if l1:
		list1.extend(l1)
	if l2:
		list2.extend(l2)
	if l3:
		list3.extend(l3)
	if l4:
		list4.extend(l4)
	if l5:
		list5.extend(l5)
	if l6:
		list6.extend(l6)
	if l7:
		list7.extend(l7)
	return list1, list2, list3, list4, list5, list6, list7
	
	
def find_first_occurence(list, phrase):
	indexes = []
	for element in list:
		if ' '+element+' ' in phrase:
			indexes.append(phrase.find(' '+element+' '))
	if not indexes: return -1
	else: return min(indexes)
		
def get_list_of_connector_indexes(phrase, rx):
	indexes = []
	for m in re.finditer(' ('+rx+') ', phrase):
		indexes.append(m.start())
		#print(str(m.start())+"||"+str(m.group()))
	return indexes

def to_pronoun(phrase):
	return re.match('.*to ('+pronoun_rx+')', phrase)

def start_ing(phrase):	
	token = phrase.split(' ')[0]
	return re.match('^.*(ing)$', token)
		
def determiner_start(phrase):
	return begins_phrase(det_rx, phrase)
	
def get_length_without_determiners(phrase):
	if begins_phrase(det_rx, phrase):
		phrase = phrase[phrase.find(' ')+1:]
	return len(phrase.split(' '))
	
def get_string(phrase, start_index):
	str = phrase[start_index+1:]
	str = str[0:str.find(' ')]
	return str
	
def preprocess(phrase):
	
	if re.match('.*\)$', phrase):
		i = phrase.rfind('(')
		if phrase[i-1:i] == ' ':
			phrase = phrase[0:i-1]
		
	phrase = phrase.replace('as a Basis for', 'for')
	phrase = phrase.replace('as a basis for', 'for')
	phrase = phrase.replace('as Basis for', 'for')
	phrase = phrase.replace('as basis for', 'for')
	phrase = phrase.replace('on the basis of', 'of')
	phrase = phrase.replace('to be of', 'of')
	phrase = phrase.replace(' Based on ', ' on ')
	phrase = phrase.replace(' based on ', ' on ')
	phrase = phrase.replace(' Extracted from ', ' from ')
	phrase = phrase.replace(' Focused on ', ' on ')
	phrase = phrase.replace(' Annotated with ', ' with ')
	phrase = phrase.replace(' dedicated to ', ' for ')
	phrase = phrase.replace(' to Study ', ' for ')
	phrase = phrase.replace(' built from ', ' from ')
	phrase = phrase.replace(' by means of ', ' using ')
	phrase = phrase.replace(' by using ', ' using ')
	phrase = phrase.replace(' straight out of ', ' from ')
	phrase = phrase.replace(' Implemented in ', ' in ')
	phrase = phrase.replace(' implemented in ', ' in ')
	phrase = phrase.replace(' Written in ', ' in ')
	phrase = phrase.replace('Towards ', '')
	phrase = phrase.replace(' into ', ' in ')
	phrase = phrase.replace(' Into ', ' in ')
	phrase = phrase.replace(' in on ', ' in ')
	phrase = phrase.replace(' at over ', ' over ')
	if 'for using and' in phrase.lower():
		phrase = phrase.lower().replace('for using and', 'for')
	if 'for using' in phrase.lower():
		phrase = phrase.lower().replace('for using', 'for')
	phrase = phrase.replace(' for representing ', ' for ')
	phrase = phrase.replace(' for Representing ', ' for ')
	phrase = phrase.replace('as Used for', 'for').replace('as Used For', 'for')
	phrase = phrase.replace('Used for', 'for')
	phrase = phrase.replace('in a tool for', 'for')
	phrase = phrase.replace('for the Development of', 'for')
	phrase = phrase.replace('for Development of', 'for')
	phrase = phrase.replace('for Representing and Using', 'for')
	phrase = phrase.replace('for Use in', 'for')
	phrase = phrase.replace('to develop', 'for')
	phrase = phrase.replace('Trained using', 'using')
	phrase = phrase.replace('`', '')
	phrase = phrase.replace('\'', '')
	phrase = phrase.replace(' - ', ' ')
	phrase = phrase.replace(' in Light of ', ' in ')
	phrase = phrase.replace(' about ', ' on ')
	phrase = phrase.replace(' About ', ' on ')
	phrase = phrase.replace(' -- ', ': ')
	phrase = phrase.replace('---', ': ')
	phrase = phrase.replace(' : ', ': ')
	phrase = phrase.replace(' Used as ', ' as ')
	phrase = phrase.replace('On the Utility of', 'On')
	phrase = phrase.replace('Defined on', 'on')
	phrase = phrase.replace('Left to Right Parsing', 'Left-to-Right Parsing')
	phrase = phrase.replace('used for', 'for')
	phrase = phrase.replace('Augmented with', 'with')
	phrase = phrase.replace('Intermediated by', 'with')
	phrase = phrase.replace('Based On', 'on')
	phrase = phrase.replace('Built From', 'from')
	phrase = phrase.replace('induced from', 'from')
	phrase = phrase.replace('Induced from', 'from')
	phrase = phrase.replace('obtained from', 'from')
	phrase = phrase.replace('Extracted From', 'from')
	phrase = phrase.replace('Generated from', 'from')
	phrase = phrase.replace('Acquired from', 'from')
	phrase = phrase.replace('acquired from', 'from')
	phrase = phrase.replace('Retrieved from', 'from')
	phrase = phrase.replace('Populated from', 'from')
	phrase = phrase.replace('Mined from', 'from')
	phrase = phrase.replace('Selected from', 'from')
	phrase = phrase.replace('Learned from', 'from')
	phrase = phrase.replace('collected from', 'from')
	phrase = phrase.replace('Derived from', 'from')
	phrase = phrase.replace('Stated in', 'in')
	phrase = phrase.replace('expressed in', 'in')
	phrase = phrase.replace(' Used in ', ' in ')
	phrase = phrase.replace('Concept to Speech', 'Concept-to-Speech')
	phrase = phrase.replace('Grapheme to Phoneme', 'Grapheme-to-Phoneme')
	phrase = phrase.replace('Phoneme to Grapheme', 'Phoneme-to-Grapheme')
	phrase = phrase.replace('Learning to Rank', 'Learning-to-Rank')
	phrase = phrase.replace('Learning to rank', 'Learning-to-rank')
	phrase = phrase.replace('learning to rank', 'learning-to-rank')
	phrase = phrase.replace('Learning to Find', 'Learning-to-Find')
	phrase = phrase.replace('Learning to Order', 'Learning-to-Order')
	phrase = phrase.replace('Learning to Compose', 'Learning-to-Compose')
	phrase = phrase.replace('Learning to Extract', 'Learning-to-Extract')
	phrase = phrase.replace('Learning to Map', 'Learning-to-Map')
	phrase = phrase.replace('Learning to Model', 'Learning-to-Model')
	phrase = phrase.replace(' text to dialogue', 'text-to-dialogue')
	phrase = phrase.replace('Sum of Squares', 'Sum-of-Squares')
	phrase = phrase.replace('Textextt to 3D', 'Text-to-3D')
	phrase = phrase.replace('Sequence to Sequence', 'Sequence-to-Sequence')
	phrase = phrase.replace('as Applied to', 'applied to')
	phrase = phrase.replace('when applied to', 'applied to')
	phrase = phrase.replace('Designed to', 'to')
	phrase = phrase.replace('Referring to', 'for')
	phrase = phrase.replace('to Enable', 'for')
	phrase = phrase.replace('according to', 'on')
	phrase = phrase.replace('Seen as', 'as')
	phrase = phrase.replace('Represented as', 'as')
	phrase = phrase.replace('by Using', 'using')
	phrase = phrase.replace('through Using', 'using')
	phrase = phrase.replace('with Applications to', 'for')
	phrase = phrase.replace('with application to', 'for')
	phrase = phrase.replace('with Application to', 'for')
	phrase = phrase.replace('Part of Speech', 'Part-of-Speech')
	phrase = phrase.replace('Time to Event', 'Time-to-Event')
	phrase = phrase.replace('Image to Text', 'Image-to-Text')
	phrase = phrase.replace('Bag of Words', 'Bag-of-Words')
	phrase = phrase.replace('Letter to Sound', 'Letter-to-Sound')
	phrase = phrase.replace('Learning to ', 'Learning-to-')
	phrase = phrase.replace('term to term', 'term-to-term')
	phrase = phrase.replace('Text to Speech', 'Text-to-Speech')
	phrase = phrase.replace('Constituency to Dependency', 'Constituency-to-Dependency')
	phrase = phrase.replace('designed for', 'for')
	phrase = phrase.replace('with and for', 'for')
	phrase = phrase.replace('as means of', 'for')
	phrase = phrase.replace('by Means of', 'by')
	phrase = phrase.replace('to Perform', 'for')
	phrase = phrase.replace('Built using', 'using')
	phrase = phrase.replace('on the Use of', 'on')
	phrase = phrase.replace('for Obtaining a for', 'for')
	phrase = phrase.replace(' Pronounced by ', ' by ')
	phrase = phrase.replace(' Powered by ', ' by ')
	phrase = phrase.replace(' Guided by ', ' by ')
	phrase = phrase.replace(' operated by ', ' by ')
	phrase = phrase.replace(' at Scale ', ' atScale ')
	phrase = phrase.replace(' at scale ', ' atscale ')
	phrase = phrase.replace(' based in ', ' in ')
	phrase = phrase.replace(', ', ' ')
	phrase = phrase.replace(' upon ', ' on ')
	phrase = phrase.replace('- Extended Abstract', '')
	phrase = phrase.replace('ORDER BY', 'ORDER-BY')
	phrase = phrase.replace('Learning with ', 'Learning ')
	phrase = phrase.replace(' predicated on ', ' on ')
	phrase = phrase.replace(' when Applying ', ' using ')
	phrase = phrase.replace(' applied to ', ' for ')
	phrase = phrase.replace(' Applied to ', ' for ')
	phrase = phrase.replace(' Apply to ', ' for ')
	phrase = phrase.replace(' Adapted to ', ' for ')
	phrase = phrase.replace(' Related to ', ' for ')
	phrase = phrase.replace(' Dedicated to ', ' for ')
	phrase = phrase.replace(' related to ', ' for ')
	phrase = phrase.replace(' Applied To ', ' for ')
	phrase = phrase.replace(' Assigned To ', ' for ')
	phrase = phrase.replace(' assigned to ', ' for ')
	phrase = phrase.replace(' contributing to ', ' for ')
	phrase = phrase.replace(' helps to beat ', ' for ')
	phrase = phrase.replace(' associated to ', ' for ')
	phrase = phrase.replace(' robust to ', ' for ')
	phrase = phrase.replace(' to Support ', ' for ')
	phrase = phrase.replace(' to support ', ' for ')
	phrase = phrase.replace(' to determine ', ' for ')
	phrase = phrase.replace(' lead to ', ' for ')
	phrase = phrase.replace(' Given ', ' from ')
	phrase = phrase.replace(' given ', ' from ')
	phrase = phrase.replace('State of the Art', 'State-of-the-Art')
	phrase = phrase.replace(' Inspired from ', ' from ')
	phrase = phrase.replace(' Proposed to ', ' for ')
	phrase = phrase.replace(' emerge from ', ' from ')
	phrase = phrase.replace(' subject to ', ' for ')
	phrase = phrase.replace('Peer to Peer ', 'Peer-to-Peer ')
	phrase = phrase.replace('Image to Image', 'Image-to-Image')
	phrase = phrase.replace('Segment to Segment', 'Segment-to-Segment')
	phrase = phrase.replace('Online to Offline', 'Online-to-Offline')
	phrase = phrase.replace('Function to Function', 'Function-to-Function')
	phrase = phrase.replace('Learn to Solve', 'Learn-to-Solve')
	phrase = phrase.replace('End to End ', 'End-to-End ')
	phrase = phrase.replace(' Subject to ', ' for ')
	if 'partner and service' in phrase.lower():
		phrase = phrase.replace('Partner and Service', 'Partner-and-Service')
	if begins_phrase('On', phrase):
		phrase = re.sub('On ', '', phrase, count=1)
	if begins_phrase('Learning to', phrase):
		phrase = re.sub('Learning to ', 'Learning-to-', phrase, count=1)
	if begins_phrase('Building and using', phrase):
		phrase = re.sub('Building and using ', 'Using ', phrase, count=1)
	
	if ending(phrase, '\\.'):
		phrase = phrase[0:len(phrase)-1]
	
	return phrase
			