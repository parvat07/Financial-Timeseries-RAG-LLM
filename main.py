"""
 import argparse
from FinSeer.src.2_train_retriever.get_llm_feedback_scores import get_all_scores

parser = argparse.ArgumentParser(description='test')
parser.add_argument('--dataset', default='acl18', type=str)
parser.add_argument('--target', default='acl18.scored.json', type=str)
args = parser.parse_args()
get_all_scores(llm='StockLLM')  # llama family are all supported for this code 
"""

from datasets import load_dataset
dataset = load_dataset("ElsaShaw/finseer_data")