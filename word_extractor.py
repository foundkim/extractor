import subprocess
import os
from pathlib import Path
from pdf_extrator import extract_pdf_data

def word_to_pdf(doc_filename: str, output_dir="tmp"):
    """Converts an Doc/Docx file to PDF."""
    subprocess.run(
        [
            "libreoffice",
            "--headless",
            "--convert-to",
            "pdf",
            os.path.join(output_dir, doc_filename),
            "--outdir",
            output_dir,
        ],
        check=True,
    )
    path = Path(doc_filename)
    # Cleanup the temporary docx file
    return os.path.join(output_dir,  path.name.split('.doc')[0] + '.pdf')


def extract_word_data(doc_file):
    """
    Extracts data and images from an Word file (doc or docx).

    Args:
      doc_file: Path to the Word file.
    """
    if not (doc_file.endswith(".doc") or doc_file.endswith(".docx")):
        raise ValueError("path must be an excel file")

    doc = word_to_pdf(doc_file)
    os.remove(doc)
    return extract_pdf_data(doc)