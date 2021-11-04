https://pyinstaller.readthedocs.io/en/stable/
https://docs.python.org/3/library/argparse.html
https://pypi.org/project/PyPDF4/, https://github.com/claird/PyPDF4

The code is compiled with 
```powershell
PS projectroot> pyinstaller --onefile .\src\pdftool\pdfmerge.py
```
or 
```powershell
PS projectroot> pyinstaller pdfmerge.spec
```


Add '\pdftool\dist' to path. 

Run 
```powershell
PS> pdfmerge file1.pdf file2.pdf
```
and the merged pdf is output to `merged.pdf`.

For testing/development `pdfmerge.py` may be run with
```powershell
PS projectroot> poetry run merge -- "file1.pdf" "file2.pdf"
```