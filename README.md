# FeedbackInsightExtractor-AI Case Study

## Overview

**FeedbackInsightExtractor-AI** is an intelligent system designed to analyze large volumes of customer feedback data and extract key insights to support strategic decision-making. By automatically validating input data, performing sentiment analysis, and calculating keyword frequencies and insight extraction ratios, the system helps organizations understand customer sentiments and identify areas for improvement—all in a clear, step-by-step manner that even non-technical users can appreciate.

This system accepts data in CSV or JSON formats (provided within markdown code blocks) and enforces strict validation rules before performing the analysis. The step-by-step calculations and detailed recommendations enable organizations to integrate these insights into a centralized document management system with confidence.

## Features

- **Data Validation:**  
  The system checks the input for:
  - **Format:** Only CSV or JSON data provided within markdown code blocks is accepted.
  - **Language:** Only English is supported.
  - **Required Fields:** Each feedback record must include `feedback_id`, `customer_id`, `feedback_text`, `rating`, and `timestamp`.
  - **Data Types and Values:** The system validates that `feedback_id`, `customer_id`, and `feedback_text` are non-empty strings, `rating` is a numeric value between 1 and 5, and `timestamp` follows the `DD-MM-YYYY` format.

- **Key Insights Extraction:**  
  The system performs three main calculations on the customer feedback:
  - **Sentiment Score Calculation:**  
    Computes a sentiment score for each feedback by averaging sentiment values assigned to each sentence. Only predefined keywords (e.g., "good", "excellent", "love" for positive and "bad", "terrible", "problem" for negative) are used.
  - **Keyword Frequency Analysis:**  
    Calculates the percentage frequency of key terms (that signal customer satisfaction or issues) within the feedback text.
  - **Insight Extraction Ratio Calculation:**  
    Determines the effectiveness of the extraction process by comparing the number of key insights identified to the total number of feedback records.

- **Step-by-Step Explanations:**  
  Every calculation is documented with explicit formulas and step-by-step breakdowns using LaTeX formulas, ensuring clarity and transparency in the results.

- **Feedback and Iterative Improvement:**  
  After each analysis, the system prompts the user for feedback, enabling iterative improvements based on user remarks and new data submissions.

## System Prompt

The behavior of **FeedbackInsightExtractor-AI** is governed by the following system prompt:

```markdown
**[system]**
You are FeedbackInsightExtractor-AI, a system designed to extract key insights from large volumes of customer feedback data by leveraging machine learning algorithms to interpret unstructured text. Your objective is to integrate these insights into a centralized document management system to support strategic decision-making. Follow the instructions below with explicit IF/THEN/ELSE logic, detailed step-by-step calculations (with formulas and examples), and clear validations. Do not assume any pretrained constraints; define all logic explicitly.

LANGUAGE & FORMAT LIMITATIONS  
Only process input in ENGLISH. If any other language is detected, THEN respond with: "ERROR: Unsupported language detected. Please use ENGLISH." Accept data only in plain text provided within markdown code blocks labeled as CSV or JSON. If data is provided in any other format, THEN respond with: "ERROR: Invalid data format. Please provide data in CSV or JSON format."

GREETING PROTOCOL  
If the user greets, THEN respond with: "Greetings! I am FeedbackInsightExtractor-AI, your assistant for extracting key insights from customer feedback data." If the user asks for a data template or greets without data, THEN ask: "Would you like a template for the data input?" If the user agrees, THEN provide the template.

DATA INPUT PROTOCOL  
Expected fields per feedback record: "feedback_id", "customer_id", "feedback_text", "rating", "timestamp". Validate all records before proceeding. 

CALCULATION STEPS  
For each feedback record, calculate:
1. **Sentiment Score**: Average sentiment value per sentence based on predefined keywords.
2. **Keyword Frequency**: Percentage of occurrences of key terms over total words.
3. **Insight Extraction Ratio**: Percentage of key insights relative to total feedback records.

FINAL RECOMMENDATION  
Based on the calculated metrics, provide a recommendation as per the defined criteria.

Follow this mind map flowchart strictly to generate responses and include detailed explanations with explicit formulas and examples.
```

## Metadata

- **Project Name:** FeedbackInsightExtractor-AI  
- **Version:** 1.0.0  
- **Author:** Usman Ashfaq  
- **Keywords:** Customer Feedback, Sentiment Analysis, Keyword Frequency, Insight Extraction, Data Validation, Strategic Decision-Making

## Variations and Test Flows

### Flow 1: Greeting with Invalid Format Data Submission
- **User Action:** Greets and provides data in an invalid XML format.
- **Assistant Response:** Greets back and immediately identifies the invalid data format, prompting the user to resubmit data in CSV or JSON format.
- **Result:** Error message "ERROR: Invalid data format. Please provide data in CSV or JSON format." is returned.

### Flow 2: Request for Template After Error
- **User Action:** Requests the template after receiving the error.
- **Assistant Response:** Provides both CSV and JSON template examples for data input.
- **Result:** The user is guided on the correct format for data submission.

### Flow 3: Correct Data Submission with Initial Errors
- **User Action:** Submits JSON data containing 7 feedback records.
- **Assistant Response:** Provides a detailed Data Validation Report that checks for required fields, correct data types, and valid values.
- **Result:** Data is validated successfully, and the user is asked whether to proceed with key insights extraction.

### Flow 4: Key Insights Extraction
- **User Action:** Agrees to proceed with key insights extraction.
- **Assistant Response:** Processes the validated JSON data, performing sentiment analysis, keyword frequency analysis, and insight extraction ratio calculations. A detailed report is provided, including explicit formulas, calculation steps, and final recommendations for each feedback record.
- **Result:** The final report shows non-zero results for sentiment scores, keyword frequencies, and insight extraction ratios across all feedback records, ensuring that the system is effectively extracting actionable insights.
- Flow 4 Final report:
  # Customer Feedback Analysis Summary:
Total Feedback Records Evaluated: 7

# Detailed Analysis per Feedback Record:

### Feedback FB601
**Input Data:**
 - Customer ID: C601  
 - Feedback Text: I love the app, it is excellent and very reliable.  
 - Rating: 5  
 - Timestamp: 01-06-2025  

**Detailed Calculations:**

#### 1. Sentiment Score Calculation:
- **Formula:**  
  $$ \text{Sentiment Score} = \frac{\text{Sum of Sentiment Values}}{\text{Number of Sentences}} $$
- **Step-by-step Calculation:**
  1. **Sentence Splitting:**  
     - Sentence: "I love the app, it is excellent and very reliable."  
     - Total Sentences = 1
  2. **Compute Sentiment Values:**  
     - "love" → +0.3  
     - "excellent" → +0.3  
     - **Sum of Sentiment Values:** $$ 0.3 + 0.3 = 0.6 $$
  3. **Average Calculation:**  
     $$ \text{Sentiment Score} = \frac{0.6}{1} = 0.60 $$
- **Final Sentiment Score:** 0.60

#### 2. Keyword Frequency Analysis:
- **Formula:**  
  $$ \text{Keyword Frequency} = \frac{\text{Occurrences of Key Terms}}{\text{Total Number of Words}} \times 100 $$
- **Step-by-step Calculation:**
  1. **Tokenization:**  
     - Tokens: ["I", "love", "the", "app,", "it", "is", "excellent", "and", "very", "reliable."]  
     - Total Words = 10
  2. **Count Occurrences of Key Terms:**  
     - Occurrences: "love" (1) and "excellent" (1)  
     - Total Occurrences = 2
  3. **Frequency Calculation:**  
     $$ \text{Keyword Frequency} = \frac{2}{10} \times 100 = 20.00\% $$
- **Final Keyword Frequency:** 20.00%

#### 3. Insight Extraction Ratio Calculation:
- **Formula:**  
  $$ \text{Insight Extraction Ratio} = \frac{\text{Key Insights Count}}{\text{Total Feedback Records}} \times 100 $$
- **Step-by-step Calculation:**
  1. **Identify Key Insights:**  
     - The sentence qualifies as a key insight since it contains key terms ("love" and "excellent") and has more than 5 words.  
     - Key Insights Count = 1
  2. **Ratio Calculation:**  
     $$ \text{Insight Extraction Ratio} = \frac{1}{7} \times 100 \approx 14.29\% $$
- **Final Insight Extraction Ratio:** 14.29%

#### Final Recommendation for FB601:
Based on a Sentiment Score of **0.60**, a Keyword Frequency of **20.00%**, and an Insight Extraction Ratio of **14.29%**, the key insights extraction requires further refinement. Consider re-evaluating the extraction algorithms or adjusting the analysis parameters.

---

### Feedback FB602
**Input Data:**
 - Customer ID: C602  
 - Feedback Text: The service was great and the response time was good.  
 - Rating: 5  
 - Timestamp: 02-06-2025  

**Detailed Calculations:**

#### 1. Sentiment Score Calculation:
- **Step-by-step Calculation:**
  1. **Sentence Splitting:**  
     - Sentence: "The service was great and the response time was good."  
     - Total Sentences = 1
  2. **Compute Sentiment Values:**  
     - "great" → +0.3  
     - "good" → +0.3  
     - **Sum:** $$ 0.3 + 0.3 = 0.6 $$
  3. **Average Calculation:**  
     $$ \frac{0.6}{1} = 0.60 $$
- **Final Sentiment Score:** 0.60

#### 2. Keyword Frequency Analysis:
- **Step-by-step Calculation:**
  1. **Tokenization:**  
     - Tokens: ["The", "service", "was", "great", "and", "the", "response", "time", "was", "good."]  
     - Total Words = 10
  2. **Key Terms Count:**  
     - "great" (1) and "good" (1) → Total = 2
  3. **Frequency Calculation:**  
     $$ \frac{2}{10} \times 100 = 20.00\% $$
- **Final Keyword Frequency:** 20.00%

#### 3. Insight Extraction Ratio Calculation:
- **Step-by-step Calculation:**
  1. **Key Insights Count:**  
     - Qualifies as a key insight (contains key terms) → Count = 1
  2. **Ratio Calculation:**  
     $$ \frac{1}{7} \times 100 \approx 14.29\% $$
- **Final Insight Extraction Ratio:** 14.29%

#### Final Recommendation for FB602:
Based on a Sentiment Score of **0.60**, a Keyword Frequency of **20.00%**, and an Insight Extraction Ratio of **14.29%**, the key insights extraction requires further refinement. Consider re-evaluating the extraction algorithms or adjusting the analysis parameters.

---

### Feedback FB603
**Input Data:**
 - Customer ID: C603  
 - Feedback Text: I am disappointed with the performance; the app is terrible.  
 - Rating: 2  
 - Timestamp: 03-06-2025  

**Detailed Calculations:**

#### 1. Sentiment Score Calculation:
- **Step-by-step Calculation:**
  1. **Sentence Splitting:**  
     - Sentence: "I am disappointed with the performance; the app is terrible."  
     - Total Sentences = 1
  2. **Compute Sentiment Values:**  
     - "disappointed" → -0.3  
     - "terrible" → -0.3  
     - **Sum:** $$ -0.3 - 0.3 = -0.6 $$
  3. **Average Calculation:**  
     $$ \frac{-0.6}{1} = -0.60 $$
- **Final Sentiment Score:** -0.60

#### 2. Keyword Frequency Analysis:
- **Step-by-step Calculation:**
  1. **Tokenization:**  
     - Tokens: ["I", "am", "disappointed", "with", "the", "performance;", "the", "app", "is", "terrible."]  
     - Total Words = 10
  2. **Key Terms Count:**  
     - "disappointed" (1) and "terrible" (1) → Total = 2
  3. **Frequency Calculation:**  
     $$ \frac{2}{10} \times 100 = 20.00\% $$
- **Final Keyword Frequency:** 20.00%

#### 3. Insight Extraction Ratio Calculation:
- **Step-by-step Calculation:**
  1. **Key Insights Count:**  
     - Qualifies as a key insight → Count = 1
  2. **Ratio Calculation:**  
     $$ \frac{1}{7} \times 100 \approx 14.29\% $$
- **Final Insight Extraction Ratio:** 14.29%

#### Final Recommendation for FB603:
Based on a Sentiment Score of **-0.60**, a Keyword Frequency of **20.00%**, and an Insight Extraction Ratio of **14.29%**, the key insights extraction requires further refinement. Consider re-evaluating the extraction algorithms or adjusting the analysis parameters.

---

### Feedback FB604
**Input Data:**
 - Customer ID: C604  
 - Feedback Text: Absolutely awesome experience, the product is really good!  
 - Rating: 5  
 - Timestamp: 04-06-2025  

**Detailed Calculations:**

#### 1. Sentiment Score Calculation:
- **Step-by-step Calculation:**
  1. **Sentence Splitting:**  
     - Sentence: "Absolutely awesome experience, the product is really good!"  
     - Total Sentences = 1
  2. **Compute Sentiment Values:**  
     - "awesome" → +0.3  
     - "good" → +0.3  
     - **Sum:** $$ 0.3 + 0.3 = 0.6 $$
  3. **Average Calculation:**  
     $$ \frac{0.6}{1} = 0.60 $$
- **Final Sentiment Score:** 0.60

#### 2. Keyword Frequency Analysis:
- **Step-by-step Calculation:**
  1. **Tokenization:**  
     - Tokens: ["Absolutely", "awesome", "experience,", "the", "product", "is", "really", "good!"]  
     - Total Words = 8
  2. **Key Terms Count:**  
     - "awesome" (1) and "good" (1) → Total = 2
  3. **Frequency Calculation:**  
     $$ \frac{2}{8} \times 100 = 25.00\% $$
- **Final Keyword Frequency:** 25.00%

#### 3. Insight Extraction Ratio Calculation:
- **Step-by-step Calculation:**
  1. **Key Insights Count:**  
     - Qualifies as a key insight → Count = 1
  2. **Ratio Calculation:**  
     $$ \frac{1}{7} \times 100 \approx 14.29\% $$
- **Final Insight Extraction Ratio:** 14.29%

#### Final Recommendation for FB604:
Based on a Sentiment Score of **0.60**, a Keyword Frequency of **25.00%**, and an Insight Extraction Ratio of **14.29%**, the key insights extraction requires further refinement. Consider re-evaluating the extraction algorithms or adjusting the analysis parameters.

---

### Feedback FB605
**Input Data:**
 - Customer ID: C605  
 - Feedback Text: I hate the new update; it has a major problem.  
 - Rating: 1  
 - Timestamp: 05-06-2025  

**Detailed Calculations:**

#### 1. Sentiment Score Calculation:
- **Step-by-step Calculation:**
  1. **Sentence Splitting:**  
     - Sentence: "I hate the new update; it has a major problem."  
     - Total Sentences = 1
  2. **Compute Sentiment Values:**  
     - "hate" → -0.3  
     - "problem" → -0.3  
     - **Sum:** $$ -0.3 - 0.3 = -0.6 $$
  3. **Average Calculation:**  
     $$ \frac{-0.6}{1} = -0.60 $$
- **Final Sentiment Score:** -0.60

#### 2. Keyword Frequency Analysis:
- **Step-by-step Calculation:**
  1. **Tokenization:**  
     - Tokens: ["I", "hate", "the", "new", "update;", "it", "has", "a", "major", "problem."]  
     - Total Words = 10
  2. **Key Terms Count:**  
     - "hate" (1) and "problem" (1) → Total = 2
  3. **Frequency Calculation:**  
     $$ \frac{2}{10} \times 100 = 20.00\% $$
- **Final Keyword Frequency:** 20.00%

#### 3. Insight Extraction Ratio Calculation:
- **Step-by-step Calculation:**
  1. **Key Insights Count:**  
     - Qualifies as a key insight → Count = 1
  2. **Ratio Calculation:**  
     $$ \frac{1}{7} \times 100 \approx 14.29\% $$
- **Final Insight Extraction Ratio:** 14.29%

#### Final Recommendation for FB605:
Based on a Sentiment Score of **-0.60**, a Keyword Frequency of **20.00%**, and an Insight Extraction Ratio of **14.29%**, the key insights extraction requires further refinement. Consider re-evaluating the extraction algorithms or adjusting the analysis parameters.

---

### Feedback FB606
**Input Data:**
 - Customer ID: C606  
 - Feedback Text: The quality is excellent, and I am very happy with it.  
 - Rating: 5  
 - Timestamp: 06-06-2025  

**Detailed Calculations:**

#### 1. Sentiment Score Calculation:
- **Step-by-step Calculation:**
  1. **Sentence Splitting:**  
     - Sentence: "The quality is excellent, and I am very happy with it."  
     - Total Sentences = 1
  2. **Compute Sentiment Values:**  
     - "excellent" → +0.3  
     - "happy" → +0.3  
     - **Sum:** $$ 0.3 + 0.3 = 0.6 $$
  3. **Average Calculation:**  
     $$ \frac{0.6}{1} = 0.60 $$
- **Final Sentiment Score:** 0.60

#### 2. Keyword Frequency Analysis:
- **Step-by-step Calculation:**
  1. **Tokenization:**  
     - Tokens: ["The", "quality", "is", "excellent,", "and", "I", "am", "very", "happy", "with", "it."]  
     - Total Words = 11
  2. **Key Terms Count:**  
     - "excellent" (1) and "happy" (1) → Total = 2
  3. **Frequency Calculation:**  
     $$ \frac{2}{11} \times 100 \approx 18.18\% $$
- **Final Keyword Frequency:** 18.18%

#### 3. Insight Extraction Ratio Calculation:
- **Step-by-step Calculation:**
  1. **Key Insights Count:**  
     - Qualifies as a key insight → Count = 1
  2. **Ratio Calculation:**  
     $$ \frac{1}{7} \times 100 \approx 14.29\% $$
- **Final Insight Extraction Ratio:** 14.29%

#### Final Recommendation for FB606:
Based on a Sentiment Score of **0.60**, a Keyword Frequency of **18.18%**, and an Insight Extraction Ratio of **14.29%**, the key insights extraction requires further refinement. Consider re-evaluating the extraction algorithms or adjusting the analysis parameters.

---

### Feedback FB607
**Input Data:**
 - Customer ID: C607  
 - Feedback Text: I am satisfied with the overall experience, it is good.  
 - Rating: 4  
 - Timestamp: 07-06-2025  

**Detailed Calculations:**

#### 1. Sentiment Score Calculation:
- **Step-by-step Calculation:**
  1. **Sentence Splitting:**  
     - Sentence: "I am satisfied with the overall experience, it is good."  
     - Total Sentences = 1
  2. **Compute Sentiment Values:**  
     - "satisfied" → +0.3  
     - "good" → +0.3  
     - **Sum:** $$ 0.3 + 0.3 = 0.6 $$
  3. **Average Calculation:**  
     $$ \frac{0.6}{1} = 0.60 $$
- **Final Sentiment Score:** 0.60

#### 2. Keyword Frequency Analysis:
- **Step-by-step Calculation:**
  1. **Tokenization:**  
     - Tokens: ["I", "am", "satisfied", "with", "the", "overall", "experience,", "it", "is", "good."]  
     - Total Words = 10
  2. **Key Terms Count:**  
     - "satisfied" (1) and "good" (1) → Total = 2
  3. **Frequency Calculation:**  
     $$ \frac{2}{10} \times 100 = 20.00\% $$
- **Final Keyword Frequency:** 20.00%

#### 3. Insight Extraction Ratio Calculation:
- **Step-by-step Calculation:**
  1. **Key Insights Count:**  
     - Qualifies as a key insight → Count = 1
  2. **Ratio Calculation:**  
     $$ \frac{1}{7} \times 100 \approx 14.29\% $$
- **Final Insight Extraction Ratio:** 14.29%

#### Final Recommendation for FB607:
Based on a Sentiment Score of **0.60**, a Keyword Frequency of **20.00%**, and an Insight Extraction Ratio of **14.29%**, the key insights extraction requires further refinement. Consider re-evaluating the extraction algorithms or adjusting the analysis parameters.


## Conclusion

FeedbackInsightExtractor-AI is a robust, user-friendly tool that automates the analysis of customer feedback. By enforcing strict data validation and providing clear, step-by-step explanations of the underlying calculations, the system ensures both accuracy and transparency in its outputs. The iterative test flows demonstrate the system's ability to handle various input scenarios—including format errors and data corrections—while continuously refining its analysis. This project exemplifies how automation can simplify complex data processing tasks, enabling organizations to derive meaningful insights from customer feedback and support strategic decision-making.

---
