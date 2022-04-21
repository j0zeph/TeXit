# **TeXit**
### A commandline utility to add TeX syntax to a textfile,<br>
### based on markers that are specified in the lines of that text file.
<br>

---
<br>

> ## <u>Examples of markers and their meaning, effect, and resulting TeX syntax</u>
<br>


| **Marker** | **Meaning**     | **Example**              | **Effect**           | **TeX syntax**                 |
|------------|-----------------|--------------------------|----------------------|--------------------------------|
| **-bf**    | bold            | -bf sample               | **sample**           | \textbf{sample}                |
| **-bp**    | bullet point    | -bp sample               | * sample             | \bullet\large\text{sample}     |
| **-bbr**   | newline (large) | sample<br>-bbr<br>sample | sample<br><br>sample | $$ $$                          |
| **-br**    | newline(small)  | sample<br>-br<br>sample  | sample<br>sample     | $$$$                           |
| **-und**   | underline       | -und sample              | sample               | \underline{\large\text{sample} |

<br>
