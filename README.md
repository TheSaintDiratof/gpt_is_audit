This is a python module and script that uses g4f for ask GPT about somewhat that you put in stdin
Usage:
$ llm_audit -m "model" -a "addition for question" -p "prefix for question" -r "role" < code # Request for gpt is intro+stdin+addition

$ llm_audit -l # List all models

Also you might to use this as module


import llm_audit
llm_audit.ask_llm(intro, code, addition, model)
