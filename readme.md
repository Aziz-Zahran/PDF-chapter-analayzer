# Questions per chapter counter
---
- This is really useful if you are cramming before an exam. it extracts how many the chapters from questions paper using their keywords and then matches them to their corresponding chapter, you can create a chart using the data by using the `chart.py `file or using excel if you'd like
---
## Dependencies

```python
pip install matplotlib
```

```python
pip install PyPDF2
```
---
## Setup
For `chapters` Replace the "x" with chapter name and y, w, z, accordingly to the keywords of the chapter, you can add as much as you like
```python
chapters = {

    "1.1 x": ["y", "yy","yyy"],
    "1.2 xx": ["w", "ww", "www"],
    "1.3 xxx": ["z", "zz", "zzz"],
}
```

Next change: 
`yourpdfname.pdf` to the filename of the pdf you want to go through(make sure its in the same directory)

---
## Disclaimer
I wouldnt consider this to be 100% accurate, especially when working with a large size pdf

---
## For [[chart.py]]

Change `x,y,z` according to chapter names
Change the numbers to the results from [[main.py]]


