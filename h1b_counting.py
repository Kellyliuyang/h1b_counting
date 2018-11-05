import csv  # import csv module

input_file = './input/h1b_input.csv'   # input file name
data = []  # create an empty list to store data
# read data from file
with open(input_file, newline = '',encoding = 'utf-8') as file:
    csv.field_size_limit(100000000)
    reader = csv.reader(file,delimiter=';', quotechar='|')
    for row in reader:
        data.append(row)
column_name=data[0] #column name corresponding to the first row
del data[0] #delete column name from the data


#find the column number for the job tile and state
for i in range(len(column_name)):
    if column_name[i]=='JOB_TITLE':
        o=i
    elif column_name[i]=='EMPLOYER_STATE':
        s=i

#find the all the occupation and state of certified application
occupation = []
state = []
for i in range(len(data)):
    if data[i][2] == 'CERTIFIED':
        occupation.append(data[i][o]) #occupation are found to be in column15
        state.append(data[i][s])  ##state are found to be in column11

total_num_certified = len(state) #this is the total number of certified application

def count(list):
    """
    :param list: input list
    :return: occurrence of items in the list in a dictionary
    """
    d = {}
    for i in list:
        if i in d:
            d[i] = d[i]+1
        else:
            d[i] = 1
    return d

def top10(items):
    """
    :param items: a dictionary with items and its occurrence
    :return: the top 10 items with their count and percentage
    """
    # read from the input dictionary to separate items and its count into different list
    l = []
    count_l = []
    for i in items:
        l.append(i)
        count_l.append(items[i])
    # find the top 10 items and their counts and percentages
    top10 = []
    top10_count = []
    top10_percent = []
    for i in range(10):
        max_count = max(count_l)
        index = count_l.index(max_count)
        l_top10 = l[index]
        percent = "{0:.1%}".format(max_count / total_num_certified)
        top10_count.append(max_count)
        top10.append(l_top10)
        top10_percent.append(percent)
        count_l.remove(max_count)
        l.remove(l_top10)
        output=[top10, top10_count, top10_percent]
        if count_l == []:
            break
    return output

occupation_count = count(occupation) #call the count function to find the count of different occupations
top_10_occupation=top10(occupation_count) #call the top10 function to find the top 10 occupation
#write the file into txt format
file = open('./output/top_10_occupations.txt','w')
file.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE'+'\n')
for i in range(len(top_10_occupation[0])):
    row = [top_10_occupation[0][i],str(top_10_occupation[1][i]),str(top_10_occupation[2][i])]
    row = ';'.join(row)
    file.write(row + '\n')

state_count = count(state) #call the count function to find the count of different states
top_10_state = top10(state_count)  #call the top10 function to find the top 10 states
#write the file into txt format
file2 = open('./output/top_10_states.txt','w')
file2.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE'+'\n')
for i in range(len(top_10_state[0])):
    row = [top_10_state[0][i],str(top_10_state[1][i]),str(top_10_state[2][i])]
    row = ';'.join(row)
    file2.write(row + '\n')
