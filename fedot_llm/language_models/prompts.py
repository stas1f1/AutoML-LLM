dataset_name_prompt = '''Your task is to define the name of this dataset. Answer only with the name.'''

dataset_description_prompt = '''Your task is to formulate a short description this dataset.
It should be no longer than a paragraph'''

train_split_definition_prompt = '''Your task is to define the train split of this dataset. Answer only with the name of the file with train split. Mind the register.'''

target_split_definition_prompt = '''Your task is to define the target split of this dataset. Answer only with the name of the file with target split. Mind the register.'''

dataset_goal_prompt = '''Your task is to formulate the task associated with this dataset. Answer only with the task description, mention the target column.
It should be short, 1-2 sentences long.'''

split_description_prompt = '''Your task is to describe the purpose of this dataset split.
It should be short, 1-2 sentences long'''

categorical_definition_prompt = '''Your task is to return the list of all option feature columns
                            Only answer with a column name on separate lines'''

categorical_definition_context = '''An option feature column in a dataset:
                            - Can have numeric or string values
                            - Represents state or option, not highly varying quantitative or unique data
                            - Has a low unique value ratio
                            - Not necessaily ordered'''

target_definition_prompt = '''Your task is to return the target column of the dataset
                            Only answer with a column name'''

task_definition_prompt = '''Your task is to define whether the task is regression or classification
                            Only answer with a task type'''
                            
describe_column_sys = """You are helpful AI assistant.
User will enter one column from dataset, and the assistant will make one sentence discription of data in this column.
Don't make assumptions about what values to plug into functions. Use column hint.
Output format: only JSON using the schema defined here: {schema}
"""

describe_column_user="""Dataset Title: {title}
Dataset description: {ds_descr}
Column name: {col_name}
Column hint: {hint}
Column values: 
```
{values}
```"""

categorical_sys_template = """Be specific and respond in the tone of a McKinsey consultant.
User will enter one column from dataset, and the assistant will define whether the column consists of categorical variables or not.
You MUST follow the instructions for your given task exactly. Use column description.
Categorical variable represents string variable where the values in the column have a finite set of values (usually way smaller than the length of the column), assigning each individual or other unit of observation to a particular group or nominal category on the basis of some qualitative property.
Output format: {{Insert reasoning steps plain text list here}}.\n{{JSON using the schema defined here: {schema}}}
Options: yes or not"""

categorical_user_template = """Dataset Title: {title}

Dataset description: {ds_desc}

Column name: {col_name}

Column description: {col_desc}

Column unique ratio: {col_ratio} (number of unique values divided by the number of total values)

Column data: 
```
{data}
```
Let’s think step by step. 
"""
