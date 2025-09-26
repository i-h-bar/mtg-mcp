GET_RULE = """select * from mtg_rule where rule_number = $1;"""

GET_SECTION = """select *
                 from mtg_rule
                          join mtg_rule_subsection on mtg_rule.subsection_id = mtg_rule_subsection.id
                 where mtg_rule_subsection.section_id = $1
                 order by rule_number
                 limit $2 offset $3;"""

GET_SUBSECTION = """select *
                    from mtg_rule
                    where subsection_id = $1;"""

GET_DEFINITION = """select *, similarity(term, $1) as sml
                    from mtg_glossary
                    where term % $1
                    order by sml
                    limit 1;"""
