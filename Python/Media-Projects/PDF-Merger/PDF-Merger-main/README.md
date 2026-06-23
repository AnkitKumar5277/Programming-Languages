The script provided is a Python script that uses the `PyPDF2` library to merge all PDF files in the current directory into a single PDF file named "combined.pdf". Here is a detailed explanation of the script:

1. **Import Libraries**:
    ```python
    import PyPDF2
    import os
    ```
    The script imports the necessary libraries: `PyPDF2` for handling PDF files and `os` for interacting with the operating system.

2. **Create a PdfMerger Object**:
    ```python
    merger = PyPDF2.PdfMerger()
    ```
    The `PdfMerger` object from `PyPDF2` is created. This object will be used to merge multiple PDF files.

3. **Iterate Through Files in the Current Directory**:
    ```python
    for file in os.listdir(os.curdir):
        if file.endswith(".pdf"):
            merger.append(file)
    ```
    The script uses `os.listdir(os.curdir)` to list all files in the current directory. It then iterates through each file and checks if the file name ends with ".pdf" (i.e., if the file is a PDF). If it is, the file is appended to the `merger` object.

4. **Write the Combined PDF**:
    ```python
    merger.write("combined.pdf")
    ```
    Finally, the script writes the combined PDF to a file named "combined.pdf".

Here is the complete script:

```python
import PyPDF2
import os

merger = PyPDF2.PdfMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
merger.write("combined.pdf")
```

**Explanation of File Contents**:
- The script starts by importing necessary libraries.
- It initializes a `PdfMerger` object.
- It loops through all files in the current directory, appending each PDF file it finds to the `PdfMerger` object.
- Finally, it writes the combined PDF to a new file called "combined.pdf".
