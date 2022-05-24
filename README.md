## TeXit

A commandline utility to add TeX syntax to a textfile,<br>
based on markers that are specified in that text file.<br>

---

### Markers, their meanings, effects, and resulting TeX syntax
<br>

| **Marker** | **Meaning**     | **Example**              | **Effect**           | **TeX syntax**                 |
|------------|-----------------|--------------------------|----------------------|--------------------------------|
| **-bf**    | bold            | -bf sample               | **sample**           | \textbf{sample}                |
| **-bp**    | bullet point    | -bp sample               | * sample             | \bullet\large\text{sample}     |
| **-bbr**   | newline (large) | sample<br>-bbr<br>sample | sample<br><br>sample | $$ $$                          |
| **-br**    | newline(small)  | sample<br>-br<br>sample  | sample<br>sample     | $$$$                           |
| **-und**   | underline       | -und sample              | sample               | \underline{\large\text{sample} |

<br>

### Usage
<br>

```
python texit.py <filepath|filename>
```
<br>

### Example<br>

```example.txt```

```
-bf Lorem Ipsum

Lorem ipsum dolor sit amet, consectetur adipiscing elit,
-und sed do eiusmod tempor incididunt ut labore et dolore
magna aliqua.

Ut enim ad minim veniam, quis nostrud exercitation
ullamco laboris nisi ut:

-bp aliquip ex ea
-bp commodo consequat
```
<br>

```
python texit.py example.txt
```
<br>

```example_texit_out.txt```

```
$$
\large\textbf{Lorem Ipsum}\\
$$$$
\large\text{Lorem ipsum dolor sit amet, consectetur adipiscing elit,}\\
\underline{\large\text{sed do eiusmod tempor incididunt ut labore et dolore}}
\large\text{magna aliqua.}\\
$$$$
\large\text{Ut enim ad minim veniam, quis nostrud exercitation}\\
\large\text{ullamco laboris nisi ut:}\\
$$$$
\bullet\large\text{ aliquip ex ea}\\
\bullet\large\text{ commodo consequat}\\
$$
```
<br>

```Rendered syntax (rendered by generic Tex renderer```<br>

![Syntax rendered in a generic TeX renderer](images/lorem_ipsum_rendered.jpg)