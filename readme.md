# PDF Chapter Analyzer
---
- This Python script is designed to analyze the contents of a PDF document and categorize each line of text into predefined chapters based on specified keywords using PyPDF2 library to extract text from the PDF file and then assigning each line to the corresponding chapter based on matching keywords.
---
## Installation
Clone or download the repository to your local machine.
Make sure you have Python installed.
Install the PyPDF2 library using pip:

```python
pip install PyPDF2
```

\[Optional] If you would like to create a chart using matplot for the results 
```python
pip install matplotlib
```

---
## Usage
- Place the PDF file you want to analyze in the same directory as the script.
- Update the chapters dictionary with the chapter titles as keys and corresponding keywords as values.
- Update the `your pdfname.pdf` with the name of your PDF
- Run the script.

## Example
- Suppose you have a PDF file containing a document with chapters and questions. You can define the chapters and their keywords in the chapters dictionary. For example:

```py
chapters = {
    "Chapter 1: Introduction": ["introduction", "overview", "purpose"],
    "Chapter 2: Methodology": ["method", "approach", "procedure"],
    "Chapter 3: Results": ["result", "finding", "outcome"],
    ...
}
```
The script will analyze each line of text in the PDF and assign it to the corresponding chapter based on the keyword matching.

