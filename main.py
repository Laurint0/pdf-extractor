import fitz  # PyMuPDF
import re
import os
import random

def extract_text_and_images_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    data = []
    for page in doc:
        page_data = {"text": "", "images": []}
        for obj in page.get_page_objects():
            if obj[0] == 1:  # Text
                page_data["text"] += obj[4]
            elif obj[0] == 3:  # Image
                img = obj[7]
                page_data["images"].append(img)
        data.append(page_data)
    return data

def split_text_and_images_into_questions(data):
    questions = []
    for page_data in data:
        text = page_data["text"]
        images = page_data["images"]
        # Utilizziamo la regex per trovare la frase "Question #numero_della_domanda" come separatore tra le domande
        page_questions = re.split(r'Question #\d+', text)
        # Rimuoviamo eventuali stringhe vuote risultanti dalla divisione
        page_questions = [q.strip() for q in page_questions if q.strip()]
        questions.extend([(q, images) for q in page_questions])
    return questions

def save_questions_to_file(exam_num, questions):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_dir, f"Exam_{exam_num}.txt"), "w", encoding="utf-8") as file:
        for question, images in questions:
            file.write(question + "\n")
            for img in images:
                file.write(f"Image: {img}\n")
            file.write("\n\n")

# Percorso del file PDF
pdf_path = "C:/Users/lauri/OneDrive/Desktop/SecurityPLUS/CompTIA-Examtrain.pdf"

# Estrazione del testo e delle immagini dal PDF
data = extract_text_and_images_from_pdf(pdf_path)

# Divisione del testo e delle immagini in domande basate sulla frase "Question #numero_della_domanda"
questions = split_text_and_images_into_questions(data)

# Mescolare le domande in ordine casuale
random.shuffle(questions)

# Verifica del numero di domande estratte
print(f"Number of questions extracted: {len(questions)}")

# Assicurarsi che ci siano 754 domande
if len(questions) != 754:
    print("Warning: The number of questions extracted does not match the expected count (754).")

# Suddivisione delle domande in base alla logica proposta
questions_per_file = 86
num_files = len(questions) // questions_per_file + 1

for i in range(num_files):
    start_idx = i * questions_per_file
    end_idx = min((i + 1) * questions_per_file, len(questions))
    exam_questions = questions[start_idx:end_idx]
    save_questions_to_file(i + 1, exam_questions)

print("Questions have been successfully saved to files.")
