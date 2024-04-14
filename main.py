import PyPDF2
# Define the chapters and their corresponding keywords
chapters = {
    "1.1 x": ["y", "yy","yyy"], # Example "1.1 Compression": ["compression", "RLE", "run-length encoding"],
    "1.2 xx": ["w", "ww", "www"],
    "1.3 xxx": ["z", "zz", "zzz"], 
}

with open("your pdfname.pdf", "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

# Split the text by newline characters ("\n") instead of "\n\n"
lines = text.split("\n")

# Analyze each line and determine if it's a question
chapter_counts = {chapter: 0 for chapter in chapters}
current_chapter = None
for line in lines:
    print(f"Line: {line}")
    # If the line is empty or contains only whitespace, skip it
    if not line.strip():
        continue
    # If the line starts with a word that is not in the current chapter's keywords,
    # assign the line to the next chapter
    if current_chapter is not None and not any(keyword in line.lower() for keyword in chapters[current_chapter]):
        current_chapter = None
    # If the line contains a keyword from any chapter, assign the line to that chapter
    if any(keyword in line.lower() for chapter in chapters for keyword in chapters[chapter]):
        current_chapter = max((chapter for chapter in chapters if any(keyword in line.lower() for keyword in chapters[chapter])), key=len)
        chapter_counts[current_chapter] += 1
        print(f"Assigned to chapter: {current_chapter}")
    # If the line is not assigned to any chapter, print a message
    else:
        print(f"Unassigned line: {line}")

# Print the chapter counts
for chapter, count in chapter_counts.items():
    print(f"{chapter}: {count}")
