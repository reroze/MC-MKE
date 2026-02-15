import json 

def match(answer, tgts):
    #answer是模型的生成 tgts是output+output_alias 
    for tgt in tgts:
        if tgt.lower().strip() in answer.lower().strip():
            return True
    return False

def load_json(filen):
    file_op = open(filen, 'r')
    data = json.load(file_op)
    file_op.close()
    return data 


#example for single answer with alias and model output match
test_id = ""

model_output = ""

answer = ""


#if cal ie consistency should ignore some data
#the consistency answer of these data don't change.

metric_type = "ie_consistency"

answer2alias_file = "cleaned.ent2mq_wiki_alias.cleaned.json"
answer2alias = load_json(answer2alias_file)

rel_cnt = 0

if metric_type == "ie_consistency":
    ignore_idx_file = 'ie_consistenct_ignore_idx.json'
    ignore_idxs = load_json(ignore_idx_file)  
    
    if test_id not in ignore_idxs:
        ref = answer 
        ref_alias = answer2alias[ref]
        
        all_tgts = [ref] + ref_alias 
        
        if match(model_output, all_tgts):
            rel_cnt += 1


        
