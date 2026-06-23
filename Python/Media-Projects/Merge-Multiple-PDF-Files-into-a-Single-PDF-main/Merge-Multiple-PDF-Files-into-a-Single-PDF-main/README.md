steps :

1. Sabse pehle `PyPDF2` library ko import kiya gaya hai. Yeh library PDF files ke manipulation ke liye use hoti hai.
   
2. `files` list mein do PDF files ke names hai, jinhein merge karna hai.

3. `PyPDF2.PdfMerger()` se ek merger object `merger` create kiya gaya hai, jo merge karne ke liye PDF files ko hold karega.

4. Fir `for` loop chalaya gaya hai `files` list ke har ek element (PDF file name) ke liye:
   - Har PDF file ko `open()` function se binary read mode (`'rb'`) mein open kiya jata hai.
   - `merger.append(file)` se har file ko `merger` object mein append kiya jata hai, yani merge ke liye tayyar kiya jata hai.

5. Jab saare files merge ho jate hain, `merger.write('saved.pdf')` se `merger` object ke contents ko `'saved.pdf'` naam se ek naye PDF file mein write kiya jata hai.

6. `merger.close()` se merger object ko band kiya jata hai, jisse saare resources properly release ho jaye.

Is code ka use kisi bhi do PDF files ko ek single PDF file mein merge karne ke liye kiya ja sakta hai.
