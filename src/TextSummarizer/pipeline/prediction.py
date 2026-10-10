from TextSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()

        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        # load tokenizer & model
        self.tokenizer = AutoTokenizer.from_pretrained("Sachin151619/text-summarizer-t5")

        self.model = AutoModelForSeq2SeqLM.from_pretrained("Sachin151619/text-summarizer-t5")
        self.model.to(self.device)

    
    def predict(self, text):
        input_text = "summarize: " + text

        print("Dialogue:")
        print(text)

        inputs = self.tokenizer(
            input_text,
            max_length=512,
            truncation=True,
            return_tensors="pt"
        ).to(self.device)

        summary_ids = self.model.generate(
            inputs["input_ids"],
            max_length=128,
            num_beams=8,
            length_penalty=0.8,
            early_stopping=True
        )

        output = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        print("\nModel Summary:")
        print(output)

        return output