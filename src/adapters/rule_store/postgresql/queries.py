GET_RULE = """select * from mtg_rules where rule_number = $1;"""

GET_SECTION = """select * from mtg_rules where section_number = $1;"""

GET_SUBSECTION = """select * from mtg_rules where subsection_number = $1;"""