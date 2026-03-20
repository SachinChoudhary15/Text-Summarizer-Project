import os
from TextSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_from_disk
from TextSummarizer.entities import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self, example_batch):

        inputs = ["summarize: " + doc for doc in example_batch["dialogue"]]

        model_inputs = self.tokenizer(
            inputs,
            max_length=512,
            truncation=True,
            padding="max_length"
        )

        labels = self.tokenizer(
            example_batch["summary"],
            max_length=128,
            truncation=True,
            padding="max_length"
        )

        labels_ids = labels["input_ids"]

        labels_ids = [
            [(l if l != self.tokenizer.pad_token_id else -100) for l in label]
            for label in labels_ids
        ]

        model_inputs["labels"] = labels_ids

        return model_inputs

    def convert(self):
        dataset = load_from_disk(self.config.data_path)

        dataset = dataset.map(
            self.convert_examples_to_features,
            batched=True
        )

        dataset.save_to_disk(os.path.join(self.config.root_dir, "samsum_dataset"))

        logger.info("Data Transformation Completed")