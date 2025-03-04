import json
import csv
import re
import datetime
import math
import random  # Used for simulating sentiment analysis and keyword extraction
from io import StringIO

class FeedbackInsightExtractor:
    def __init__(self):
        self.required_fields = ["feedback_id", "customer_id", "feedback_text", "rating", "timestamp"]
        self.key_terms = ["excellent", "awesome", "great", "good", "bad", "terrible", "poor", "issue", "problem", "love", "hate"]
    
    def validate_data(self, data, format_type):
        """Validate the input data format and content"""
        records = []
        errors = []
        
        if format_type == "csv":
            try:
                csv_reader = csv.DictReader(StringIO(data))
                records = list(csv_reader)
            except Exception as e:
                return [], [f"ERROR: Invalid CSV format. {str(e)}"]
        elif format_type == "json":
            try:
                json_data = json.loads(data)
                if "feedbacks" not in json_data:
                    return [], ["ERROR: Invalid JSON structure. 'feedbacks' key is missing."]
                records = json_data["feedbacks"]
            except Exception as e:
                return [], [f"ERROR: Invalid JSON format. {str(e)}"]
        else:
            return [], ["ERROR: Invalid data format. Please provide data in CSV or JSON format."]
        
        # Validate each record
        validated_records = []
        for row_num, record in enumerate(records, 1):
            # Check missing fields
            missing_fields = [field for field in self.required_fields if field not in record or not record[field]]
            if missing_fields:
                errors.append(f"ERROR: Missing required field(s): {', '.join(missing_fields)} in row {row_num}.")
                continue
            
            # Validate field types and values
            invalid_fields = []
            
            # Validate feedback_id, customer_id, and feedback_text (non-empty strings)
            for field in ["feedback_id", "customer_id", "feedback_text"]:
                if not isinstance(record[field], str) or not record[field].strip():
                    invalid_fields.append(field)
            
            # Validate rating (number between 1 and 5)
            try:
                rating = float(record["rating"])
                if not (1 <= rating <= 5):
                    invalid_fields.append("rating")
            except (ValueError, TypeError):
                invalid_fields.append("rating")
            
            # Validate timestamp (DD-MM-YYYY)
            timestamp = record["timestamp"]
            if not re.match(r"^\d{2}-\d{2}-\d{4}$", timestamp):
                invalid_fields.append("timestamp")
            else:
                try:
                    day, month, year = map(int, timestamp.split('-'))
                    datetime.datetime(year, month, day)
                except ValueError:
                    invalid_fields.append("timestamp")
            
            if invalid_fields:
                errors.append(f"ERROR: Invalid value for the field(s): {', '.join(invalid_fields)} in row {row_num}. Please correct and resubmit.")
                continue
            
            # If all validations pass, add the record to validated records
            validated_records.append(record)
        
        return validated_records, errors
    
    def generate_validation_report(self, records, errors):
        """Generate a validation report based on the validation results"""
        if not records and not errors:
            return "No data provided for validation."
        
        report = "# Data Validation Report\n"
        
        if errors:
            report += "\n## Validation Errors:\n"
            for error in errors:
                report += f" - {error}\n"
            report += "\n## Validation Summary:\n"
            report += "Data validation failed. Please correct and resubmit the data."
            return report
        
        report += "## Data Structure Check:\n"
        report += f" - Number of feedback records: {len(records)}\n"
        report += f" - Number of fields per record: {len(self.required_fields)}\n\n"
        
        report += "## Required Fields Check:\n"
        for field in self.required_fields:
            report += f" - {field}: present\n"
        report += "\n"
        
        report += "## Data Type and Value Validation:\n"
        report += " - feedback_id (non-empty string): validated\n"
        report += " - customer_id (non-empty string): validated\n"
        report += " - feedback_text (non-empty string): validated\n"
        report += " - rating (number between 1 and 5): validated\n"
        report += " - timestamp (DD-MM-YYYY): validated\n\n"
        
        report += "## Validation Summary:\n"
        report += "Data validation is successful!\n"
        
        return report
    
    def calculate_sentiment_score(self, feedback_text):
        """
        Simulate sentiment analysis by analyzing the text
        In a real implementation, this would use a proper NLP model
        """
        # Split into sentences
        sentences = re.split(r'[.!?]+', feedback_text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        if not sentences:
            return 0.0
        
        # Simplified sentiment analysis based on key words
        sentiment_values = []
        for sentence in sentences:
            # Simple rule-based sentiment scoring
            words = sentence.lower().split()
            sentiment = 0.0
            
            positive_words = ["good", "great", "excellent", "awesome", "love", "like", "happy", "satisfied"]
            negative_words = ["bad", "poor", "terrible", "hate", "dislike", "unhappy", "disappointed", "issue", "problem"]
            
            for word in words:
                if word in positive_words:
                    sentiment += 0.3
                elif word in negative_words:
                    sentiment -= 0.3
            
            # Normalize to range [-1, 1]
            sentiment = max(min(sentiment, 1.0), -1.0)
            sentiment_values.append(sentiment)
        
        # Average sentiment across all sentences
        sentiment_score = sum(sentiment_values) / len(sentences)
        return round(sentiment_score, 2)
    
    def calculate_keyword_frequency(self, feedback_text):
        """Calculate the frequency of key terms in the feedback text"""
        words = re.findall(r'\b\w+\b', feedback_text.lower())
        if not words:
            return 0.0
        
        total_words = len(words)
        key_term_count = sum(1 for word in words if word in self.key_terms)
        
        keyword_frequency = (key_term_count / total_words) * 100
        return round(keyword_frequency, 2)
    
    def extract_key_insights(self, feedback_text):
        """
        Simulate key insight extraction
        In a real implementation, this would use a proper NLP model
        """
        # Simple heuristic to identify potential insights
        sentences = re.split(r'[.!?]+', feedback_text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        insights = []
        for sentence in sentences:
            # Criteria for considering a sentence as an insight
            words = sentence.lower().split()
            if any(term in words for term in self.key_terms) and len(sentence.split()) >= 5:
                insights.append(sentence)
        
        return insights
    
    def calculate_insight_extraction_ratio(self, insights, total_records):
        """Calculate the ratio of extracted insights to total records"""
        if total_records == 0:
            return 0.0
        
        ratio = (len(insights) / total_records) * 100
        return round(ratio, 2)
    
    def generate_recommendation(self, sentiment_score, keyword_frequency, insight_extraction_ratio):
        """Generate recommendation based on calculated metrics"""
        sentiment_status = "Positive" if sentiment_score >= 0.5 else ("Negative" if sentiment_score <= -0.5 else "Neutral")
        keyword_freq_status = "High" if keyword_frequency >= 20 else "Low"
        insight_ratio_status = "Effective" if insight_extraction_ratio >= 50 else "Ineffective"
        
        if sentiment_status == "Positive" and keyword_freq_status == "High" and insight_ratio_status == "Effective":
            status = "Effective"
            action = "Integrate insights into the document management system as is"
        else:
            status = "Needs Refinement"
            action = "Re-evaluate extraction algorithms or adjust analysis parameters"
        
        return {
            "sentiment_score": sentiment_score,
            "keyword_frequency": keyword_frequency,
            "insight_extraction_ratio": insight_extraction_ratio,
            "status": status,
            "action": action
        }
    
    def generate_final_report(self, records):
        """Generate the final analysis report"""
        report = "# Customer Feedback Analysis Summary:\n"
        report += f"Total Feedback Records Evaluated: {len(records)}\n\n"
        
        # For each feedback record
        for record in records:
            report += f"# Detailed Analysis per Feedback Record:\n"
            report += f"Feedback {record['feedback_id']}\n"
            report += "Input Data:\n"
            report += f" - Customer ID: {record['customer_id']}\n"
            report += f" - Feedback Text: {record['feedback_text']}\n"
            report += f" - Rating: {record['rating']}\n"
            report += f" - Timestamp: {record['timestamp']}\n\n"
            
            report += "# Detailed Calculations:\n"
            
            # Sentiment score calculation
            sentiment_score = self.calculate_sentiment_score(record['feedback_text'])
            report += "## 1. Sentiment Score Calculation:\n"
            report += " - Formula: $$ \\text{Sentiment Score} = \\frac{\\text{sum of sentiment values for each sentence}}{\\text{number of sentences}} $$\n"
            report += " - Calculation Steps:\n"
            report += "   Step 1: Divide feedback_text into sentences.\n"
            
            sentences = re.split(r'[.!?]+', record['feedback_text'])
            sentences = [s.strip() for s in sentences if s.strip()]
            report += f"   Number of sentences: {len(sentences)}\n"
            
            report += "   Step 2: Compute sentiment value for each sentence.\n"
            # Simulate sentiment values for each sentence
            sentiment_values = []
            for i, sentence in enumerate(sentences, 1):
                # Simulate a sentiment value
                value = round(self.calculate_sentiment_score(sentence), 2)
                sentiment_values.append(value)
                report += f"   Sentence {i} sentiment: {value}\n"
            
            report += "   Step 3: Sum the sentiment values.\n"
            sum_sentiment = sum(sentiment_values)
            report += f"   Sum of sentiment values: {round(sum_sentiment, 2)}\n"
            
            report += "   Step 4: Divide the sum by the number of sentences.\n"
            if len(sentences) > 0:
                final_sentiment = round(sum_sentiment / len(sentences), 2)
            else:
                final_sentiment = 0.0
            report += f" - Final Sentiment Score: {final_sentiment}\n\n"
            
            # Keyword frequency analysis
            keyword_frequency = self.calculate_keyword_frequency(record['feedback_text'])
            report += "## 2. Keyword Frequency Analysis:\n"
            report += " - Formula: $$ \\text{Keyword Frequency} = \\frac{\\text{Number of occurrences of key terms}}{\\text{Total number of words in feedback_text}} \\times 100 $$\n"
            report += " - Calculation Steps:\n"
            report += "   Step 1: Tokenize feedback_text into words.\n"
            
            words = re.findall(r'\b\w+\b', record['feedback_text'].lower())
            report += f"   Total words: {len(words)}\n"
            
            report += "   Step 2: Count total words.\n"
            report += f"   Total word count: {len(words)}\n"
            
            report += "   Step 3: Count occurrences of key terms.\n"
            key_term_counts = {}
            for term in self.key_terms:
                count = sum(1 for word in words if word == term)
                if count > 0:
                    key_term_counts[term] = count
            
            total_key_terms = sum(key_term_counts.values())
            report += f"   Key terms found: {', '.join([f'{term} ({count})' for term, count in key_term_counts.items()])}\n"
            report += f"   Total key term occurrences: {total_key_terms}\n"
            
            report += "   Step 4: Divide the occurrences by total words and multiply by 100.\n"
            if len(words) > 0:
                freq = (total_key_terms / len(words)) * 100
            else:
                freq = 0.0
            report += f" - Final Keyword Frequency: {round(freq, 2)}%\n\n"
            
            # Insight extraction ratio calculation
            insights = self.extract_key_insights(record['feedback_text'])
            insight_ratio = self.calculate_insight_extraction_ratio(insights, 1)  # 1 record at a time
            
            report += "## 3. Insight Extraction Ratio Calculation:\n"
            report += " - Formula: $$ \\text{Insight Extraction Ratio} = \\frac{\\text{Number of key insights extracted}}{\\text{Total number of feedback records}} \\times 100 $$\n"
            report += " - Calculation Steps:\n"
            report += "   Step 1: Count total feedback records.\n"
            report += "   Total feedback records: 1\n"
            
            report += "   Step 2: Count key insights extracted.\n"
            report += f"   Key insights extracted: {len(insights)}\n"
            if insights:
                report += "   Insights:\n"
                for i, insight in enumerate(insights, 1):
                    report += f"   - Insight {i}: \"{insight}\"\n"
            
            report += "   Step 3: Divide key insights count by total records and multiply by 100.\n"
            report += f" - Final Insight Extraction Ratio: {round(insight_ratio, 2)}%\n\n"
            
            # Final recommendation
            recommendation = self.generate_recommendation(final_sentiment, freq, insight_ratio)
            
            report += "# Final Recommendation:\n"
            report += f" - Sentiment Score: {recommendation['sentiment_score']}\n"
            report += f" - Keyword Frequency: {recommendation['keyword_frequency']}%\n"
            report += f" - Insight Extraction Ratio: {recommendation['insight_extraction_ratio']}%\n"
            report += f" - Status: {recommendation['status']}\n"
            report += f" - Recommended Action: {recommendation['action']}\n\n"
        
        return report

    def process_feedback_data(self, data, format_type):
        """Main method to process feedback data"""
        # Validate data
        records, errors = self.validate_data(data, format_type)
        validation_report = self.generate_validation_report(records, errors)
        
        # If validation fails, return only the validation report
        if errors:
            return validation_report, None
        
        # Generate final report
        final_report = self.generate_final_report(records)
        
        return validation_report, final_report

def main():
    """
    Main function to demonstrate the FeedbackInsightExtractor
    """
    extractor = FeedbackInsightExtractor()
    
#     # Example input data in CSV format
#     csv_data = """feedback_id,customer_id,feedback_text,rating,timestamp
# FB101,C101,"Amazing product and fast delivery!",5,01-04-2025
# FB102,C102,"Not satisfied with the packaging.",3,02-04-2025
# FB103,C103,"The quality is excellent but the price is high.",4,03-04-2025
# FB104,C104,"Customer service was terrible and rude.",1,04-04-2025
# FB105,C105,"I love the new features of the app.",4,05-04-2025
# FB106,C106,"The update caused several issues and delays.",2,06-04-2025  """

    # Example input data in JSON format
    json_data = """{
    "feedbacks": [
    {
      "feedback_id": "FB601",
      "customer_id": "C601",
      "feedback_text": "I love the app, it is excellent and very reliable.",
      "rating": 5,
      "timestamp": "01-06-2025"
    },
    {
      "feedback_id": "FB602",
      "customer_id": "C602",
      "feedback_text": "The service was great and the response time was good.",
      "rating": 5,
      "timestamp": "02-06-2025"
    },
    {
      "feedback_id": "FB603",
      "customer_id": "C603",
      "feedback_text": "I am disappointed with the performance; the app is terrible.",
      "rating": 2,
      "timestamp": "03-06-2025"
    },
    {
      "feedback_id": "FB604",
      "customer_id": "C604",
      "feedback_text": "Absolutely awesome experience, the product is really good!",
      "rating": 5,
      "timestamp": "04-06-2025"
    },
    {
      "feedback_id": "FB605",
      "customer_id": "C605",
      "feedback_text": "I hate the new update; it has a major problem.",
      "rating": 1,
      "timestamp": "05-06-2025"
    },
    {
      "feedback_id": "FB606",
      "customer_id": "C606",
      "feedback_text": "The quality is excellent, and I am very happy with it.",
      "rating": 5,
      "timestamp": "06-06-2025"
    },
    {
      "feedback_id": "FB607",
      "customer_id": "C607",
      "feedback_text": "I am satisfied with the overall experience, it is good.",
      "rating": 4,
      "timestamp": "07-06-2025"
    }
  ]
}

"""

    # # Process CSV data
    # print("Processing CSV data:")
    # validation_report_csv, final_report_csv = extractor.process_feedback_data(csv_data, "csv")
    # print(validation_report_csv)
    # if final_report_csv:
    #     print("\n" + final_report_csv)
    
    # print("\n" + "-" * 80 + "\n")
    
    # Process JSON data
    print("Processing JSON data:")
    validation_report_json, final_report_json = extractor.process_feedback_data(json_data, "json")
    print(validation_report_json)
    if final_report_json:
        print("\n" + final_report_json)

if __name__ == "__main__":
    main()