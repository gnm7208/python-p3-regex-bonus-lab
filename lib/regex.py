import re

# Pattern matches exactly three specific strings using alternation (|)
# Each string is matched literally with special characters escaped
my_pattern = r"It's such a lovely day today\.|Some weather we're having today, huh\?|Maybe today's just not my day\."
my_regex = re.compile(my_pattern)

