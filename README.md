This program is designed to extract questions from a PDF file and save them in text files (`.txt`) in random order. It is particularly useful for transforming PDF documents containing exam questions into textual format, thus facilitating their reorganization and consultation. The program is written in Python using the PyMuPDF (`fitz`) library for PDF manipulation.

### Features

1. **Text and Image Extraction from PDF:**
   - The program reads the specified PDF file and extracts text and images from each page.
   - It uses page objects to distinguish between text and images.

2. **Splitting Text and Images into Questions:**
   - The extracted text is divided based on the presence of the phrase "Question #question_number".
   - Any images present are associated with their respective questions.

3. **Randomization of Questions:**
   - The extracted questions are shuffled in random order to avoid predictable sequences.

4. **Saving Questions in Text Files:**
   - The shuffled questions are saved in text files (`.txt`).
   - Each file contains a defined number of questions (e.g., 86 questions per file).

### Usage

#### Requirements

- Python 3.x
- PyMuPDF (`fitz`)

---
