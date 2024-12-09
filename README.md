# Szkolenie z analizy danych w Python [9-12.12.24]

Linkedin: https://www.linkedin.com/in/tomasz-wilinski/

email: tomasz.wilinski97@gmail.com

--------------------------------------------------------------------------------------

## NUMPY

o module numpy.linalg: https://numpy.org/doc/stable/reference/routines.linalg.html

o module numpy.random: https://numpy.org/doc/stable/reference/random/legacy.html

##### Losowanie 6 liczb z przedziału [1, 49] bez powtórzeń
```python
numbers = np.random.choice(np.arange(1, 50), size=6, replace=False)
print(numbers)
```