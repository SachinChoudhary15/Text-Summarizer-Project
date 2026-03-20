from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from TextSummarizer.entities import ModelEvaluationConfig
from datasets import load_from_disk
import torch
import pandas as pd
import evaluate

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def evaluate(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"

        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path).to(device)

        dataset = load_from_disk(self.config.data_path)

        rouge = evaluate.load("rouge")

        predictions = []
        references = []

        for item in dataset["test"]:
            inputs = tokenizer(
                item["dialogue"],
                return_tensors="pt",
                truncation=True,
                padding=True
            ).to(device)

            output = model.generate(**inputs, max_length=128)

            pred = tokenizer.decode(output[0], skip_special_tokens=True)

            predictions.append(pred)
            references.append(item["summary"])

        scores = rouge.compute(predictions=predictions, references=references)

        df = pd.DataFrame([scores])
        df.to_csv(self.config.metric_file_name, index=False)