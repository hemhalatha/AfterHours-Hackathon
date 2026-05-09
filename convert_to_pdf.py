
import re
from fpdf import FPDF

def strip_emojis(text):
    return text.encode('ascii', 'ignore').decode('ascii')

def markdown_to_pdf(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        md_text = f.read()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("helvetica", size=11)
    
    # Process the text more simply
    safe_text = strip_emojis(md_text)
    
    for line in safe_text.split('\n'):
        if line.startswith('# '):
            pdf.ln(5)
            pdf.set_font("helvetica", 'B', 16)
            pdf.write(10, line[2:] + '\n')
            pdf.set_font("helvetica", size=11)
        elif line.startswith('## '):
            pdf.ln(3)
            pdf.set_font("helvetica", 'B', 14)
            pdf.write(9, line[3:] + '\n')
            pdf.set_font("helvetica", size=11)
        elif line.startswith('### '):
            pdf.ln(2)
            pdf.set_font("helvetica", 'B', 12)
            pdf.write(8, line[4:] + '\n')
            pdf.set_font("helvetica", size=11)
        elif line.startswith('---'):
            pdf.ln(2)
            pdf.line(10, pdf.get_y(), 200, pdf.get_y())
            pdf.ln(2)
        else:
            if line.strip().startswith('- ') or line.strip().startswith('* '):
                pdf.write(6, "  " + line.strip() + '\n')
            else:
                pdf.write(6, line + '\n')
            
    pdf.output(output_file)

if __name__ == "__main__":
    markdown_to_pdf('hackathon_submission.md', 'hackathon_submission.pdf')
    print("PDF created successfully: hackathon_submission.pdf")
