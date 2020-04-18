import turtle

# initialization
t=turtle.Turtle()
t.speed(0)
t.up()
t.bk(200)
t.down()

# ask for data file name
fname=input('enter data file name: ')
print('reading from file: '+fname)

# create an empty list datalines
datalines=[]

# read lines from the data file into the list datalines
with open(fname) as df:
    datalines=df.readlines()

# check what's there in datalines
print('datalines:')
print(datalines)

# loop over each line in the list and do something with line
for dl in datalines:
    amt=int(dl)
    # move upward by distance 'amt'
    t.lt(90)
    t.fd(amt)
    t.bk(amt)
    t.rt(90)
    # shift turtle little to right to prepare it for the next iteration
    t.up()
    t.fd(10)
    t.down()

print('end of program')
