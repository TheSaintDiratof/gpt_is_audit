### This is a python module and script that uses g4f for ask GPT about somewhat that you put in stdin
# Usage:
``` Bash
# Default model is llama_70b
# Default addition is none
# Default prefix is "There is a piece of code. Show me vulnerabilities in this code. Answer like \"$line_number $what_kind_of_vulnerability $way_to_fix\""
# Default role is "user"

$ llm_audit -m "model" -a "addition for question" -p "prefix for question" -r "role" < file_with_code # Request for LLM is intro+stdin+addition
or 
$ echo code | llm_audit -m "model" -a "addition for question" -p "prefix for question" -r "role" # Request for LLM is intro+stdin+addition

$ llm_audit -l # List all available models

```

# Also you might to use this as module

``` Python
import llm_audit
llm_audit.ask_llm(intro, code, addition, model)
```
