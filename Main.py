import pandas as pd
import openai
import os
from dotenv import load_dotenv,find_dotenv

_ = load_dotenv(find_dotenv())
openai.api_Key = os.environ['api_key']
print(os.environ['api_key'])
print("Hello")