import PyPDF2
files = ["first.pdf", "second.pdf"] # you can add more pdf's
merger = PyPDF2.PdfMerger()
for filename in files:
    new = open(filename, 'rb')
    read = PyPDF2.read(new)
    merger.append(read)
new.close()
merger.write('total.pdf')
