GET_RULE = """select * from mtg_rules where rule_number = $1;"""

GET_SECTION = """select * from mtg_rules where section_number = $1;"""

GET_SUBSECTION = """select * from mtg_rules where subsection_number = $1;"""

GET_DEFINITION = """select *, similarity(term, $1) as sml
                    from mtg_glossary
                    where term % $1
                    order by sml
                    limit 1;"""