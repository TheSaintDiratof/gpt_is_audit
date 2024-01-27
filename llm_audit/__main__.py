import sys
import g4f

models = { 'gpt_35_long': g4f.models.gpt_35_long, 
           'gpt_35_turbo': g4f.models.gpt_35_turbo,
           'gpt_35_turbo_16k': g4f.models.gpt_35_turbo_16k,
           'gpt_35_turbo_16k_0613': g4f.models.gpt_35_turbo_16k_0613,
           'gpt_35_turbo_0613': g4f.models.gpt_35_turbo_0613,
           'gpt_4': g4f.models.gpt_4,
           'gpt_4_0613': g4f.models.gpt_4_0613,
           'gpt_4_32k': g4f.models.gpt_4_32k,
           'gpt_4_32k_0613': g4f.models.gpt_4_32k_0613,
           'gpt_4_turbo': g4f.models.gpt_4_turbo,
           'llama2_7b': g4f.models.llama2_7b,
           'llama2_13b': g4f.models.llama2_13b,
           'llama2_70b': g4f.models.llama2_70b,
           'llama13b_v2_chat': g4f.models.llama13b_v2_chat,
           'llama7b_v2_chat': g4f.models.llama7b_v2_chat,
           'llama70b_v2_chat': g4f.models.llama70b_v2_chat,
           'llama_13b': g4f.models.llama_13b,
           'mixtral_8x7b': g4f.models.mixtral_8x7b,
           'mistral_7b': g4f.models.mistral_7b,
           'openchat_35': g4f.models.openchat_35,
           'palm': g4f.models.palm,
           'falcon_7b': g4f.models.falcon_7b,
           'falcon_40b': g4f.models.falcon_40b,
           'claude_instant_v1': g4f.models.claude_instant_v1,
           'claude_v1': g4f.models.claude_v1,
           'claude_v2': g4f.models.claude_v2,
           'command_light_nightly': g4f.models.command_light_nightly,
           'command_nightly': g4f.models.command_nightly,
           'gpt_neox_20b': g4f.models.gpt_neox_20b,
           'oasst_sft_1_pythia_12b': g4f.models.oasst_sft_1_pythia_12b,
           'oasst_sft_4_pythia_12b_epoch_35': g4f.models.oasst_sft_4_pythia_12b_epoch_35,
           'santacoder': g4f.models.santacoder,
           'bloom': g4f.models.bloom,
           'flan_t5_xxl': g4f.models.flan_t5_xxl,
           'code_davinci_002': g4f.models.code_davinci_002,
           'text_ada_001': g4f.models.text_ada_001,
           'text_babbage_001': g4f.models.text_babbage_001,
           'text_curie_001': g4f.models.text_curie_001,
           'text_davinci_002': g4f.models.text_davinci_002,
           'text_davinci_003': g4f.models.text_davinci_003,
           'pi': g4f.models.pi
          }

def ask_llm(prefix="There is a piece of code. Show me vulnerabilities in this code. Answer like \"$line_number $what_kind_of_vulnerability $way_to_fix\"", 
            code="", 
            addition="",
            role="user",
            model=g4f.models.gpt_35_long):
    content = prefix  + '\n' + code + '\n' + addition
    response = g4f.ChatCompletion.create(
        model=model,
        messages=[{"role": role, "content": content}],
    )
    return response

def get_model(model):
    return models[model]

def get_models():
    string = str()
    i = 1
    while i < len(list(models.keys())):
        string += list(models.keys())[i-1]
        string += ' '
        if not i % 3:
            string += '\n'
        i += 1
    return string

def main(args=sys.argv):
    prefix = "There is a piece of code. Show me vulnerabilities in this code. Answer like \"$line_number $what_kind_of_vulnerability $way_to_fix\""
    addition = ""
    role = "user"
    code = ""
    model = g4f.models.gpt_35_long
    i = 1
    while i < (len(args) - 1):
        if "-l" or "--list-models" in args:
            print(get_models())
            sys.exit(0)
        if args[i] == "-a" or args[i] == "--addition":
            i += 1
            addition = args[i]
        if args[i] == "-p" or args[i] == "--prefix":
            i += 1
            prefix = args[i]
        if args[i] == "-r" or args[i] == "--role":
            i += 1
            role = args[i]
        if args[i] == "-h" or args[i] == "--help":
            i += 1
            print("will be soon")
            sys.exit(0)
        if args[i] == "-m" or args[i] == "--model":
            i += 1
            try:
                model = get_model(args[i])
            except KeyError:
                sys.stderr.write("No such model\n")
                sys.exit(1)
        i += 1

    for line in sys.stdin:
        code += line

    answer = ask_llm(prefix, code, addition, role, model)
    print(answer)

if __name__ == '__main__':
    main(sys.argv)
