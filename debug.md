https://pymotw.com/3/pdb/

# start pdb

## @intepretor:
```python
import pdb
pdb.run('statement')
```

## @failure
```python
#some failure
import pdb
pdb.pm() #for post mortem
```

## @set startpoint in script.py
```python
import pdb
#some statement
pdb.set_trace()
#more statement
```

## @cmd
python3 -m pdb script.py

# control
Step
Next line
Reture something
List
Continue to breakpoint
Up/Down a stack
Break
