# Local PDF Parsing Dependencies (Windows)

Parsing PDFs locally through langchain `UnstructuredLoader` requires the installation of additional dependencies.

---

## 1. Poppler

Poppler is used for PDF processing, including extracting text and images.

### Installation Steps:

1. Download the latest version from the official Windows port:  
   https://github.com/oschwartz10612/poppler-windows

2. Extract the ZIP file to a folder, e.g.,  
   `C:\Poppler PDF to Text Local Parser\poppler-24.08.0\`

3. Locate the `bin` folder inside the extracted directory.  
   For example:  
   `C:\Poppler PDF to Text Local Parser\poppler-24.08.0\Library\bin`

4. Open **Start Menu** → search for **"Edit the system environment variables"** → open it.

5. In the **System Properties** window, click **Environment Variables**.

6. Under **System Variables**, find and select the `Path` variable → click **Edit**.

7. Click **New** and paste the path to the `bin` folder.

8. Click **OK** on all dialogs to apply changes.

9. Open **Command Prompt** and type:
   ```bash
   pdftotext -v
   ```
   If it returns a version number, Poppler is successfully installed and added to your system `PATH`.

---

## 2. Tesseract OCR

Tesseract is used for optical character recognition (OCR) of scanned PDFs or images.

### Installation Steps:

1. Download the Windows installer (`.exe`) from:  
   https://github.com/UB-Mannheim/tesseract/wiki#tesseract-installer-for-windows

2. Run the installer and follow the setup wizard to complete the installation.

3. (Optional) Add Tesseract to the system `PATH` during installation, or manually afterward if needed.

4. If you are adding manually, go to the path where the tesseract is installed: `C:/Program Files/Tesseract-OCR/` and add it in `Path` variable in `System Variables` in `Environment Variables`.

---